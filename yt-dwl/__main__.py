#! /usr/bin/env python3

import sys
from time import sleep
from src.main.Download import Download
from src.main.DirPath import DirPath

try: 
    # Animação de Loading
    for c in range(1,4):
            ponto = "." * c
            sys.stdout.write(f"\033[1;37mLoading{ponto}\r")
            sys.stdout.flush()
            sleep(0.25)

    print('''Download Options

    [0] => Video
    [1] => Áudio
    ''')
    opt = int(input("Download Option: "))

    # Verificando se a opção é valida
    if opt < 0 or opt > 1:
        print("\n\033[1;31m[ERROR]\033[1;37m Número inválido\n")
        exit()

    # Definindo diretório
    dir_path = DirPath().SetDir()

    # Baixando o formato do vídeo de acordo com a opção
    while True:
        url = str(input("\nURL do vídeo: "))
        download = Download(url, dir_path)
        download.SetVideo()

        if opt == 0:
            download.DownloadVideo()
        else:
            download.DownloadAudio()
except KeyboardInterrupt:
    exit(print())