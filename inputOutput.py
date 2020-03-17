
import glob
import os
from GeneralVar import Generals


class iop:
    def createFile(self, fileName):
        f = open(fileName, "w+")

    def getNames(self, path):
        os.chdir(path)
        print("Here========")
        for file in glob.glob("*"):
            print(file)

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
        fileNames = Generals.fileNames

        dictioOfFileNames = {}

        for i in fileNames:
            dictioOfFileNames[i] = self.read(Generals.subLibraryLanguage+i)

        return dictioOfFileNames

# TODO: Implements CSV files
