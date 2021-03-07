from tkinter import *
import utils
import withdraw
import deposit
import benquiry
import pchange
import uid as mainpage
import threading
import gc
import speech_recognition as sr
from pygame import*
  

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer() 
device_id =1


operator=""
txt =""
result=0


def main():
    global operator;
    operator=""
    global txt
    txt=""
    global result
    result=0
    root=Tk()
    root.title("menu")
    root.configure(background='LIGHT GREY')
    mixer.init()
    mixer.music.load('audio\\choice.mp3')
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
                text.lower()
                if(len(text)!=0):
                    if(text=="withdrawal"):
                        txt="0"
                        result=1
                    elif(text=="withdraw"):
                        txt="0"
                        result=1
                    elif(text=="deposit"):
                        txt="2"
                        result=1
                    elif(text=="balance"):
                        txt="1"
                        result=1
                    elif(text=="balanceenquiry"):
                        txt="1"
                        result=1
                    elif(text=="pinchange"):
                        txt="3"
                        result=1
                    else:
                        print("no")
                    
                              
            except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 
                              
            except sr.RequestError as e: 
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
    

    def listen_for_result():
        '''
        Check if there is something in the queue
        '''
        if(result==1):
            sub(int(txt))
        elif(result==2):
            print("exit")
        else:
            root.after(100, listen_for_result)
    
    new_thread = threading.Thread(
            target=listen,
            args=(),
            kwargs={})
    new_thread.start()
    root.after(1000, listen_for_result)
    

    
    full=Frame(root,width=1200, height=600,bg='lightskyblue')
    def gomain():
        root.destroy()
        root.quit()
        gc.collect()
        mainpage.main()
        
    def sub(q):
        if(q==0):
            root.destroy()
            withdraw.main()
        elif (q==1):
            root.destroy()
            benquiry.main()
        elif (q==2):
            root.destroy()
            deposit.main()
        elif (q==3):
            root.destroy()
            pchange.main()
        else:
            gomain()
            
    heading=Label(full,font=('Kacst Screen',40,'bold'),text="CHOOSE ONE",anchor='w',fg='Black',bg='lightskyblue')
    heading.place(x=400,y=15)
    submit1=Button(full,font=('arial',16,'bold'),text="WITHDRAW",fg='black',bg='light green',command=lambda: sub(0),relief='raise',bd=5)
    submit1.place(x=200,y=150)
    submit1.config(height=2,width=20)
    submit2=Button(full,font=('arial',16,'bold'),text="BALANCE ENQUIRY",fg='black',bg='light green',command=lambda: sub(1),relief='raise',bd=5)
    submit2.place(x=200,y=300)
    submit2.config(height=2,width=20)
    submit3=Button(full,font=('arial',16,'bold'),text="DEPOSIT",fg='black',bg='light green',command=lambda: sub(2),relief='raise',bd=5)
    submit3.place(x=700,y=150)
    submit3.config(height=2,width=20)
    submit4=Button(full,font=('arial',16,'bold'),text="PIN CHANGE",fg='black',bg='light green',command=lambda: sub(3),relief='raise',bd=5)
    submit4.place(x=700,y=300)
    submit4.config(height=2,width=20)
    submit5=Button(full,font=('arial',16,'bold'),text="EXIT",fg='black',bg='red',command=lambda: gomain(),relief='raise',bd=5)
    submit5.place(x=455,y=450)
    submit5.config(height=2,width=20)
    full.place(x=165,y=95)

    root.geometry("1900x1060+0+0")
    root.mainloop()
