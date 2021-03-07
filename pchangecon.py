from tkinter import *
import utils
import uid as mainpage
import tcancel as tc
import threading
import gc
import speech_recognition as sr
  

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer() 
device_id =1


operator=""
txt =""
result=0
from pygame import*

def main():
    global operator
    operator=""
    global txt
    txt=""
    global result
    result=0
    root=Tk()
    root.title("ATM")
    root.configure(background='blue')

    mixer.init()
    mixer.music.load('audio\\new.mp3')
    mixer.music.play()
    def listen():
        global result
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate, chunk_size = chunk_size) as source:
            r.adjust_for_ambient_noise(source) 
            print("Say Something")
            audio = r.listen(source)                 
            try:
                global txt
                text = r.recognize_google(audio)
                text.replace(" ", "")
                t=utils.only_digits(text)
                if(len(t)!=0):
                    txt=t
                    result=1
                    
                              
            except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 
                              
            except sr.RequestError as e: 
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    

    def listen_for_result():
        '''
        Check if there is something in the queue
        '''
        if(result==1):
            txtDisplay.delete(0,END)
            txtDisplay.insert(0,txt)
            sub()
        else:
            root.after(100, listen_for_result)
    
    new_thread = threading.Thread(
            target=listen,
            args=(),
            kwargs={})
    new_thread.start()
    root.after(1000, listen_for_result)
    

    full=Frame(root,width=1350, height=760,bg='lightskyblue')

    heading=Label(full,font=('Kacst Screen',48,'bold'),text="PIN CHANGE.",anchor='w',fg='red',bg='blue')
    heading.place(x=30,y=15)
    uid=Label(full,font=('arial',20,'bold'),text="NEW PIN:",anchor='w',fg='white',bg='blue')
    uid.place(x=300,y=130)

    def sub():
        npin= str(text_Input.get())
        if(utils.changepin(npin)):
            root.destroy()
            mainpage.main()
        else:
            root.destroy()
            tc.main("could not change pin")

    #------------------------calculator-------------------------------------------------------------------------------------
    calculator=Frame(full)
    calculator.place(x=450,y=100)

    def btnClick(numbers):
        global operator
        operator = operator +str(numbers)
        text_Input.set(operator)
    def btnClearDisplay():
        global operator
        operator=""
        text_Input.set("")

    def gomain():
        root.destroy()
        root.quit()
        mainpage.main()
        
    text_Input=StringVar()
    txtDisplay=Entry(calculator,font=('arial',17,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg='white',justify='center')
    txtDisplay.grid(columnspan=4)
    #-------------------------------------------------------------------------------------------------------------
    btn1=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="1",bg="powder blue",
                command=lambda: btnClick(1)).grid(row=2,column=0)
    btn2=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="2",bg="powder blue",
                command=lambda: btnClick(2)).grid(row=2,column=1)
    btn3=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="3",bg="powder blue",
                command=lambda: btnClick(3)).grid(row=2,column=2)
    clr=Button(calculator,padx=18,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="CLR",bg="yellow",
                command=btnClearDisplay).grid(row=2,column=3)
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    btn4=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="4",bg="powder blue",
                command=lambda: btnClick(4)).grid(row=3,column=0)
    btn5=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="5",bg="powder blue",
                command=lambda: btnClick(5)).grid(row=3,column=1)
    btn6=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="6",bg="powder blue",
                command=lambda: btnClick(6)).grid(row=3,column=2)
    btn6=Button(calculator,padx=33,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="0",bg="powder blue",
                command=lambda: btnClick(0)).grid(row=3,column=3)
    #------------------------------------------------------------------------------------------------------------------------------------------------------
    btn7=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="7",bg="powder blue",
                command=lambda: btnClick(7)).grid(row=4,column=0)
    btn8=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="8",bg="powder blue",
                command=lambda: btnClick(8)).grid(row=4,column=1)
    btn9=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="9",bg="powder blue",
                command=lambda: btnClick(9)).grid(row=4,column=2)
    ex=Button(calculator,padx=16,pady=16,bd=5,fg='black',font=('arial',16,'bold'),text="EXIT",bg="red",
                command=lambda: gomain()).grid(row=4,column=3)
    #------------------------------------------------------------------------------------------------------------------------------------------------------

    submit=Button(full,font=('arial',20,'bold'),text="SUBMIT",fg='black',bg='light green',command=sub,relief='raise',bd=5)
    submit.place(x=550,y=425)
    submit.config(height=1,width=7)
    full.place(x=165,y=95)

    root.geometry("1900x1060+0+0")
    root.mainloop()
