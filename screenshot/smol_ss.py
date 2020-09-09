import getpass, mss, time, keyboard, os
from datetime import datetime
from os import system

system("title "+"smolscreenshot")
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

print("smolscreenshot, code available on https://github.com/etobroflovski/smol/")
print("press O and P at same time to quick screenshot\n")

def skrinsyut():
    time = datetime.now()
    filename =  desktop + time.strftime("\ss_%d%m%Y_%H%M%S") + ".jpg"
    keyboard.wait('o+p')
    with mss.mss() as sct:
        sct.shot(mon=-1, output=filename.lower())
    print("saved to " + filename.lower())
    

while True:
    skrinsyut()

