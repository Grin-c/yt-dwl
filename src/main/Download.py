#! /usr/bin/env python3

import sys
import os
from time import sleep
from pytube import YouTube
from pytube import exceptions

def Loading():
    for c in range(1,4):
        ponto = "." * c
        sys.stdout.write(f"\033[1;37mLoading{ponto}\r")
        sys.stdout.flush()
        sleep(0.25)

def FilePath():
    global file_path
    file_path = str(input("\nDiretório de Download: "))
    home = os.getenv("HOME") + "/"
    dir_default_download = home + "/Downloads/yt-dwl"
    directorys = file_path.split("/")

    if "~" in directorys:
        directorys = directorys[1:len(directorys)]
        strDire = "/".join(directorys)
        file_path = home + strDire

    if len(file_path) == 0:    
        if not os.path.exists(dir_default_download):
            os.makedirs(dir_default_download)

        file_path = dir_default_download
        print(f"\n\033[1;33m[WARNING] \033[1;37mDiretório de Download Definido Para: {file_path} ")

    if os.path.isdir(file_path) == False:
        print("\nDiretório inexistente\n")
        FilePath()   

def SetVideo():
    url = str(input("\nLink do vídeo: "))

    try:
        global video
        video = YouTube(url, on_progress_callback=BarDownloadProgress)
    except exceptions.RegexMatchError:
        print("\n\033[1;31m[ERROR]\033[1;37m link inválido")
    except exceptions.VideoUnavailable: 
        print("\n\033[1;31m[ERROR]\033[1;37m Video indisponível") 

    titulo = video.title 
    lTitulo = []

    for c in range(0, len(titulo.split())):
        lTitulo.append(titulo.split()[c].capitalize())
    titulo = " ".join(lTitulo)
    
    return titulo

def GetVideo(titulo):
    global stream
    stream = video.streams.get_highest_resolution()
    print("\n\033[1;33m[WARNING] \033[1;37mBaixando o vídeo na melhor resolução\n")
    Download(file_path, titulo, ".mp4")

def GetAudio(titulo):
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

def Download(dir_path, titulo, extension):
    file = titulo+extension
    file_path = f"{dir_path}/{file}"
    file_upper = titulo.upper()+extension
    file_path_upper = f"{dir_path}/{file_upper}"

    while os.path.exists(file_path):
        print("\n\033[1;31m[ERROR]\033[1;37m Nome de arquivo já existente nesse diretório\n")
        titulo = str(input("Nome do arquivo: "))
        file = titulo+extension
        file_path = f"{dir_path}/{file}"

    print(f"\nDownloading: {file}")
    stream.download(dir_path, file_upper)
    print(f"\n\n\033[1;32mDownload Concluido => {file_path}\033[1;37m\n")

    if extension == ".mp3":
        print(f"\nConvertendo: {titulo}")
        os.system(f"ffmpeg -i '{file_path_upper}' -vn -ar 44100 -ac 2 -b:a 192k '{file_path}'")
        os.system(f"rm '{file_path_upper}'")
        print(f"\n\033[1;32mConversão Concluida => {file_path}\033[1;37m\n")