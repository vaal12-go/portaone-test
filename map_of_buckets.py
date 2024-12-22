from fragment import Fragment

class Bucket:
    def __init__(self):
        self.bucketList = []
        self.currentItem = 0
    
    def addFragment(self, fragment):
        self.bucketList.append(fragment)

class MOB:
    def __init__(self, fragmentList):
        self.stringDict = {}
        for fragment in fragmentList:
            bucketObj = self.stringDict.get(fragment.tail)
            if bucketObj == None:
                bucketObj = Bucket()
                self.stringDict[fragment.tail] = bucketObj
            bucketObj.addFragment(fragment)
