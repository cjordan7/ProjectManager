
import os
import subprocess
import glob

from GeneralVar import Generals

class Manager:
    def backup(self):
        # TODO: SPlit in several functions
        # TODO: Backup of most important files
        # TODO: .emacs, .emacs.d, files with path github projects...
        # TODO: push files to github
        print("Something")

    def emacsBackup(self):
        subprocess.call(Generals.subLibraryScripts+"./backup.sh", shell=True, executable='/bin/bash')
        
        
    def deleteEmacsBackup(self, path):
            for root, dirs, files in os.walk(path):
                for f in files:
                    os.unlink(os.path.join(root, f))
                    print(f)
                    for d in dirs:
                        print(d)
                        shutil.rmtree(os.path.join(root, d))
                        
    def printProjectsPath(dictio):
        for key, value in dictio.items():
            print("{:>20}  {:>1}  {:>20}".format(key, ":", value))

            
