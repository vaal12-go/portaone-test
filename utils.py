def printLists(lsts, printComplete=False):
    print("\n\n*************************************************")
    if len(lsts) == 0:
        print("!! List is empty.")
        print("*************************************************")
        return
    res = f"Longest lists: {{\n"
    for lst in lsts:
        # res += f"  len={len(lst)} [  "
        res += "  ["
        for itm in lst:
            res += f" {itm}"
        res += " ]\n"
        if not printComplete:
            res += "  List is not printed in full (to save space)   ...\n"
            break
    res += f"}} (noOfLists:{len(lsts)}, listLen:{len(lsts[0])})"
    print(res)
    print("*************************************************")


def findNumberOfEntries(frag, lst):
    # TODO find number of entries of frag in the list
    counter = 0
    for itm in lst:
        if frag == itm:
            counter += 1
    return counter

def checkFragmentList(lst):
    i=0
    while (i+1)<len(lst):
        if lst[i].head != lst[i+1].tail:
            print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"Problem checking list. Item {lst[i]} head does not maths item {lst[i+1]} tail.")
            printList(lst)
            raise Exception("Problem checking list - see output for details")

        if findNumberOfEntries(lst[i], lst)>1:
            print("!!!!!!!!!!!!!!!!!!")
            print(f"May be a problem - duplicated fragments in the list. Fragment:{lst[i]}")
            printList(lst)
        i += 1
    # print("checkFragmentList check result - OK")

def listsAreEqual(lst1, lst2):
    if len(lst1) != len(lst2):
        return False
    i=0
    while i<len(lst1):
        if lst1[i] != lst2[i]:
            return False
        i += 1
    return True

def checkListOfLists(lsts):
    i=0
    while (i+1)<len(lsts):
        currList = lsts[i]
        k=i+1
        while k<len(lsts):
            compList = lsts[k]
            if currList[0] == compList[0] \
                    and \
               listsAreEqual(currList, compList) :
                print("\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("Possible duplicate lists are found:")
                printList(currList)
                printList(compList)
                print("---------------------------\n")
                
            k += 1
        i += 1
    print("Lists of list check-OK")

def printList(lst):
    res = ""
    for itm in lst:
        res += f" {itm}"
    res = f"    || {res} || [{len(lst)}]"
    print(res)
