from tkinter import *
import utils
import emailutil
import pchangecon
import tcancel as tc
import uid as mainpage
import threading
import gc
import speech_recognition as sr
  

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer() 
device_id =1


txt =""
result=0
from pygame import*

def main():
    global txt
    txt=""
    global result
    result=0
    root=Tk()
    root.title("pin")
    #root.configure(background='blue')
    mixer.init()
    mixer.music.load('audio\\email.mp3')
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
                if(len(text)!=0):
                    txt=text
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
            emailDisplay.delete(0,END)
            emailDisplay.insert(0,txt)
        else:
            root.after(100, listen_for_result)
    
    new_thread = threading.Thread(
            target=listen,
            args=(),
            kwargs={})
    new_thread.start()
    root.after(3000, listen_for_result)

    full=Frame(root,width=1200, height=600,bg='lightskyblue')
    heading=Label(full,font=('Kacst Screen',40,'bold'),text="Enter or Speak registered email to change pin",anchor='w',fg='black',bg='lightskyblue')
    heading.place(x=10,y=15)
    def gomain():
        root.destroy()
        root.quit()
        gc.collect()
        mainpage.main()

    def sub():
        print("Submit")

    def sendemail():
        em= str(email.get())
        print(em)
        if(utils.checkemail(em)):
            emailutil.main(em)
        else:
            msg="Could not verify email. Please try again"
            root.destroy()
            tc.main(msg)

    def verifyotp():
        o = str(otp.get())
        if(o==emailutil.otp):
            root.destroy()
            pchangecon.main()
            print("verify otp function")
        else:
            msg="Wrong otp. Please try again"
            root.destroy()
            tc.main(msg)


    uid=Label(full,font=('arial',25,'bold'),text="EMAIL",anchor='w',fg='black',bg='lightskyblue')
    uid.place(x=250,y=120)
    email=StringVar()
    emailDisplay=Entry(full,font=('arial',17,'bold'),textvariable=email,bd=10,insertwidth=4,bg='white',justify='center')
    emailDisplay.place(x=440,y=120)
    send=Button(full,padx=18,bd=5,fg='black',font=('arial',16,'bold'),command=sendemail,text="Send OTP",bg="yellow")
    send.place(x=750,y=118)
    uid=Label(full,font=('arial',25,'bold'),text="OTP",anchor='w',fg='black',bg='lightskyblue')
    uid.place(x=290,y=180)
    otp=IntVar()
    otpDisplay=Entry(full,font=('arial',17,'bold'),textvariable=otp,bd=10,insertwidth=4,bg='white',justify='center')
    otpDisplay.place(x=440,y=180)
    
    

    submit=Button(full,font=('arial',20,'bold'),text="SUBMIT",fg='black',bg='light green',padx=93,command=verifyotp,relief='raise',bd=5)
    submit.place(x=420,y=250)
    full.place(x=165,y=95)
    #------------------------------------------------------------------------------------------------------------------------------------------------------



    root.geometry("1900x1060+0+0")
    root.mainloop()
