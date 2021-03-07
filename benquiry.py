from tkinter import *
import utils
import uid as mainpage

operator=""

def main():
    root=Tk()
    root.title("ATM")
    #root.configure(background='blue')
    full=Frame(root,width=1200, height=600,bg='lightskyblue')
    
    def gomain():
        root.destroy()
        mainpage.main()
    bal = "Your current Available balance is :"+ str(utils.getbalance())
    heading=Label(full,font=('Kacst Screen',40,'bold'),text=bal,anchor='w',fg='black',bg='lightskyblue')
    heading.place(x=100,y=15)
    def sub():
        root.destroy()
        quit()
    submit=Button(full,font=('arial',20,'bold'),text="EXIT",fg='black',bg='red',command=gomain,relief='raise',bd=5)
    submit.place(x=532,y=220)

    full.place(x=165,y=95)

    root.geometry("1900x1060+0+0")
    root.mainloop()
