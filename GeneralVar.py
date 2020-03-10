
class Generals:
    # General path to sub-library
    subLibraryLanguage = "Language/"
    subLibraryScripts = "Scripts/"
    fileNames = {"python", "swift", "cpp", "c", "iOS"}
    cdRoot = "cd ~"
    gitAll = 'git status && git add . && git commit -m \"Commit on $(date)\" && git push'

    @staticmethod
    def cdToPath(i):
        return Generals.cdRoot + " && cd " + i.strip()

    @staticmethod
    def printSep():
        print("==========================================================")
        print("==========================================================")

    @staticmethod
    def printProjectsPath(project, path):
        print("Project: " + project)
        print("Path: " + path)
