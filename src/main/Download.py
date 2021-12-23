#! /usr/bin/env python3

import sys
import os
from pytube import YouTube
from pytube import exceptions

def SetVideo():
    url = str(input("\nLink do vídeo: "))

    try:
        global video
        video = YouTube(url, on_progress_callback=BarDownloadProgress)
    except exceptions.RegexMatchError:
        print("\n\033[1;31m[ERROR]\033[1;37m link inválido")
        exit()
    except exceptions.VideoUnavailable: 
        print("\n\033[1;31m[ERROR]\033[1;37m Video indisponível") 
        exit()

    titulo = video.title 
    titulo_split = titulo.split()
    lTitulo = []

    for c in range(len(titulo_split)):
        letras = list(titulo_split[c])
        for d in range(len(letras)):
            if letras[d] == "/" or letras[d] == "'/'":
                pass
            else:
                lTitulo.append(letras[d])
        lTitulo.append(" ")

    titulo = "".join(lTitulo)
    titulo = titulo.rstrip()
    
    return titulo

def BarDownloadProgress(chunk, file_handle, bytes_remaining):
    filesize = stream.filesize
    current = ((filesize - bytes_remaining)/filesize)
    percent = ('{0:.1f}').format(current*100)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    sys.stdout.write('↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
    sys.stdout.flush()

def DownloadVideo(dir_path, titulo):
    file_path = f"{dir_path}/{titulo+'.mp4'}"

    while os.path.exists(file_path):
        print("\n\033[1;31m[ERROR]\033[1;37m Nome de arquivo já existente nesse diretório\n")
        titulo = str(input("Nome do arquivo: "))
        file_path = f"{dir_path}/{titulo+'.mp4'}"

    print("\n\033[1;33m[WARNING] \033[1;37mBaixando o vídeo na melhor resolução\n")

    print(f"Downloading: {titulo}")
    global stream
    stream = video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").first()
    stream.download(dir_path)
    print(f"\n\n\033[1;32mDownload Concluido => {file_path}\033[1;37m\n")

def DownloadAudio(dir_path, titulo):
    file_path = f"{dir_path}/{titulo+'.mp3'}"
    file_path_orig = f"{dir_path}/{titulo}"

    while os.path.exists(file_path):
        print("\n\033[1;31m[ERROR]\033[1;37m Nome de arquivo já existente nesse diretório, defina outro nome\n")
        titulo = str(input("Nome do arquivo: "))
        file_path = f"{dir_path}/{titulo+'.mp3'}"
        file_path_orig = f"{dir_path}/{titulo}"

    print(f"Downloading: {titulo}")
    global stream
    stream = video.streams.filter(only_audio=True).first()
    stream.download(dir_path, titulo)
    print(f"\n\n\033[1;32mDownload Concluido => {file_path}\033[1;37m\n")

    print(f"\nConvertendo: {titulo}")
    os.system(f"ffmpeg -i '{file_path_orig}' -vn -ar 44100 -ac 2 -b:a 192k '{file_path}'")
    os.system(f"rm '{file_path_orig}'")
    print(f"\n\033[1;32mConversão Concluida => {file_path}\033[1;37m\n")
