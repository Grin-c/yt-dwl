#! /usr/bin/env python3

import sys
import os

from pytube import YouTube
from pytube import exceptions

from SetVideo import PickVideo


def BarDownloadProgress(chunk, file_handle, bytes_remaining):
        filesize = stream.filesize
        current = ((filesize - bytes_remaining)/filesize)
        percent = ('{0:.1f}').format(current*100)
        progress = int(50*current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write('↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()

def SetUrl():
        global url
        url = str(input("\nLink do Vídeo: "))
        return url

class Download:
    def __init__(self, dir_path, extension):
        try:
            self.video = YouTube(url, on_progress_callback=BarDownloadProgress)
        except exceptions.RegexMatchError:
            print("\n\033[1;31m[ERROR]\033[1;37m Erro no Link")
        except exceptions.VideoUnavailable:
            print("\n\033[1;31m[ERROR]\033[1;37m Video indisponível") 
        self.video_titulo = self.video.title 
        self.extension = extension
        self.dir_path = dir_path
        self.file = self.video_titulo + self.extension
        self.file_path = f"{self.dir_path}/{self.file}"
        self.file_upper = self.video_titulo.upper() + self.extension
        self.file_path_upper = f"{self.dir_path}/{self.file_upper}"
        self.lTitulo = []

    def ManageName(self):
        for c in range(0,len(self.video_titulo.split())):
            self.lTitulo.append(self.video_titulo[c].capitalize())
        self.video_titulo = " ".join(self.lTitulo)

        while os.path.exists(self.file_path):
            print("\n\033[1;31m[ERROR]\033[1;37m Nome de arquivo já existente nesse diretório, mude o nome dele\n")
            self.video_titulo = str(input("Nome do arquivo: "))
            self.file = self.video_titulo+self.extension_param
            self.file_path = f"{self.dir_path_param}/{self.file}"

    def DownloadVideo(self):
        global stream
        stream = self.video.streams.get_highest_resolution()
        print("\n\033[1;33m[WARNING] \033[1;37mBaixando o vídeo na melhor resolução\n")
        print(f"\nDownloading: {self.video_titulo}")
        stream.download(self.dir_path, self.file)
        print(f"\n\n\033[1;32mDownload Concluido => {self.file_path}\033[1;37m\n")

    def DownloadAudio(self):
        global stream
        stream = self.video.streams.get_highest_resolution()
        print("\n\033[1;33m[WARNING] \033[1;37mBaixando o vídeo na melhor resolução\n")
        print(f"\nDownloading: {self.video_titulo}")
        stream.download(self.dir_path, self.file_upper)
        print(f"\n\n\033[1;32mDownload Concluido => {self.file_path}\033[1;37m\n")

        print(f"\nConvertendo: {self.video_titulo}")
        os.system(f"ffmpeg -i '{self.file_path_upper}' -vn -ar 44100 -ac 2 -b:a 192k '{self.file_path}'")
        os.system(f"rm '{self.file_path_upper}'")
        print(f"\n\033[1;32mConversão Concluida => {self.file_path}\033[1;37m\n")
