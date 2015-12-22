# Monitors the source files for any new insertions new excel files for loops only. Once it finds new excel file database operations.py does the insertion
from os import listdir
from os.path import isfile, join, isdir
import json
import os

currentPath = os.path.dirname(os.path.realpath(__file__))


def newfiledetector(targetdir, targetYear):
    returningList = []

    # CAUTION! the JSON file must be under json format: {}
    with open(currentPath + '/logs/log.json', 'a+') as data_file:
        PreviousFiles = json.load(data_file)

    targetTypes = [targetdir + '\\' + f for f in listdir(targetdir) if isdir(join(targetdir, f))]

    # onetype is the data type: Class, Volume, Speed
    for onetype in targetTypes:

        # Only select Class for now.
        if onetype.split('\\')[-1:][0] != 'Class':
            continue

        # In case of new data types add in
        if onetype not in PreviousFiles:
            PreviousFiles[onetype] = {}

        # targetYear is the specific Year
        yeardir = onetype + '\\' + targetYear

        # In case of new year
        if yeardir not in PreviousFiles[onetype]:
            PreviousFiles[onetype][yeardir] = {}

        StationIDs = [yeardir + '\\' + f for f in listdir(yeardir) if isdir(join(yeardir, f))]

        # onestation is the StationID
        for onestation in StationIDs:

            # In case of new stations add in
            if onestation not in PreviousFiles[onetype][yeardir]:
                PreviousFiles[onetype][yeardir][onestation] = []

            sourcefiles = [onestation + '\\' + f for f in listdir(onestation) if isfile(join(onestation, f))]

            set_PreviousFiles = set(PreviousFiles[onetype][yeardir][onestation])
            set_CurrentFiles = set(sourcefiles)

            PreviousFiles[onetype][yeardir][onestation] = list(set_CurrentFiles | set_PreviousFiles)
            returningList.extend(list(set_CurrentFiles - set_PreviousFiles))

    with open(currentPath + '/logs/log.json', 'w') as data_file:
        json.dump(PreviousFiles, data_file)

    return returningList

    # Commet out
    # import datetime
    # print newfiledetector('C:\\ProgramData\\Peek Traffic\\Viper\\Output1\\Binned Data Reports', datetime.datetime.now().strftime('%Y'))