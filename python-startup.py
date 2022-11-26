# You are probably trying to cheat at the game or pirate it.
#If you are pirating this game. Well, it's already free.
#You might even be trying to just find out how this game was coded.
#Just go to the github page at: https://github.com/exotic-pineapple/Zerum.git 

# Importations
from tkinter import *
from time import time

#Functions

def RBF():
    OBP=1
    OKButton.pack_forget()

def RBF1():
    OKButton.pack_forget()
    CILN.pack_forget()
    WelcomeText1.pack_forget()
    OBP = 0
    CILNF()
    
def CILNF():
    CILN.pack_forget()
    WelcomeText1.pack_forget()
    ThatWVN.pack()
    if OBP == 1:
        Btn001.pack()
    elif OBP == 0:
        Btn002.pack()
    
    

def AL():
    LText.pack_forget()
    root.title('Zerum')
    WelcomeText1.pack()
    OKButton.pack()
    CILN.pack()
    
def IDC():
    ThatWVN.pack_forget()
    BATWVN.pack_forget()
    IDCT.pack()
    SM.pack()

def MQF():
    IDCT.pack_forget()
    SM.pack_forget()
    ELT.pack()
    CEB.pack()
    
def game():
    ELT.pack_forget()
    CEB.pack_forget()
    
# Variables
root = Tk()
app = root
LText = Label(app, text='Loading... (Please Wait)')
WelcomeText1 = Label(root, text='Hello! Welcome to Zerum!')
OBP = 1
OKButton = Button(app, text="OK.", command=RBF)
CILN = Button(app, text="Can I leave now?", command=RBF1)
ThatWVN = Label(app, text="That wasn't very nice!")
Btn001 = Button(app, text="But the OK. button disappeared after I clicked it! And this was the only one now!", command=IDC)
Btn002 = Button(app, text="This game is boring bro. I really don't care about it.", command=IDC)
IDCT = Label(app, text="I DON\'T CARE! YOU WILL PAY FOR THIS!")
SM = Button(app, text="Please. Spare me!", command=MQF)
ELT = Label(app, text="ONLY if you win against me in a game. >:)")
CEB = Button(app, text="Challenge excepted!", command=game)


#app.iconbitmap('C:\Users\---------\Desktop\-------\Resources\Icon.bmp')
root.title('Zerum (Loading...)')
app.geometry('500x300')
LText.pack()
root.after(5000, AL)



root.mainloop()
