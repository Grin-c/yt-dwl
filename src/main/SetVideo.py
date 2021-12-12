from pytube import YouTube
from pytube import exceptions


def SetUrl():
    url = str(input("Link do Vídeo"))
    return url

class PickVideo:
    def __init__(self):
        self.url = url
        try:
            self.video = YouTube(self.url, on_progress_callback=BarDownloadProgress)
        except exceptions.RegexMatchError:
            print("\n\033[1;31m[ERROR]\033[1;37m link inválido")
            SetUrl()
        except exceptions.VideoUnavailable:
            print("\n\033[1;31m[ERROR]\033[1;37m Video indisponível") 
            SetUrl()
        self.stream = None
        self.video_titulo = self.video.title.split()
        self.lTitulo = []
    
    def CapitalizeTitulo(self):
        for c in range(0,len(self.video_titulo)):
            self.lTitulo.append(self.video_titulo[c].capitalize())

        self.video_titulo = " ".join(self.lTitulo)
        return self.video_titulo

    def GetVideo(self):
        self.stream = self.video.streams.get_highest_resolution()
        print("\n\033[1;33m[WARNING] \033[1;37mBaixando o vídeo na melhor resolução\n")

    def GetAudio(self):
        self.stream = self.video.streams.get_audio_only()