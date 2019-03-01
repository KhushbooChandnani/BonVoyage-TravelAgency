from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image
import HomePage
from booking1 import main

def paris_flight(origin):
	origin.destroy()
	root=Tk()

	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()

	mainframe = Frame(root,width = screen_width,height = screen_height)
	mainframe.pack()
	swin = ScrolledWindow(mainframe, width=screen_width, height=screen_height)
	swin.pack()
	win = swin.window

	root.minsize(width=screen_width, height=screen_height)
	root.config(bg="white")


	frame_width = win.winfo_screenwidth()
	frame_height = 1400

	top=Frame(win,width=frame_width,height=100,bg="white")
	top.pack(side=TOP)

	f1=Frame(win,width=frame_width/2,height=frame_height-60,bg="white")
	f1.propagate(0)
	f1.pack(side=LEFT)


	f2=Frame(win,width=frame_width/2,height=frame_height-60,bg="white")
	f1.propagate(0)
	f2.pack(side=RIGHT)

	#-----------HOME BUTTON-----------------------------------------------
	b=Button(top,command=lambda:HomePage.frontpage(root))
	img=PhotoImage(file="res/home_login.png")
	b.config(image=img,width="60",height="50",bg="white",bd = 0)
	b.place(x=screen_width-80,y=10)



	lb=Label(top,text="PARIS",font=("lucida calligraphy",40,"bold"),fg="#4EB1BA",bg="white")
	lb.place(x=560,y=0)
	lb=Label(top,text="FLIGHTS+HOTELS",font=("lucida calligraphy",28,"bold"),fg="#b20000",bg="white")
	lb.place(x=70,y=60)

	path="res/f3.jpg"

	photo=ImageTk.PhotoImage(Image.open(path))
	lb=Label(f1,image=photo)
	lb.place(x=70,y=40,width=510,height=250)

	l1=Label(f2,text="Spicejet+Holiday inn Paris",font=("arial",30,"bold"),fg="black",bg="white")
	l1.place(x=0,y=40)
	l1=Label(f2,text="Before Discount :",font=("arial",20,"bold"),fg="blue",bg="white")
	l1.place(x=0,y=90)
	l2=Label(f2,text="Rs.40000",font=("arial",20,"overstrike"),fg="red",bg="white")
	l2.place(x=235,y=90)
	l2=Label(f2,text="After Discount :",font=("arial",20,"bold"),fg="blue",bg="white")
	l2.place(x=0,y=120)
	l2=Label(f2,text="Rs.31000",font=("arial",20,"bold"),fg="green",bg="white")
	l2.place(x=210,y=120)
	t1=Message(f2,text="Posh riverside lodging with chic rooms and a hip BBQ restaurant.",font=("arial",20),fg="black",bg="white",width = 400)
	t1.place(x=0,y=160)
	b1=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white",command = lambda : main(root,"Holiday inn Paris"))
	b1.place(x=9,y=240)



	path2="res/f1.jpg"

	photo2=ImageTk.PhotoImage(Image.open(path2))
	lb2=Label(f1,image=photo2)
	lb2.place(x=70,y=320,width=510,height=250)

	l3=Label(f2,text="Emirates+Ideal Hotel Design",font=("arial",30,"bold"),fg="black",bg="white")
	l3.place(x=0,y=320)
	l4=Label(f2,text="Before Discount :",font=("arial",20,"bold"),fg="blue",bg="white")
	l4.place(x=0,y=370)
	l4=Label(f2,text="Rs.55000",font=("arial",20,"overstrike"),fg="red",bg="white")
	l4.place(x=235,y=370)
	l4=Label(f2,text="After Discount :",font=("arial",20,"bold"),fg="blue",bg="white")
	l4.place(x=0,y=400)
	l4=Label(f2,text="Rs.45000",font=("arial",20,"bold"),fg="green",bg="white")
	l4.place(x=210,y=400)
	t1=Message(f2,text="Beautiful beaches with good view and exotic rooms best.",font=("arial",20),fg="black",bg="white",width = 400)
	t1.place(x=0,y=440)
	b1=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white",command = lambda : main(root,"Ideal Hotel Design"))
	b1.place(x=9,y=520)


	path4="res/indigo.jpg"
	photo4=ImageTk.PhotoImage(Image.open(path4))
	lb4=Label(f1,image=photo4)
	lb4.place(x=70,y=600,width=510,height=250)
	l5=Label(f2,text="Indigo+Novotel Tour Eiffel Hotel",font=("arial",30,"bold"),fg="black",bg="white")
	l5.place(x=0,y=600)
	l5=Label(f2,text="Before Discount :",font=("arial",20,"bold"),fg="blue",bg="white")
	l5.place(x=0,y=654)
	l5=Label(f2,text="Rs.50000",font=("arial",20,"overstrike"),fg="red",bg="white")
	l5.place(x=235,y=654)
	l5=Label(f2,text="After Discount : ",font=("arial",20,"bold"),fg="blue",bg="white")
	l5.place(x=0,y=684)
	l5=Label(f2,text="Rs.40000",font=("arial",20,"bold"),fg="green",bg="white")
	l5.place(x=210,y=684)
	t2=Message(f2,text="Beautiful beaches with good view and exotic rooms best.",font=("arial",20),fg="black",bg="white",width = 400)
	t2.place(x=0,y=720)
	b2=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white",command = lambda : main(root,"Novotel Tour Eiffel Hotel"))
	b2.place(x=9,y=800)

	path6="res/jet.png"

	photo6=ImageTk.PhotoImage(Image.open(path6))
	lb6=Label(f1,image=photo6)
	lb6.place(x=70,y=880,width=510,height=250)

	l7=Label(f2,text="Jet Airways+Hotel ibis Paris",font=("arial",30,"bold"),fg="black",bg="white")
	l7.place(x=0,y=880)

	l8=Label(f2,text="Before Discount :",font=("arial",20,"bold"),fg="blue",bg="white")
	l8.place(x=9,y=930)

	l8=Label(f2,text="Rs.21000",font=("arial",20,"overstrike"),fg="red",bg="white")
	l8.place(x=235,y=930)

	l8=Label(f2,text="After Discount :",font=("arial",20,"bold"),fg="blue",bg="white")
	l8.place(x=9,y=960)

	l8=Label(f2,text="Rs.15000",font=("arial",20,"bold"),fg="green",bg="white")
	l8.place(x=210,y=960)
	t3=Message(f2,text="Natural view with good atmosphere and exotic rooms.",font=("arial",20),fg="black",bg="white",width = 400)
	t3.place(x=0,y=1000)
	b3=Button(f2,text="BOOK",padx=20,pady=10,bd=5,bg="blue",fg="white",command = lambda : main(root,"Hotel ibis Paris"))
	b3.place(x=9,y=1080)

	root.mainloop()
