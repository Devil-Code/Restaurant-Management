from tkinter import*
import os
from tkinter import messagebox
import MySQLdb 
  
# Function for connecting to MySQL database 
def mysqlconnect(): 
    try: 
        db_connection= MySQLdb.connect ("localhost","root","root","DeliveryApp") 
    except: 
        print("Can't connect to database") 
        return 0
    print("Connected") 
    cursor=db_connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS DATA") 
    sql = """CREATE TABLE DATA (
   ITEM CHAR(10),
   QUAN CHAR(10) )"""
    print("Table Created")
    cursor.execute(sql) 
    db_connection.close()   
root=Tk()
root.geometry("500x500")
root.title("Login Page")
def Reset():
	e_login.delete(0,END) 
	e_Pass.delete(0,END)

def Reg():
	root.destroy()
	os.system('python3 register.py')

def Ref():
	if((e_login.get()=="admin")and(e_Pass.get()=="123456")):
		
		messagebox.showerror("Login","Login Successful")
		mysqlconnect()
		root.destroy()
		os.system('python3 test1.py')
		Reset()
	else:
		messagebox.showerror("Login Failed","Invalid Login or Password")
		Reset()
	
f=Frame(root)
f.pack(side=TOP,expand=TRUE,padx=5,pady=5)
l_login=Label(f,text='Login',bg='white',fg='black')
l_login.pack(side=LEFT,expand=TRUE,padx=5,pady=5)
e_login=Entry(f,text='',bg='white',fg='black')
e_login.pack(side=RIGHT,expand=TRUE,fill=BOTH,padx=5,pady=5)


f=Frame(root)
f.pack(side=TOP,expand=TRUE,padx=5,pady=5)
l_Pass=Label(f,text='Password:',bg='white',fg='black')
l_Pass.pack(side=LEFT,expand=TRUE,padx=5,pady=5)
e_Pass=Entry(f,text='',bg='white',fg='black')
e_Pass.pack(side=RIGHT,expand=TRUE,padx=5,pady=5)

f=Frame(root)
f.pack(side=TOP,expand=TRUE,padx=5,pady=5)

b_signin=Button(f,text='Sign In',command=Ref)
b_signin.pack(side=LEFT,expand=TRUE,padx=5,pady=5)

b_reset=Button(f,text='Reset',command=Reset)
b_reset.pack(side=LEFT,expand=TRUE,padx=5,pady=5)

b_register=Button(f,text='Register',command=Reg)
b_register.pack(side=LEFT,expand=TRUE,padx=5,pady=5)
root.mainloop()
