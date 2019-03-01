from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image
import HomePage

def about (origin):
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
	#root.attributes("-fullscreen",True)
	root.title("Bon Voyage")
	
	frame_width = win.winfo_screenwidth()
	frame_height =2500


	back="#FFFFF0"
	top=Frame(win,width=frame_width,height=60,bg=back)
	top.pack(side=TOP)

	f1=Frame(win,width=frame_width/2,height=frame_height-60,bg=back)
	f1.propagate(0)
	f1.pack(side=LEFT)


	f2=Frame(win,width=frame_width/2,height=frame_height-60,bg=back)
	f1.propagate(0)
	f2.pack(side=RIGHT)

	l1=Label(top,text="About",font=("lucida calligraphy",40,"bold"),bg=back,fg="#c25245")
	l1.place(x=5,y=0)

	path="res/mal.jpg"

	photo=ImageTk.PhotoImage(Image.open(path))
	lb=Label(f1,image=photo)
	lb.place(x=70,y=40,width=510,height=350)

	l2=Label(f2,text="Take only memories..",font=("georgia",30,"bold"),fg="black",bg=back)
	l2.place(x=0,y=40)
	l3=Label(f2,text="Leave only footprints!!!",font=("georgia",30,"bold"),fg="black",bg=back)
	l3.place(x=0,y=80)
	m1=Message(f2,text="An experience designed to bring us back to our elements, immerse us in the magic of the woods, and challenge us to rediscover.",font=("arial",20),fg="black",bg=back)
	m1.place(x=0,y=140)

	l3=Label(f1,text="Every Gateaway is quest for...",font=("georgia",30,"bold"),fg="black",bg=back)
	l3.place(x=70,y=400)
	#------------------------------------

	b5=Button(f1,command=lambda:HomePage.frontpage(root))
	b5.config(text="Return to Home",font=("georgia",18),bg="red")
	b5.place(x=130,y=1750,width=200,height=50)

	l3=Label(f1,text="Balance",font=("georgia",30,"bold"),fg="#c25245",bg=back)
	l3.place(x=120,y=560)
	m2=Message(f1,text="Making cities, technology and work even better through nature, disconnection and rest",font=("arial",20),fg="black",bg=back)
	m2.place(x=120,y=620)

	path1="res/balance.jpg"
	photo1=ImageTk.PhotoImage(Image.open(path1))
	lb=Label(f2,image=photo1)
	lb.place(x=0,y=490,width=510,height=350)
	#--------------------------------------
	l3=Label(f2,text="Ritual",font=("georgia",30,"bold"),fg="#c25245",bg=back)
	l3.place(x=70,y=950)
	m3=Message(f2,text="Creating the time and space you need to explore, appreciate and wonder ",font=("arial",20),fg="black",bg=back)
	m3.place(x=70,y=1000)

	path2="res/ritual.png"
	photo2=ImageTk.PhotoImage(Image.open(path2))
	lb=Label(f1,image=photo2)
	lb.place(x=70,y=900,width=510,height=350)
	#-----------------------------------------

	l3=Label(f1,text="Leisure",font=("georgia",30,"bold"),fg="#c25245",bg=back)
	l3.place(x=120,y=1380)
	m3=Message(f1,text="Marrying the curiosity of a pioneer with the humility of a houseguest",font=("arial",20),fg="black",bg=back)
	m3.place(x=120,y=1430)

	path3="res/leisure.png"
	photo3=ImageTk.PhotoImage(Image.open(path3))
	lb=Label(f2,image=photo3)
	lb.place(x=0,y=1320,width=510,height=350)

	#--------------------------------------
	#--------NEXT------------------

	root.mainloop()
