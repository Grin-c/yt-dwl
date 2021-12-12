import sys
from time import sleep
from Download import Download
from Download import SetUrl
from FilePath import FilePath

def Loading():
    for c in range(1,4):
        ponto = "." * c
        sys.stdout.write(f"\033[1;37mLoading{ponto}\r")
        sys.stdout.flush()
        sleep(0.25)

def DownloadType():
    print('''\nDownload Options

        [0] => Video
        [1] => Áudio
    ''')
    option = int(input("Download Option: "))

    if option < 0 or option > 1:
        print("\nNúmero inválido \n")
        Option()
    
    if option == 0:
        cfg_download = {
            "option"    : 0,
            "extension" : ".mp4"
        }
    elif option == 1:
        cfg_download = {
            "option"    : 1,
            "extension" : ".mp3"
        }
    else:
        print("\nOpção Inválida \n")
        Option()

    return cfg_download

Loading()

dir_path = FilePath().VerifyPath()

cfg_download = DownloadType()
option = cfg_download["option"]
extension = cfg_download["extension"]

while True:

    SetUrl()

    Download(dir_path, extension).ManageName()

    if int(option) == 0:
        Download(dir_path, extension).DownloadVideo()

    else:
        Download(dir_path, extension).DownloadAudio()