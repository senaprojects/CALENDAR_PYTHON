import calendar
from tkinter import *
root=Tk()
root.title("CALENDAR")
root.geometry("300x300")
root.configure(bg='black')
def show():
    a=int(spin1.get())
    b=int(spin2.get())
    cal=calendar.month(b,a)
    txt.delete(0.0,END)
    txt.insert(INSERT,cal)
lbl1=Label(root,text="Month",font=("times","12","bold")).place(x=32,y=20)
lbl2=Label(root,text="Year",font=("times","12","bold")).place(x=159,y=20)
spin1=Spinbox(root,values=(1,2,3,4,5,6,7,8,9,10,11,12),width=6)
spin1.place(x=85,y=20)
spin2=Spinbox(root,from_=1999,to_=2100,width=10)
spin2.place(x=200,y=20)
btn=Button(root,text="show",font=("times","12","bold"),width=6,command=show).place(x=100,y=60)
txt=Text(root,width=24,height=8)
txt.place(x=50,y=100)
root.mainloop()


