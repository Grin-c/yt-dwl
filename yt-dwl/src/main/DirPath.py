#! /usr/bin/env python3

import os

class DirPath:
    def __init__(self):
        self.dir_path = str(input("\nDirectory to download: "))
        self.home = os.getenv("HOME") + "/"
        self.dir_default_download = self.home + "Downloads/yt-dwl"
        self.directorys = self.dir_path.split("/")

    def SetDir(self):
        # If passed '~' it will be the home directory
        if "~" in self.directorys:
            self.directorys = self.directorys[1:len(self.directorys)]
            self.strDire = "/".join(self.directorys)
            self.dir_path = self.home + self.strDire

        # Setting a default directory if none is passed
        if len(self.dir_path) == 0:    
            # Creating directory if it does not exist
            if not os.path.exists(self.dir_default_download):
                os.makedirs(self.dir_default_download)

            self.dir_path = self.dir_default_download
            print(f"\n\033[1;33m[WARNING] \033[1;37mDownloading directory set to: {self.dir_path} ")
        
        if os.path.isdir(self.dir_path) == False:
            print("\n\033[1;31m[ERROR]\033 Non-existent directory\n")
            exit()

        return self.dir_path
