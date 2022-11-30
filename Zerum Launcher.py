#WHY YOU LOOKING? TRYING TO COPY? GO SCRUMAGE SOMEWHERE ELSE!

# Imports
from urllib.request import urlopen
import os
import subprocess
import time
from tkinter import *
import webbrowser

# Variables
pageopener = urlopen("https://pastebin.com/raw/yf9Sb24J")
update_code_page = str(pageopener.read(), 'utf-8')
tru = str("54 52 55 45")
fls = str("46 41 4c 53 45")
app = Tk()
ask = Label(app, text="There is an update. Would you like to update?")
yb = Button(app, text="Yes", command=YES)
nb = Button(app, text="No", command=NO)
directoryname = os.path.dirname(os.path.abspath(__file__))
py = os.path.join(directoryname, 'startup.py')
update = os.path.join(directoryname, 'Update.py')

# Functions
def NO():
    subprocess.call(py)

def YES():
    print("Opening website...")
    webbrowser.open('http://github.com/exotic-pineapple/Zerum', new=2)
    print("Website Opened")

def yes_update():
    print("Update Found")
    time.sleep(2)
    ask.pack()
    yb.pack()
    nb.pack()
    app.title('Update Found!')
    app.geometry('250x200')
    app.mainloop()

def no_update():
    print("No Update Found")
    time.sleep(2)
    subprocess.call(py)

# Conditions
while True:
    if fls in update_code_page:
        no_update()
    elif tru in update_code_page:
        yes_update()
    break
