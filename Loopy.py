__author__ = 'Kaiqun'

from Monitor import newfiledetector
from xlsParsor import onefileoperate
import datetime
import time
import os
# 
# Loopy program parses the source files from CSV and inserts the data to MS SQL file 
#
#

if __name__ == '__main__':
    TheQueue = newfiledetector('C:\\ProgramData\\Peek Traffic\\Viper V1.5.8\\Output1\\Binned Data Reports', datetime.datetime.now().strftime('%Y'))
    if TheQueue == []:
        pass
    else:
        currentPath = os.path.dirname(os.path.realpath(__file__))
        with open(currentPath + '/logs/DailyLog/' + datetime.datetime.now().strftime('%Y-%m-%d') + '.txt', 'w') as data_file:
            data_file.write(','.join(TheQueue))
        for onefile in TheQueue:
            onefileoperate(onefile)
    # time.sleep(30)
    # onefileoperate('003308021896_000000000001_11110000.xlsx')