from tkinter import *
import uid as mainpage
operator=""
from pygame import*

def main(err):
    root=Tk()
    root.title("ATM")
    root.configure(background='blue')

    mixer.init()
    mixer.music.load('audio\\can.mp3')
    mixer.music.play()
    full=Frame(root,width=1200, height=600,bg='lightskyblue')
    def gomain():
        root.destroy()
        mainpage.main()

    heading=Label(full,font=('Kacst Screen',32,'bold'),text=err,anchor='w',fg='white',bg='blue')
    heading.place(x=290,y=15)
    def sub():
        root.destroy()
        quit()
    submit=Button(full,font=('arial',20,'bold'),text="EXIT",fg='black',bg='red',command=gomain,relief='raise',bd=5)
    submit.place(x=460,y=100)
    full.place(x=165,y=95)
    root.geometry("1350x760")
    root.mainloop()
