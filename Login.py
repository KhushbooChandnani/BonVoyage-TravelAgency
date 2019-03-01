from tkinter import *
import os
from Register import create_register
import functions as f
import HomePage

def create_login(origin):
	from PIL import ImageTk, Image
	import Createnew
	from HomePage import frontpage
	origin.destroy()
	origin = Tk()
	#origin = Frame(origin,)
	origin.title("Bon Voyage")

	screen_width = origin.winfo_screenwidth()
	screen_height = origin.winfo_screenheight()
	#origin.attributes('-fullscreen',True)
	origin.minsize(width=screen_width, height=screen_height)
	origin.config(bg="White")

	gg='#134e86'
	g="#0a2845#"
	gw="white"

	path = "res/logoc.png"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = Label(origin, image=img,background="white")
	panel.place(x=0,y=0)

	tk_rgb = "#%02x%02x%02x" % (32,48,60)
	lb_rgb = "#%02x%02x%02x" % (133,143,150)

	lab_login = Label(origin,text="Log In",background="white",font = "Arial 42",foreground=tk_rgb)
	lab_login.place(x=630,y=100)

	lab_newuser = Label(origin,text="New to Bon Voyage? ",background="white",font = "Arial 15",foreground=tk_rgb)
	lab_newuser.place(x=570,y=170)

	lab_signup = Label(origin,text="Sign Up.",background="white",font = "Arial 15",foreground=tk_rgb)
	lab_signup.place(x=760,y=170)

	b4 = Button(origin,text="Sign Up",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 15",relief=RAISED,overrelief=RIDGE,command=lambda:create_register(origin))
	img5 = PhotoImage(file = "res/signup.png")
	b4.config(image=img5)
	b4.place(x=760,y=170)

	home_but = Button(origin,text = "Home",padx=20,pady=10,bd=0,bg="white",fg="white",relief=RAISED,overrelief=RIDGE,command=lambda:HomePage.frontpage(origin))
	img_home = PhotoImage(file = "res/home_login.png")
	home_but.config(image=img_home)
	home_but.place(x=screen_width-80,y=10)

	lab_username = Label(origin,text="Email : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_username.place(x=230,y=310)

	global uname 
	uname = Entry(origin,font="Arial 18")
	uname.place(x=375,y=315,width=250)

	lab_passwd = Label(origin,text="Password : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_passwd.place(x=230,y=371)

	global passwd
	passwd = Entry(origin,font="Arial 18",show="*")
	passwd.place(x=375,y=376,width=250)

	path1 = "res/separator.jpg"
	img1 = ImageTk.PhotoImage(Image.open(path1))
	panel1 = Label(origin, image = img1)
	panel1.place(x=700,y=265,width=1,height=280)

	check_remember=Checkbutton(origin,text="Keep me logged in.",bg="white",font="Arial 14")
	check_remember.place(x=230,y=430)

	b1 = Button(origin,text="Sign In",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command = lambda : submit(origin))
	image = PhotoImage(file="res/signin2.png",)
	b1.config(image=image)
	b1.place(x=380,y=510)

	b2 = Button(origin,text="Facebook",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=Createnew.create_window)
	img2 = PhotoImage(file = "res/fbutton.png")
	b2.config(image=img2)
	b2.place(x=830,y=325)

	b3 = Button(origin,text="Google",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=Createnew.create_window)
	img3 = PhotoImage(file = "res/gbutton.png")
	b3.config(image=img3)
	b3.place(x=830,y=400)

	lab_conditions1 = Label(origin,text = "* By signing up, you agree to our Terms of Use ,Privacy \nPolicy and to receive emails, newsletters & updates from Bon Voyage",background="white",font = "Arial 11",foreground=lb_rgb)
	lab_conditions1.place(x=550,y=590)

	origin.mainloop()


def submit(origin):
	usrname = uname.get()
	password = passwd.get()

	if(usrname == ""):
		l = Label(origin,text = "Enter valid Email-Id",font = "Arial 14",bg= 'white',fg = 'red')
		l.place(x = 230 , y = 470)
	elif(password == ""):
		l = Label(origin,text = "Enter Password\t",font = "Arial 14",bg = 'white',fg = 'red')
		l.place(x = 230 , y = 470)
	else:
		l = Label(origin,text = "\t\t\t",font = "Arial 14",bg = 'white',fg = 'red')
		l.place(x = 230 , y = 470)
		boo = f.signin_data(usrname,password)
		if boo == 1:
			HomePage.frontpage(origin)