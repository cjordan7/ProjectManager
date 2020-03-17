
import glob
import os
from inputOutput import iop
from manager import Manager
from GeneralVar import Generals


def printProjectsPath(dictio):
    for key, value in dictio.items():
        print("{:>20}  {:>1}  {:>20}".format(key, ":", value))

# printProjectsPath(projectsPathCPlusPlus)


i = iop()
dictio = i.readAll()

print(dictio)
manage = Manager()
print("what.. ")
print(dictio.keys())
print("=======")
manage.gitStatusFull(dictio)
manage.pushAll(dictio)

print("==================================")

current = Generals.getCurrentDir() + Generals.subLibraryLanguage
print(current)
print("==================================")
i.getNames("Documents/Programming/Python/pythonManager")
            
