#! /usr/bin/env python3

import sys
from time import sleep

from Download import SetVideo
from Download import DownloadVideo
from Download import DownloadAudio
from DirPath import DirPath

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
option = int(input("Download Option: "))

# Verificando se a opção é valida
if option < 0 or option > 1:
    print("\nNúmero inválido tente novamente\n")
    DownloadOption()

# Definindo diretório
dir_path = DirPath().SetDir()

# Baixando o formato do vídeo de acordo com a opção
if option == 0:
    while True:
        DownloadVideo(dir_path, SetVideo())
else:
    while True:
        DownloadAudio(dir_path, SetVideo())
