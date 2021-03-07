from sqlconn import *
from tkinter import *

UID=None

def changepin(npin):
    
    if(pinchange(UID,npin)):
       return True
    else:
       return False

def setuid(u):
    global UID
    UID = u

def setemail(e):
    global UID
    data = get_useremail(e)
    UID = data[0]

def set_text(e,text):
    e.delete(0,END)
    e.insert(0,text)
    return

def only_digits(x):
    return ''.join(ele for ele in x if ele.isdigit())

def checkuser(u,p):
    if(check_user(u,p)):
        return True
    else:
        return False

def checkemail(em):
    if(check_email(em)):
        return True
    else:
        return False

def getuser():
    return get_user(UID)


def authuser(u,p):
    if(checkuser(u,p)):
       setuid(u)
       return True
    else:
       return False
    
def getbalance():
    return show_balance(UID)[0]

def addbalance(amount):
    try:
        add_balance(UID,amount)
        return True
    except sqlite3.Error as er:
        return False

def removebalance(amount):
    b=getbalance()
    if(b>=amount):
        try:
            remove_balance(UID,amount)
            return 1
        except sqlite3.Error as er:
            return 0
    else:
        return -1

#dbconnect()
#create_utable()
#adduser(0,"anitik",5000,1000,"naiitk@gmail.com")
#print(checkuser(0,1000))    
#setpin(0)
"""print(UID)

setuid(0)
addbalance(2000)

if(removebalance(10000)):
    print("god")
else:
    print("not good")
print(show_balance(0)[0])
remove_balance(0,1000)"""

