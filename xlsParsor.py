__author__ = 'Kaiqun'
# the file is called from loopy to parse the data and call database operations
import xlrd
from os import listdir
from os.path import isfile, join
import datetime
from DatabaseOperations import InsertionHandle

#
def BatchOperator(inputPath):
    onlyfiles = [inputPath + '\\' + f for f in listdir(inputPath) if isfile(join(inputPath, f))]

    for file in onlyfiles:
        onefileoperate(file)


def checkistime(ipnutlist):
    try:
        reslt = ipnutlist[1]
        return True
    except IndexError:
        return False


def onefileoperate(filedir):
    currentYear = datetime.datetime.now().strftime('%Y')
    currentDateTime = ''

    onefile = filedir.split('\\')[-1:][0]
    currentDate = currentYear + '-' + onefile.split('_')[-1:][0][:2] + '-' + onefile.split('_')[-1:][0][2:4]
    StationID = onefile.split('_')[-2:][0]

    workbook = xlrd.open_workbook(filedir)

    if 'Sheet1' == workbook.sheet_names()[0]:
        worksheet = workbook.sheet_by_name('Sheet1')
        num_rows = worksheet.nrows - 1

        curr_row = 3
        channelIndex = 0

        while curr_row < num_rows:
            curr_row += 1

            # Break loop if is at bottom
            if worksheet.cell_value(curr_row, 1) == 'Total':
                break

            # Skip Class heading row and Totals
            if worksheet.cell_type(curr_row, 1) == 0 and worksheet.cell_type(curr_row, 2) == 0:
                continue
            if worksheet.cell_value(curr_row, 2) == 'Total':
                continue

            # Counting Channels
            if worksheet.cell_type(curr_row, 1) == 1 and worksheet.cell_value(curr_row, 2) == 'Channel 1':
                currentDateTime = currentDate + ' ' + "%02d" % (
                    int(worksheet.cell_value(curr_row, 1).split(':')[0]) - 1) + ':00:00'
                channelIndex = 1
            else:
                channelIndex += 1

            print StationID + '--' + currentDateTime
            countList = [int(worksheet.cell_value(curr_row, i)) for i in range(3, 20) if
                         worksheet.cell_value(curr_row, i) != '']

            InsertionHandle(StationID, currentDateTime, channelIndex, countList)

    elif 'Sheet' == workbook.sheet_names()[0]:
        worksheet = workbook.sheet_by_name('Sheet')
        num_rows = worksheet.nrows - 1

        curr_row = 7

        while curr_row < num_rows:
            if worksheet.cell_value(curr_row, 14) == 'All Lanes':
                break

            if worksheet.cell_type(curr_row, 0) == 3 and worksheet.cell_type(curr_row, 14) == 1:
                channelIndex = int(worksheet.cell_value(curr_row, 14)[-2:])

                curr_row += 3
                while checkistime(worksheet.cell_value(curr_row, 0).split(':')):
                    currentDateTime = currentDate + ' ' + worksheet.cell_value(curr_row, 0) + ':00'
                    countList = [int(worksheet.cell_value(curr_row, i)) for i in range(17) if
                                 worksheet.cell_type(curr_row, i) == 2]
                    print StationID + '--' + str(channelIndex) + '--' + currentDateTime
                    InsertionHandle(StationID, currentDateTime, channelIndex, countList)
                    curr_row += 1

            curr_row += 1

    else:
        print 'No Sheet Name Found!'
        return ""


        # BatchOperator('D:\\Software\\LoopsInsert\\testingData\\Class\\2015\\000000000001')