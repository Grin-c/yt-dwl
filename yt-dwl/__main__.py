#! /usr/bin/env python3

import sys
from time import sleep
from src.main.download import Download
from src.main.dir_path import DirPath

try: 
    # Loading Animation
    for c in range(1,4):
            dot = "." * c
            sys.stdout.write(f"\033[1;37mLoading{dot}\r")
            sys.stdout.flush()
            sleep(0.25)

    print('''Download Options

    [0] => Video
    [1] => Audio
    ''')
    option = int(input("Download Option: "))

    # Checking if the option is valid
    if option < 0 or option > 1:
        print("\n\033[1;31m[ERROR]\033[1;37m Invalid number\n")
        exit()

    # Defining directory
    dir_path = DirPath().SetDir()

    # Downloading video format according to option
    while True:
        url = str(input("\nVideo URL: "))
        download = Download(url, dir_path)
        download.SetVideo()

        if option == 0:
            download.DownloadVideo()
        else:
            download.DownloadAudio()
except KeyboardInterrupt:
    exit(print())