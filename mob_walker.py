import globs
from utils import *


def MOBWalker(itemList):
    if len(itemList) == 0:
        # Should iterate all the fragments
        keys = list(globs.sOBject.stringDict.keys())
        itmsIterated = 0
        if globs.DEBUG:
            print(f"MOBWalker. Quantity of keys:{len(keys)}")
            print(f"    MOBWalker.   Keys:{keys}")
        
        keyNoIterated = 0
        for key in keys:
            if globs.DEBUG:
                print(f"\n\n  --- Key #{keyNoIterated+1} iteration starts. MapKey:{key} \n\n")
            bucketObj = globs.sOBject.stringDict[key]
            i=0
            while i<len(bucketObj.bucketList):
                fragm = bucketObj.bucketList[i]
                newList = [fragm]
                i += 1
                itmsIterated += 1
                yield from MOBWalker(newList)
            keyNoIterated += 1
            # print("Keys iterated:", keyNoIterated)
        if globs.DEBUG:
            print(f"Total items (keybuckets which should correspond to number of lines in the file) iterated:{itmsIterated}")
    else: #if len(itemList) == 0:
        shouldReturnThisItemList = True
        lastHead = itemList[len(itemList)-1].head
        bckt = globs.sOBject.stringDict.get(lastHead)
        if bckt != None:
            i=0
            while i<len(bckt.bucketList):
                fragm = bckt.bucketList[i]
                i += 1
                if not (fragm in itemList):
                    shouldReturnThisItemList = False
                    itemListCP = itemList.copy()
                    itemListCP.append(fragm)
                    yield from MOBWalker(itemListCP)
            # END while i<len(bckt.bucketList):
        # END if bckt != None:
        if shouldReturnThisItemList and len(itemList)>1:
            yield itemList
    # else: #if len(itemList) == 0:
# END def MOBWalker(itemList):







# TEST SOURCE
# 942517
# 605676
# 498291
# 668826
# 357057
# 171060
# 761049
# 911094
# 941094
# 948894