#! /usr/bin/env python3

import os

class DirPath:
    def __init__(self):
        self.dir_path = str(input("\nDiretório Para o Download: "))
        self.home = os.getenv("HOME") + "/"
        self.dir_default_download = self.home + "/Downloads/yt-dwl"
        self.directorys = self.dir_path.split("/")

    def SetDir(self):
        if "~" in self.directorys:
            self.directorys = self.directorys[1:len(self.directorys)]
            self.strDire = "/".join(self.directorys)
            self.dir_path = self.home + self.strDire

        if len(self.dir_path) == 0:    
            if not os.path.exists(self.dir_default_download):
                os.makedirs(self.dir_default_download)

            self.dir_path = self.dir_default_download
            print(f"\n\033[1;33m[WARNING] \033[1;37mDiretório de Download Definido Para: {self.dir_path} ")
        
        if os.path.isdir(self.dir_path) == False:
            print("\n\033[1;31m[ERROR]\033 Diretório Inexistente\n")
            exit()

        return self.dir_path

