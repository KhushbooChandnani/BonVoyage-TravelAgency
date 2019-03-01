from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image


root=Tk()
root.title("Maldives")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

mainframe = Frame(root,width = screen_width,height = screen_height)
mainframe.pack()
swin = ScrolledWindow(mainframe, width=screen_width, height=screen_height)
swin.pack()
win = swin.window

root.minsize(width=screen_width, height=screen_height)
root.config(bg="white")
#root.attributes("-fullscreen",True)

frame_width = win.winfo_screenwidth()
frame_height = 1600

top=Frame(win,width=frame_width,height=60,bg="white")
top.pack(side=TOP)

f1=Frame(win,width=frame_width/2,height=frame_height-60,bg="white")
f1.propagate(0)
f1.pack(side=LEFT)


f2=Frame(win,width=frame_width/2,height=frame_height-60,bg="white")
f1.propagate(0)
f2.pack(side=RIGHT)


lb=Label(top,text="MALDIVES",font=("arial",40,"bold"),fg="blue",bg="white")
lb.place(x=470,y=0)
lb=Label(top,text="Come Explore Your Dreams",font=("arial",15,"bold"),fg="blue",bg="white")
lb.place(x=470,y=70)

path="mal1.jpg"

photo=ImageTk.PhotoImage(Image.open(path))
lb=Label(f1,image=photo)
lb.place(x=70,y=40,width=510,height=250)

l1=Label(f2,text="The  Mirihi  Island",font=("arial",30,"bold"),fg="black",bg="white")
l1.place(x=0,y=40)

path1="star.png"

photo1=ImageTk.PhotoImage(Image.open(path1))
lb1=Label(f2,image=photo1,bg="white")
lb1.place(x=0,y=80,width=200,height=50)

l2=Label(f2,text="Rs.21000",font=("arial",20,"bold"),fg="blue",bg="white")
l2.place(x=9,y=120)
t1=Message(f2,text="Posh riverside lodging with chic rooms and a hip BBQ restaurant.",font=("arial",20),fg="black",bg="white",width = 400)
t1.place(x=0,y=160)
b1=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
b1.place(x=9,y=240)



path2="mal5.jpg"

photo2=ImageTk.PhotoImage(Image.open(path2))
lb2=Label(f1,image=photo2)
lb2.place(x=70,y=320,width=510,height=250)

l3=Label(f2,text="Komandoo Maldives Island",font=("arial",30,"bold"),fg="black",bg="white")
l3.place(x=0,y=320)

path3="star.png"

photo3=ImageTk.PhotoImage(Image.open(path3))
lb3=Label(f2,image=photo3,bg="white")
lb3.place(x=0,y=360,width=200,height=50)

l4=Label(f2,text="Rs.35000",font=("arial",20,"bold"),fg="blue",bg="white")
l4.place(x=9,y=400)
t1=Message(f2,text="Beautiful beaches with good view and exotic rooms best.",font=("arial",20),fg="black",bg="white",width = 400)
t1.place(x=0,y=440)
b1=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
b1.place(x=9,y=520)


path4="mal6.jpg"

photo4=ImageTk.PhotoImage(Image.open(path4))
lb4=Label(f1,image=photo4)
lb4.place(x=70,y=600,width=510,height=250)

l5=Label(f2,text="The Baros Maldives",font=("arial",30,"bold"),fg="black",bg="white")
l5.place(x=0,y=600)

path5="star.png"

photo5=ImageTk.PhotoImage(Image.open(path5))
lb5=Label(f2,image=photo5,bg="white")
lb5.place(x=0,y=640,width=200,height=50)

l5=Label(f2,text="Rs.45000",font=("arial",20,"bold"),fg="blue",bg="white")
l5.place(x=9,y=680)
t2=Message(f2,text="Beautiful beaches with good view and exotic rooms best.",font=("arial",20),fg="black",bg="white",width = 400)
t2.place(x=0,y=720)
b2=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
b2.place(x=9,y=800)

path6="mal40.jpg"

photo6=ImageTk.PhotoImage(Image.open(path6))
lb6=Label(f1,image=photo6)
lb6.place(x=70,y=880,width=510,height=250)

l7=Label(f2,text="The Grand Royale",font=("arial",30,"bold"),fg="black",bg="white")
l7.place(x=0,y=880)

path7="star.png"

photo7=ImageTk.PhotoImage(Image.open(path7))
lb7=Label(f2,image=photo5,bg="white")
lb7.place(x=0,y=920,width=200,height=50)

l8=Label(f2,text="Rs.40000",font=("arial",20,"bold"),fg="blue",bg="white")
l8.place(x=9,y=960)
t3=Message(f2,text="Natural view with good atmosphere and exotic rooms.",font=("arial",20),fg="black",bg="white",width = 400)
t3.place(x=0,y=1000)
b3=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
b3.place(x=9,y=1080)

path8="mal50.jpg"

photo8=ImageTk.PhotoImage(Image.open(path8))
lb8=Label(f1,image=photo8)
lb8.place(x=70,y=1160,width=510,height=250)

l9=Label(f2,text="Paradise Island Resort",font=("arial",30,"bold"),fg="black",bg="white")
l9.place(x=0,y=1160)

path9="star.png"

photo9=ImageTk.PhotoImage(Image.open(path9))
lb9=Label(f2,image=photo5,bg="white")
lb9.place(x=0,y=1200,width=200,height=50)

l10=Label(f2,text="Rs.55000",font=("arial",20,"bold"),fg="blue",bg="white")
l10.place(x=9,y=1240)
t4=Message(f2,text="Natural view with good atmosphere and exotic rooms.",font=("arial",20),fg="black",bg="white",width = 400)
t4.place(x=0,y=1280)
b4=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white")
b4.place(x=9,y=1360)

root.mainloop()
