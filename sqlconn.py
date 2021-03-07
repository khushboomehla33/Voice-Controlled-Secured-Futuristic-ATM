import sqlite3

def dbconnect():
    con=sqlite3.connect("atm.db")
def create_utable():
    con=sqlite3.connect("atm.db")
    con.execute('''CREATE TABLE USERS(ID INT PRIMARY KEY NOT NULL,
                    NAME TEXT NOT NULL,
                    BALANCE INT NOT NULL,
                    PIN INT NOT NULL,
                    EMAIL TEXT);''')
def adduser(uid,nm,bln,pin,email):
    con=sqlite3.connect("atm.db")
    con.execute("INSERT INTO USERS(ID,NAME,BALANCE,PIN,EMAIL) VALUES(?,?,?,?,?)",[uid,nm,bln,pin,email])
    con.commit()

def pinchange(uid,pn):
    con=sqlite3.connect("atm.db")
    con.execute("UPDATE USERS SET PIN=? WHERE ID= ?",[pn,uid])
    con.commit()

def check_user(uid,pin):
    con1=sqlite3.connect("atm.db")
    cursor = con1.execute("SELECT ID,NAME FROM USERS WHERE ID=? AND PIN=?",[uid,pin])
    data = cursor.fetchone()
    if data is None:
        return False
    else:
        return True

def check_email(email):
    con1=sqlite3.connect("atm.db")
    cursor = con1.execute("SELECT EMAIL FROM USERS WHERE EMAIL=?",[email])
    data = cursor.fetchone()
    if data is None:
        return False
    else:
        return True



def get_user(uid):
    con1=sqlite3.connect("atm.db")
    cursor = con1.execute("SELECT ID,NAME,BALANCE FROM USERS WHERE ID=?",[uid])
    return cursor.fetchone()

def get_useremail(em):
    con=sqlite3.connect("atm.db")
    cursor = con1.execute("SELECT ID FROM USERS WHERE EMAIL=?",[em])
    return cursor.fetchone()

def show_balance(uid):
    con1=sqlite3.connect("atm.db")
    cursor = con1.execute("SELECT BALANCE FROM USERS WHERE ID=?",[uid])
    return cursor.fetchone()

def add_balance(uid,amount):
    
    con=sqlite3.connect("atm.db")
    c=show_balance(uid)
    balance=c[0]+ amount
    con.execute("UPDATE USERS SET BALANCE=? WHERE ID=?",[balance,uid])
    con.commit()
    
def remove_balance(uid,amount):
    con=sqlite3.connect("atm.db")
    c=show_balance(uid)
    balance=c[0]-amount
    con.execute("UPDATE USERS SET BALANCE=? WHERE ID=?",[balance,uid])
    con.commit()
    c1=show_balance(uid)
    return c1
