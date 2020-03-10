
import os
import subprocess
from GeneralVar import Generals


class Manager:
    def backup(self):
        # TODO: SPlit in several functions
        # TODO: Backup of most important files
        # TODO: .emacs, .emacs.d, files with path github projects...
        # TODO: push files to github
        print("Something")

    def emacsBackup(self):
        subprocess.call(Generals.subLibraryScripts+"./backup.sh",
                        shell=True, executable='/bin/bash')

    def deleteEmacsBackup(self, path):
            for root, dirs, files in os.walk(path):
                for f in files:
                    os.unlink(os.path.join(root, f))
                    print(f)
                    for d in dirs:
                        print(d)
                        shutil.rmtree(os.path.join(root, d))

    def printProjectsPath(self, dictio):
        for key, value in dictio.items():
            print("{:>20}  {:>1}  {:>20}".format(key, ":", value))

    def gitStatusOne(self, dictio):
        for key, value in dictio.items():
            Generals.printSep()
            path = Generals.cdToPath(value)
            command = path + " && git status"
            print("Here: " + value)
            subprocess.call(command,
                            shell=True, executable='/bin/bash')

    def gitStatusFull(self, dictio):
        for i in dictio:
            self.gitStatusOne(dictio[i])

    def gitAll(self):
        subprocess.call(Generals.gitAll, shell=True, executable='/bin/bash')

    def pushPath(self, path):
        Generals.cdToPath(path)
        self.gitAll()

    def pushOne(self, dictio):
        for key, value in dictio.items():
            Generals.printSep()
            path = Generals.cdToPath(value)
            print(value)
            command = path + " && " + Generals.gitAll
            subprocess.call(command,
                            shell=True, executable='/bin/bash')

    def pushAll(self, dictio):
        for i in dictio:
            self.pushOne(dictio[i])
