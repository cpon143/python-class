# import tkinter
# from tkinter import *

# top = Tk()

# top.geometry("800x900")
# c= Canvas(top,bg="green",width="1366",height="768")
# arc=c.create_arc((500,0,150,200),start=0,extent=250,fill="red")


#---------------------------------------------------------------------------------------

# c.pack()
# top.mainloop()

# from tkinter import *
# top=Tk()
# top.geometry("200x200")
# checkyar1=IntVar()
# checkyar2=IntVar()
# checkyar2=IntVar()

# checkbtn1=Checkbutton(top,text="C",variable="checkver1",onvalue=1,offvalue=0,height=2,width=10)
# checkbtn2=Checkbutton(top,text="C",variable="checkver1",onvalue=1,offvalue=0,height=2,width=10)
# checkbtn3=Checkbutton(top,text="C",variable="checkver1",onvalue=1,offvalue=0,height=2,width=10)

# checkbtn1.pack()
# checkbtn2.pack()
# checkbtn3.pack()
# top.mainloop()

#-------------------------------------------------------------------------------------------


# import tkinter
# from tkinter import *
# top=Tk()
# top.geometry("200x300")
# lbl=Label(top,text="Top four countries in the world")
# listbox=Listbox(top)
# listbox.insert(1,"India")
# listbox.insert(2,"America")
# listbox.insert(3,"Austrila")
# listbox.insert(4,"Japan")
# btn=Button(top,text="delete",command=lambda listbox = listbox.delete(ANCHOR))

# btn.pack()
# lbl.pack()
# listbox.pack()
# top.mainloop()


#-------------------------------------------------------------------------------------------------

# import tkinter
# from tkinter import *
# top=Tk()
# def hello():
#     print("hello")
    
# #create a top level menu
# menubar=Menu(top)
# menubar.add_command(label="Hello!",command=hello)
# menubar.add_command(label="Quit!",command=top.destroy)

# #display the menu
# top.config(menu=menubar)

# top.mainloop()

#---------------------------------------------------------------------------------------------------------

# import tkinter
from tkinter import Toplevel,Button,Tk,Menu
top=Tk()
menubar=Menu(top)
file=Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save as")
file.add_command(label="Close")

file.add_command(label="Exit",command=top.destroy)
file.add_separator()
menubar.add_cascade(label="File",menu=file)

edit=Menu(menubar,tearoff=1)
edit.add_command(label="Undo ????????")
edit.add_command(label="Cut ???")
edit.add_command(label="Copy ????")
edit.add_command(label="Paste ????")
edit.add_command(label="Delete ???")
edit.add_command(label="SelectAll ????")

edit.add_separator()

menubar.add_cascade(label="Edit",menu=edit)
help=Menu(menubar,tearoff=2)
help.add_command(label="About")

menubar.add_cascade(label="Help",menu=help)

top.config(menu=menubar)
top.mainloop()