# from tkinter import *
# from turtle import right
# top=Tk()
# # sq lite make a data base for own
# top.geometry("140x100")
# frame=Frame(top)
# frame.pack

# leftframe=Frame(top)
# leftframe.pack(side=LEFT)

# rightframe=Frame(top)
# rightframe.pack(side=RIGHT)

# btn1=Button(rightframe,text="submit",fg="red",activebackground="red")
# btn1.pack(side=TOP)
# btn2=Button(leftframe,text="remove",fg="brown",activebackground="brown")
# btn2.pack(side=BOTTOM)
# btn3=Button(rightframe,text="add",fg="blue",activebackground="blue")
# btn3.pack(side=LEFT)
# btn4=Button(leftframe,text="modify",fg="black",activebackground="white")
# btn4.pack(side=RIGHT)
# top.mainloop()



# /----------------------------
from tkinter import *
def selection():
    selection="You selected the option" + str(radio.get())
    label.config(text=selection)
top=Tk()
top.geometry("300x150")
radio=IntVar()
lbl=Label(text="Favourite programming language")
lbl.pack()

R1=Radiobutton(top,text="C",variable=radio,value=1,command=selection)
R1.pack(anchor= W)

R2=Radiobutton(top,text="C++",variable=radio,value=2,command=selection)
R2.pack(anchor= W)
    
R3=Radiobutton(top,text="JAVA",variable=radio,value=3,command=selection)
R3.pack(anchor= W)

label=Label(top)
label.pack()
top.mainloop()