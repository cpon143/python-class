from tkinter import *
from turtle import right
top=Tk()
# sq lite make a data base for own
top.geometry("140x100")
frame=Frame(top)
frame.pack

leftframe=Frame(top)
leftframe.pack(side=LEFT)

rightframe=Frame(top)
rightframe.pack(side=RIGHT)

btn1=Button(frame,text="submit",fg="red",activebackground="red")
btn1.pack(side=LEFT)
btn2=Button(frame,text="remove",fg="brown",activebackground="brown")
btn2.pack(side=RIGHT)
btn3=Button(rightframe,text="add",fg="blue",activebackground="blue")
btn3.pack(side=LEFT)
btn4=Button(leftframe,text="modify",fg="black",activebackground="white")
btn4.pack(side=right)
top.mainloop()

