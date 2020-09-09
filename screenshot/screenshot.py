# screenshot and upload to uguu.se
# oleh etooooooooooooooooooooo :)
#
# ./screenshot.py (screenshot and save image to current directory)
# ./screenshot.py -u -o (screenshot, upload, open your default browser to uguu.se)
#
# compile to exe:
# pyinstaller --onefile --noconsole --onefile screenshot.py
#

# modules
import argparse, os, getpass, requests, json, webbrowser, mss
from datetime import datetime
from sys import exit

# variables
username = getpass.getuser()
time = datetime.now()
filename = username + time.strftime("_%d%m%Y_%H%M%S") + ".jpg"

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--upload", help="upload screenshot to uguu.se", action='store_true')
parser.add_argument("-o", "--open", help="open uploaded image link in browser (depends on -u)", action='store_true')
args = parser.parse_args()

# execute code
'''
print(filename.upper())
with open(filename.lower(), 'w') as fp: 
    fp.write("[+] " + filename + " > oks")
 '''

with mss.mss() as sct:
    
    def upload_screenshot(open_link):
    
        uploadthis = {
                'files[]': (filename.lower(), open(filename.lower(), 'rb')),
                            }
                            
        response = requests.post('https://uguu.se/upload.php', files=uploadthis)
        uguu_se = json.loads(response.text)
        ugu_se_ = (uguu_se["files"][0]["url"])
        
        open_link == ""
        
        if open_link == "ok":
            webbrowser.open(ugu_se_, new = 2)
        else:
            exit
            ##print(filename.lower() + " > " + ugu_se_) 
        
    if ((args.upload == 1) and (args.open == 1)):
            
            sct.shot(mon=-1, output=filename.lower())
            upload_screenshot(open_link="ok")
            exit
    
    elif ((args.upload == 1) and (args.open == 0)):
           
            sct.shot(mon=-1, output=filename.lower())
            upload_screenshot(open_link="")
            exit
            
    elif ((args.upload == 0) and (args.open == 1)):
           
            ##print("--help for help")
            exit
            
    else:
        sct.shot(mon=-1, output=filename.lower())
        ##print(filename.lower())
        exit
