#! /usr/bin/env python3

from pytube import YouTube
import sys
import os
from time import sleep

def Loading():
    for c in range(1,4):
        ponto = "." * c
        sys.stdout.write(f"\033[1;37mLoading{ponto}\r")
        sys.stdout.flush()
        sleep(0.25)

def DownloadOption():
    print('''Download Options

    [0] => Video
    [1] => Audio
    ''')
    option = int(input("Download Option: "))

    if option < 0 or option > 1:
        print("\nNúmero inválido tente novamente\n")
        DownloadOption()
    
    if option == 0:
        while True:
            GetVideo()
    else:
        while True:
            GetAudio()

def FilePath():
    global file_path
    file_path = str(input("\nDiretório de Download: "))
    home = os.getenv("HOME") + "/"
    directorys = file_path.split("/")

    if "~" in directorys:
        directorys = directorys[1:len(directorys)]
        strDire = "/".join(directorys)
        file_path = home + strDire

    if len(file_path) == 0:
        file_path = os.getenv("HOME") + "/Downloads"
    
    if os.path.isdir(file_path) == False:
        print("\nDiretório inexistente, tente novamente\n")
        FilePath()   

def GetVideo():
    url = str(input("\nLink do vídeo: "))
    video = YouTube(url, on_progress_callback=BarDownloadProgress)
    FilePath()
    titulo = video.title
    global stream
    stream = video.streams.get_highest_resolution()
    Download(file_path, titulo, ".mp4")

def GetAudio():
    url = str(input("\nLink do vídeo: "))
    video = YouTube(url, on_progress_callback=BarDownloadProgress)
    FilePath()
    titulo = video.title
    global stream
    stream = video.streams.get_audio_only()
    Download(file_path, titulo, ".mp3")

def BarDownloadProgress(chunk, file_handle, bytes_remaining):
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

def Download(file_path, titulo, extension):
        print("\n\033[1;33m[WARNING] \033[1;37mBaixando o vídeo na melhor resolução\n")
        print(f"Downloading: {titulo}\n")
        stream.download(file_path, titulo+extension)
        print("\n\n\033[1;32mDownload finalizado\033[1;37m\n")
