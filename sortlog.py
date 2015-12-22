__author__ = 'Kaiqun'

import json
import os

currentPath = os.path.dirname(os.path.realpath(__file__))

with open(currentPath + '/logs/log_new.json', 'a+') as data_file:
    PreviousFiles = json.load(data_file)

tmpdict = PreviousFiles[PreviousFiles.keys()[0]]
tmplist = tmpdict[tmpdict.keys()[0]]

for station in tmplist:
    tempList = tmplist[station]
    tmplist.update({station: sorted(tempList)})

tmpdict.update({tmpdict.keys()[0]: tmplist})
PreviousFiles.update({PreviousFiles.keys()[0]: tmpdict})

with open(currentPath + '/logs/log1.json', 'w') as data_file:
    json.dump(PreviousFiles, data_file)
