import os

class FilePath:
    def __init__(self):
        self.dir_path = str(input("\n\nDiretório para Download: "))
        self.home = os.getenv("HOME") + "/"
        self.dir_default_download = self.home + "/Downloads/yt-dwl"
        self.directorys = self.dir_path.split("/")
    
    def VerifyPath(self):
        if "~" in self.directorys:
            self.directorys = self.directorys[1:len(self.directorys)]
            self.strDire = "/".join(self.directorys)
            self.dir_path = self.home + self.strDire

        if self.dir_path == "dev":
            self.dir_path = "/home/rodf/Prog/Projetos/Python/yt-dwl/DwlTest"

        if len(self.dir_path) == 0:    
            if not os.path.exists(self.dir_default_download):
                os.makedirs(self.dir_default_download)
            self.dir_path = self.dir_default_download
        
        if os.path.isdir(self.dir_path) == False:
            print("\nDiretório inexistente\n")

        return self.dir_path

        print("\n\033[1;33m[WARNING] \033[1;37mDiretório salvo para essa sessão\n")
