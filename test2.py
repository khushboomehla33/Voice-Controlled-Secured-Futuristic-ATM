#Python 2.x program for Speech Recognition 
  
import speech_recognition as sr 
  

sample_rate = 48000
chunk_size = 2048
r = sr.Recognizer() 
device_id =1

def wrapper():
    txt =""
    def listen():
        with sr.Microphone(device_index = device_id, sample_rate = sample_rate,  
                                chunk_size = chunk_size) as source:
            r.adjust_for_ambient_noise(source) 
            print("Say Something")
            audio = r.listen(source) 
                  
            try: 
                text = r.recognize_google(audio) 
                txt=text
              
            except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio") 
              
            except sr.RequestError as e: 
                print("Could not request results from Google Speech Recognition service; {0}".format(e)) 
    def on_done():
        return txt
