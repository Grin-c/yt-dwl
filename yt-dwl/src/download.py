#! /usr/bin/env python3

import sys
import os
from pytube import YouTube
from pytube import exceptions

class Download:
    def __init__(self, url, dir_path):
        self.url = url
        self.dir_path = dir_path

    def BarDownloadProgress(self, chunk, file_handle, bytes_remaining):
        filesize = self.stream.filesize
        current = ((filesize - bytes_remaining) / filesize)
        percent = ('{0:.1f}').format(current * 100)
        progress = int(50 * current)
        status = '█' * progress + '-' * (50 - progress)
        sys.stdout.write('↳ |{bar}| {percent}%\r'.format(bar=status, percent=percent))
        sys.stdout.flush()

    def SetVideo(self):
        try:
            self.video = YouTube(self.url, on_progress_callback=self.BarDownloadProgress)
        except exceptions.RegexMatchError:
            print("\n\033[1;31m[ERROR]\033[1;37m Invalid link")
            exit()
        except exceptions.VideoUnavailable:
            print("\n\033[1;31m[ERROR]\033[1;37m Video unavailable")
            exit()

        # Dormatting the title
        self.titulo = self.video.title
        self.titulo_split = self.titulo.split()
        self.lTitulo = []

        for c in range(len(self.titulo_split)):
            self.letters = list(self.titulo_split[c])
            for d in range(len(self.letters)):
                if self.letters[d] == "/" or self.letters[d] == "'/'" or self.letters[d] == '"' or self.letters[d] == "'":
                    pass
                else:
                    self.lTitulo.append(self.letters[d])
            self.lTitulo.append(" ")

        self.titulo = "".join(self.lTitulo)
        self.titulo = self.titulo.rstrip()

    def DownloadVideo(self):
        self.file_path = f"{self.dir_path}/{self.titulo + '.mp4'}"

        # Checking if the file exists
        if os.path.exists(self.file_path):
            opt = str(input("\n\033[1;33m[WARNING]\033[1;37m File already existing in that directory, replace? [Y/N] ")).upper()
            if opt == "N":
                print("\n\033[1;33m[WARNING]\033[1;37m Download canceled\n")
                return
            elif opt == "Y":
                os.system(f"rm '{self.file_path}'")
            else:
                print("\n\033[1;31m[ERROR] Invalid option\033[1;37m")
                return

        print("\n\033[1;33m[WARNING]\033[1;37m Downloading the video in the best resolution\n")

        print(f"Downloading: {self.titulo}")
        self.stream = self.video.streams.filter(progressive=True, file_extension="mp4").order_by("resolution").first()
        self.stream.download(self.dir_path)
        print(f"\n\n\033[1;32mDownload completed => {self.file_path}\033[1;37m\n")

    def DownloadAudio(self):
        self.file_path = f"{self.dir_path}/{self.titulo + '.mp3'}"
        self.file_path_orig = f"{self.dir_path}/{self.titulo}"

        # Checking if the file exists
        if os.path.exists(self.file_path):
            opt = str(input("\n\033[1;33m[WARNING]\033[1;37m File already existing in that directory, replace? [Y/N] ")).upper()
            if opt == "N":
                print("\n\033[1;33m[WARNING]\033[1;37m Download canceled\n")
                return
            elif opt == "Y":
                os.system(f"rm '{self.file_path}'")
            else:
                print("\n\033[1;31m[ERROR] Invalid option\033[1;37m")
                return

        print(f"Downloading: {self.titulo}")
        self.stream = self.video.streams.filter(only_audio=True).first()
        self.stream.download(self.dir_path, self.titulo)
        print(f"\n\n\033[1;32mDownload completed => {self.file_path_orig}\033[1;37m\n")

        print(f"\nConverting: {self.titulo}")
        os.system(f"ffmpeg -i '{self.file_path_orig}' -vn -ar 44100 -ac 2 -b:a 192k '{self.file_path}'")
        os.system(f"rm '{self.file_path_orig}'")
        print(f"\n\033[1;32mConversion completed => {self.file_path}\033[1;37m\n")
