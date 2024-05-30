from tkinter import*
import random
import time
import datetime
import os
from subprocess import *
root=Tk()
root.geometry("1600x8000")
root.title("Restaurant Vadavli Tiger")
def func1():
	root.destroy()
	os.system("python3 restaurent.py")
def func2():
	root.destroy()
	os.system("python3 res1.py")
def func3():
	root.destroy()
	os.system("python3 res2.py")
def func4():
	root.destroy()

Tops=Frame(root, width=1600,relief=SUNKEN,bg='red')
Tops.pack(side=TOP)

f1=Frame(root,width=800,height=700,relief=SUNKEN,bg='red')
f1.pack()

lblInfo=Label(Tops,font=('arial',50,'bold'),text="Welcome To Vadavli Tiger Restaurent ",fg="Black",bd=10,anchor='w')
lblInfo.grid(row=0,column=0)

lblName=Label(Tops,font=('arial',25,'bold'),text="Order Food By Selecting Option",fg="Black",bd=10,anchor='w')
lblName.grid(row=4,column=0)


btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Starter",bg="powder blue",command=func1).grid(row=7,column=1)



btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Main Course",bg="powder blue",command= func2).grid(row=7,column=2)

btnExit1=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Desert",bg="powder blue",command= func3).grid(row=7,column=3)

btnExit2=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="powder blue",command=func4).grid(row=7,column=4)


root.mainloop()

