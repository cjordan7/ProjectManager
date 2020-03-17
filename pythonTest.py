
import glob
import os
from inputOutput import iop
from manager import Manager
from GeneralVar import Generals


def printProjectsPath(dictio):
    for key, value in dictio.items():
        print("{:>20}  {:>1}  {:>20}".format(key, ":", value))


# f = open("Language/applescript", "r")
# f1 = f.readlines()
# for line in f1:
#     print(line)
# f.close()
i = iop()
dictio = i.readAll()

manage = Manager()
manage.gitStatusFull(dictio)
manage.pushAll(dictio)

print("==================================")

current = Generals.getCurrentDir() + "/" + Generals.subLibraryLanguage
# print(i.getNames(current))
