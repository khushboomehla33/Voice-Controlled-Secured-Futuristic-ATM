from tkinter import *
import uid as mainpage

operator=""
from pygame import*

def main(success):
    root=Tk()
    root.title("ATM")
    #root.configure(background='blue')

    mixer.init()
    mixer.music.load('audio\\sucessfull.mp3')
    mixer.music.play()
    full=Frame(root,width=1200, height=600,bg='lightskyblue')
    thank = "Thank YOU , for the transaction!!"
    thank=Label(full,font=('Kacst Screen',40,'bold'),text=thank,anchor='w',fg='black',bg='lightskyblue')
    thank.place(x=170,y=15)

    heading=Label(full,font=('Kacst Screen',32,'bold'),text=success,anchor='w',fg='black',bg='lightskyblue')
    heading.place(x=85,y=80)
    def gomain():
        root.destroy()
        root.quit()
        mainpage.main()
    def sub():
        root.destroy()
        quit()
    submit=Button(full,font=('arial',20,'bold'),text="EXIT",fg='black',bg='red',command=gomain,relief='raise',bd=5)
    submit.place(x=550,y=200)
    full.place(x=165,y=95)
    root.geometry("1900x1060+0+0")
    root.mainloop()
