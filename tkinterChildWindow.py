# from tkinter import *
# root=Tk()
# root.geometry("200x200")
# def open():
#     top= Toplevel(root)
#     top.mainloop()
# btn=Button(root,text="click me plz", command=open)

# btn.place(x=75,y=50)

# root,mainloop()

# ---------------------------------------------------


from tkinter import *
def add():
    a=int(e1.get())
    b=int(e2.get())
    leftdata=str(1,a+b)

w1=PanedWindow()
w1.pack(fill=BOTH,expand=1)

left=Entry(w1,bd=5)
w1.add(left)

w2=PanedWindow(w1,orient=VERTICAL)
w1.add(w2)
    
e1=Entry(w2)
e2=Entry(w2)

w2.add(e1)
w2.add(e2)

bottom=Button(w2,text="add",command=add)
w2.add(bottom)
mainloop()