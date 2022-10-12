# import tkinter
# from tkinter import *
# from turtle import left
# top=Tk()
# top.title("GUI")

# b1=Button(top,text="RED", fg="red", bg="Blue")
# b1.pack(side=TOP)

# b2=Button(top,text="Blue", fg="blue", bg="yellow")
# b2.pack(side=RIGHT)

# b3=Button(top,text="Yellow", fg="yellow", bg="black")
# b3.pack(side=LEFT)

# b4=Button(top,text="ORANGE", fg="ORANGE", bg="pink")
# b4.pack(side=BOTTOM)

# top.mainloop()


# using grid() geometry
# import tkinter
# from tkinter import *
# top=Tk()
# l1=Label(top, text="Name", fg="red")
# l1.grid(row=0, column=0)

# t1=Entry(top)
# t1.grid(row=0, column=1)

# l2=Label(top, text="Password",fg="yellow")
# l2.grid(row=1,column=0)

# t2=Entry(top)
# t2.grid(row=1,column=1)

# b1=Button(top,text="SUBMIT", fg="green")
# b1.grid(row=3,column=0)

# top.mainloop()


# using place() Geometry
# import tkinter
# from tkinter import *

# top=Tk()
# l1=Label(top,text="Name")
# l1.place(x=10,y=10)

# t1=Entry(top)
# t1.place(x=80,y=10)

# l2=Label(top,text="Password")
# l2.place(x=10,y=30)

# t2=Entry(top)
# t2.place(x=80,y=35)

# top.mainloop()



import tkinter
# using some library function
from tkinter import messagebox
from tkinter import *
top=Tk()

def msg():
    messagebox.showinfo("Alert", "Button Clicked")
    b=Button(top,text="click me", activeforeground="red", activebackground="black", command=msg)
    b.pack()
    top.geometry("300x200") #for resizing the o/p window
    top.mainloop()