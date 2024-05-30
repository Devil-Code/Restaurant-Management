from tkinter import*
from test1 import*
root=Tk() 

root.geometry("1600x8000")
root.title("Restaurant XYZ")

def maincourse():
	items=['Veg Makhanwala','Butter Chicken','Biryani','Pasta']
	
	lblDish=Label(Tops,font=('arial',15,'bold'),text="Dish Name",fg="Black",bd=10,anchor='w')
	lblDish.grid(row=4,column=0)
	
root.mainloop()
