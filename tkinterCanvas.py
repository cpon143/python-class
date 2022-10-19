# import tkinter
# from tkinter import *

# top = Tk()

# top.geometry("800x900")
# c= Canvas(top,bg="green",width="1366",height="768")
# arc=c.create_arc((500,0,150,200),start=0,extent=250,fill="red")

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

import tkinter
from tkinter import *
top=Tk()
top.geometry("200x300")
lbl=Label(top,text="Top four countries in the world")
listbox=Listbox(top)
listbox.insert(1,"India")
listbox.insert(2,"America")
listbox.insert(3,"Austrila")
listbox.insert(4,"Japan")
btn=Button(top,text="delete",command=lambda listbox = listbox.delete(ANCHOR))

btn.pack()
lbl.pack()
listbox.pack()
top.mainloop()