from fragment import Fragment


def parseFile(fName):
    f = open(fName, "r")
    retList = []
    for line in f:
        # print("Have line:", line.strip())
        currFrag = Fragment(line)
        # print("\t frag:", currFrag, "\n")
        retList.append(currFrag)
    f.close()
    return retList


def mainFunc():
    mainFragList = parseFile("source.txt")


if __name__ == "__main__":
    mainFunc()