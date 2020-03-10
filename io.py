
class iop:
    def createFile(fileName):
        f = open(fileName, "w+")
        
#    def createFile():
#

    def read(fileName):
        dictio = dict()
        f = open(fileName, "r")
        
        f1 = f.readLines()
        for line in f1:
            # TODO: Create files swift, python,...
            first, second = line.split(":")
            dic[first] = second
        
        f.close()

        return dictio
        
    def readAll():
        fileNames = {"python", "swift", "cpp", "c", "iOS"}

        dictioOfFileNames = {}
        
        for i in fileNames:
            dictioOfFileNames[i] = read(i)

        return dictioOfFileNames
