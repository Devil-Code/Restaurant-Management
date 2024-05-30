from tkinter import *
from tkinter import messagebox 
import os
root=Tk()
root.title('Register')
root.geometry('500x500')
gender=StringVar()
tc=IntVar()
def add():
	if((e_name.get()=='')or(e_phno.get()=='')or(e_eid.get()=='')or(gender.get()=='')or(tc.get()==0)):
		messagebox.showerror("Invalid","Form Incomplete")
		Reset()
	else:
		messagebox.showerror("Register","Register Successful")
		root.destroy()
		os.system('python3 login.py')

def Reset():
	e_name.delete(0,END) 
	e_phno.delete(0,END)
	e_eid.delete(0,END)
	gender.set("")
	tc.set(0)

l=Label(root,text='Register',bg='white',fg='black')
l.pack(side=TOP,expand=TRUE,fill=BOTH,padx=5,pady=5)

f=Frame(root)
f.pack(side=TOP,expand=TRUE,fill=BOTH,padx=5,pady=5)
l_name=Label(f,text='Name:',bg='white',fg='black')
l_name.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)
e_name=Entry(f,text='',bg='white',fg='black')
e_name.pack(side=RIGHT,expand=TRUE,fill=BOTH,padx=5,pady=5)


f=Frame(root)
f.pack(side=TOP,expand=TRUE,fill=BOTH,padx=5,pady=5)
l_phno=Label(f,text='Phone Number:',bg='white',fg='black')
l_phno.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)
e_phno=Entry(f,text='',bg='white',fg='black')
e_phno.pack(side=RIGHT,expand=TRUE,fill=BOTH,padx=5,pady=5)


f=Frame(root)
f.pack(side=TOP,expand=TRUE,fill=BOTH,padx=5,pady=5)
l_eid=Label(f,text='Email:',bg='white',fg='black')
l_eid.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)
e_eid=Entry(f,text='',bg='white',fg='black')
e_eid.pack(side=RIGHT,expand=TRUE,fill=BOTH,padx=5,pady=5)


f=Frame(root)
f.pack(side=TOP,expand=TRUE,fill=BOTH,padx=5,pady=5)
l_gen=Label(f,text='Gender:',bg='white',fg='black')
l_gen.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)
r_genm=Radiobutton(f,text='M',variable=gender,value='male')
r_genm.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)
r_genf=Radiobutton(f,text='F',variable=gender,value='female')
r_genf.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)


f=Frame(root)
f.pack(side=TOP,expand=TRUE,fill=BOTH,padx=5,pady=5)
c_tac=Checkbutton(f,text='Terms & Conditions',variable=tc)
c_tac.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)

b=Button(f,text='Submit',command=add)
b.pack(side=LEFT,expand=TRUE,fill=BOTH,padx=5,pady=5)
mainloop()

