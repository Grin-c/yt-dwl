from Download import Loading
from Download import FilePath
from Download import SetVideo
from Download import GetVideo
from Download import GetAudio

Loading()

print('''Download Options

[0] => Video
[1] => Áudio
''')
option = int(input("Download Option: "))

if option < 0 or option > 1:
    print("\nNúmero inválido tente novamente\n")
    DownloadOption()

FilePath()

if option == 0:
    while True:
        GetVideo(SetVideo())
else:
    while True:
        GetAudio(SetVideo())
