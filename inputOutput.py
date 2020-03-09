
class iop:    
    def createFile(self, fileName):
        f = open(fileName, "w+")
        
#    def createFile():
#

    def read(self, fileName):
        dictio = dict()
        f = open(fileName, "r")
        
        f1 = f.readlines()
        for line in f1:
            # TODO: Create files swift, python,...
            first, second = line.replace(" ", "").split(":")
            dictio[first] = second
        
        f.close()

        return dictio
        
    def readAll(self):
        fileNames = {"python", "swift", "cpp", "c", "iOS"}

        dictioOfFileNames = {}
        
        for i in fileNames:
            dictioOfFileNames[i] = read(i)

        return dictioOfFileNames
