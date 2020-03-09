
import os
import subprocess
import functools
from inputOutput import iop
from manager import Manager

cdTo = """
cd ~ && cd 
"""

gitAll = """
    git status
    git add .
    git commit -m "Commit on $(date)"
    git push
"""


projectPathiOS = {
    "ToDoListApp" : "Documents/Programming/iOS"
}

projectPathSwift = {
    "OrgMode-Generator" :
    "Documents/Programming/Swift/Projects/EmacsUsefulFunction/OrgMode-Generator",
    "" : ""
}

projectsPathC = {
    "" : ""
}

projectPathPython = {
    "pythonManager" : "Documents/Programming/Python/pythonManager"
}



def cdToPath(path):
    subprocess.call(cdTo + path, shell=True, executable='/bin/bash')

def printProjectsPath(dictio):
    for key, value in dictio.items():
        print("{:>20}  {:>1}  {:>20}".format(key, ":", value))

#printProjectsPath(projectsPathCPlusPlus)

def pushPath(path):
    cdToPath(path)
    gitAll()
    
def pushAll():
    print("Holy hell")
    
def gitAll():
    subprocess.call(gitAll, shell=True, executable='/bin/bash')
    #subprocess.call("./gitAll.sh", shell=True)

i = iop()
dictio = i.readAll()

manage = Manager()

#"/Users/cosmejordan/Documents/EmacsBackups"
#manage.deleteEmacsBackup("/Users/cosmejordan/Documents/EmacsBackups")

print(dictio)
