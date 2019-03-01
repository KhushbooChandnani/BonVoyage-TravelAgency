from tkinter import*
from tkinter.tix import *
from PIL import ImageTk, Image



""" root=Toplevel()
    app=FullScreenApp(root)
    f1=Frame(root,bg="white")
    f1.place(x=0,y=0,width=700,height=800)
    f2=Frame(root,bg="white")
    f2.place(x=700,y=0,width=700,height=800)
    top=Label(root,text="TAKE ONLY MEMORIES..LEAVE ONLY FOOTPRINTS!!",font=("arial",20),fg="BLACK",bg="WHITE")
    top.place(x=0,y=0,width=700,height=40)"""
def aboutbut():
    pass
    
def servicesbut():
    pass
    
def contactbut():
    r=Toplevel()
    r.geometry('2200x1000+0+0')
    r.configure(background = 'white')

    f=Frame(r)
    f.place(x=350,y=80,width=700,height=650)
    p='logo_c.png'
    i = ImageTk.PhotoImage(Image.open(p))
    pan = Label(f, image = i)
    pan.place(x=0,y=0,width=200,height=100)
    r.mainloop()
        
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
swin = ScrolledWindow(root, width=screen_width, height=5000)
swin.pack()
main = swin.window
root.minsize(width=screen_width, height=screen_height)
root.config(bg="white")

#root.attributes("-fullscreen",True)

path='res/bg.jpg'
img = ImageTk.PhotoImage(Image.open(path))
panel = Label(root, image = img)
panel.pack(expand = "yes")

remain1=Label(root,bg="black")
remain1.place(x=0,y=0,width=1400,height=50)

about=Button(root,text="About",bd=0,font=("arial",15),fg="white",bg="black",command=aboutbut)
about.place(x=50,y=0,width=150,height=50)
services=Button(root,text="Services",bd=0,font=("arial",15),fg="white",bg="black",command=servicesbut)
services.place(x=200,y=0,width=150,height=50)
contact=Button(root,text="Contact",bd=0,font=("arial",15),fg="white",bg="black",command=contactbut)
contact.place(x=350,y=0,width=150,height=50)
down=Label(root,bg="white")
down.place(x=0,y=100,width=1500,height=68)

bon=Label(root,text="BON VOYAGE ",font=("arial",40,"bold"),bg="white")
bon.place(x=100,y=100)
come=Label(root,text="Come Explore your Dreams!!!",font=("Lora",25),bg="white")
come.place(x=465,y=118)

#for flight

path1='flight.jpg'
img1 = ImageTk.PhotoImage(Image.open(path1))
panel1 = Label(root, image = img1)
panel1.place(x=100,y=190,width=650,height=450)
top=Label(root,text="TAKE ONLY MEMORIES..LEAVE ONLY FOOTPRINTS!!",font=("arial",20),fg="BLACK")
top.place(x=100,y=650,width=700,height=30)

a='heel.png'
b= ImageTk.PhotoImage(Image.open(a))
panel2 = Label(root, image = b)
panel2.place(x=100,y=700,width=400,height=200)
root.mainloop()
