import sys
import datetime
from fragment import Fragment
from map_of_buckets import MOB
import globs

from utils import *
from mob_walker import *


NUMBER_OF_ITEM_LISTS_TO_SKIP = 100000
SOURCE_FILE_NAME = "source.txt"

def parseFile(fName):
    f = open(fName, "r")
    retList = []
    for line in f:
        if len(line.strip())>0:
            currFrag = Fragment(line)
            retList.append(currFrag)
    f.close()
    print(f"Number of file entries (lines):{len(retList)}")
    return retList


def mainFunc():
    mainFragList = parseFile(SOURCE_FILE_NAME)

    sys.setrecursionlimit(len(mainFragList)*10)

    globs.sOBject = MOB(mainFragList)
    i=0
    counter_i = 1
    longestListLen = 0
    longestLists = []
    
    for itemList in MOBWalker([]):
        if globs.DEBUG:
            if (counter_i >= NUMBER_OF_ITEM_LISTS_TO_SKIP):
                counter_i = 0
                print(f"Number of lists received from MOBWalker:{i+1}")
                # print(f"Item list received (#{i}, len={len(itemList)})")
                # printList(itemList)
        if globs.WITH_CHECKS:
            checkFragmentList(itemList)

        res = f""
        
        i += 1
        counter_i += 1

        if len(itemList)>longestListLen:
            longestListLen = len(itemList)
            longestLists = []
        if len(itemList) == longestListLen:
            longestLists.append(itemList)
            if globs.DEBUG:
                printLists(longestLists)
            if globs.WITH_CHECKS:
                checkListOfLists(longestLists)
                # print("Check of list of lists passed.")

    print("\n\n\n *******  FINAL result: ********")
    printLists(longestLists, printComplete=True)
    if globs.WITH_CHECKS:
        checkListOfLists(longestLists)

    finalNum = ""
    if len(longestLists)>0:
        firstList = longestLists[0] 

        for num in firstList:
            finalNum += str(num)[:4]
        finalNum += str(firstList[len(firstList)-1])[4:]

    print("First longest number:\n", finalNum)
    print(f"Length of longest number:{len(finalNum)}")
        
    
    


if __name__ == "__main__":
    startTime = datetime.datetime.now()
    mainFunc()
    endTime = datetime.datetime.now()
    diff = endTime - startTime
    print(f"Program executed in {diff.total_seconds()} seconds")