__author__ = 'Kaiqun'

import pyodbc
import os

# THis file inserts database records from excel sheets

def InsertionHandle(StationID, DateT, ChannelIndex, CountList):
    for i in range(len(CountList)):
        dataInsert(StationID, DateT, ChannelIndex, i + 1, CountList[i])


def dataInsert(StationID, DateT, ChannelIndex, Class, Count):
    currentPath = os.path.dirname(os.path.realpath(__file__))

    with open(currentPath + '/DBCredentials/MSSQL', 'r') as crdts:
        CrStr = crdts.readline()
        DBDriver = CrStr.split(',')[0]
        DBServer = CrStr.split(',')[1]
        DBDatabase = CrStr.split(',')[2]
        DBUid = CrStr.split(',')[3]
        DBPwd = CrStr.split(',')[4]

    connStr = 'DRIVER={%s};SERVER=%s;DATABASE=%s;UID=%s;PWD=%s' % (DBDriver, DBServer, DBDatabase, DBUid, DBPwd)

    cnxn = pyodbc.connect(connStr)
    cursor = cnxn.cursor()

    try:
        InsertCommand = "insert into [speed].[tirs].[LoopsClass_new] values ('" + StationID + "','" + DateT + "'," + str(
            ChannelIndex) + "," + str(Class) + "," + str(Count) + ")"
        cursor.execute(InsertCommand)
        cnxn.commit()
        return "OK"
    except Exception, e:
        print 'Some Error'
        return None