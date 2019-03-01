from tkinter import *
from PIL import ImageTk, Image
import os	
import Login as L
import functions as f
import HomePage

def create_register(root) :
	import Createnew
	root.destroy()
	origin=Tk()
	screen_width = origin.winfo_screenwidth()
	screen_height = origin.winfo_screenheight()
	#root.attributes('-fullscreen',True)
	origin.minsize(width=screen_width, height=screen_height)
	origin.config(bg="White")
	origin.title("Bon Voyage")

	gg='#134e86'
	g="#0a2845#"
	gw="white"

	path = "res/logoc.png"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = Label(origin, image=img,background="white")
	panel.place(x=0,y=0)

	tk_rgb = "#%02x%02x%02x" % (32,48,60)
	lb_rgb = "#%02x%02x%02x" % (133,143,150)

	lab_login = Label(origin,text="Sign Up",background="white",font = "Arial 42",foreground=tk_rgb)
	lab_login.place(x=630,y=50)

	lab_newuser = Label(origin,text="Already a Bon Voyage user?",background="white",font = "Arial 15",foreground=tk_rgb)
	lab_newuser.place(x=570,y=120)

	b4 = Button(origin,text="Log in.",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 15",relief=RAISED,overrelief=RIDGE,command=lambda : L.create_login(origin))
	img5 = PhotoImage(file = "res/login1.png")
	b4.config(image=img5)
	b4.place(x=825,y=124)

	lab_name = Label(origin,text="Name : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_name.place(x=230,y=210)

	global name
	name = Entry(origin,font="Arial 18")
	name.place(x=375,y=215,width=250)

	lab_username = Label(origin,text="Email : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_username.place(x=230,y=260)

	global uname
	uname = Entry(origin,font="Arial 18")
	uname.place(x=375,y=265,width=250)

	lab_passwd = Label(origin,text="Password : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_passwd.place(x=228,y=318)

	global passwd
	passwd = Entry(origin,font="Arial 16",show="*")
	passwd.place(x=375,y=321,width=250)

	lab_passwd_re = Label(origin,text="Retype\nPassword : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_passwd_re.place(x=228,y=370)

	global passwd_re
	passwd_re = Entry(origin,font="Arial 16",show="*")
	passwd_re.place(x=375,y=390,width=250)

	path1 = "res/separator.jpg"
	img1 = ImageTk.PhotoImage(Image.open(path1))
	panel1 = Label(origin, image = img1)
	panel1.place(x=700,y=205,width=1,height=330)

	sign_up = Button(origin,text="Sign Up",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command = lambda : submit(origin))
	image7 = PhotoImage(file="res/sign_up1.png",)
	sign_up.config(image=image7)
	sign_up.place(x=400,y=490)

	home_but = Button(origin,text = "Home",padx=20,pady=10,bd=0,bg="white",fg="white",relief=RAISED,overrelief=RIDGE,command=lambda:HomePage.frontpage(origin))
	img_home = PhotoImage(file = "res/home_login.png")
	home_but.config(image=img_home)
	home_but.place(x=screen_width-80,y=10)

	b2 = Button(origin,text="Facebook",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=Createnew.create_window)
	img2 = PhotoImage(file = "res/fbutton.png")
	b2.config(image=img2)
	b2.place(x=830,y=285)

	b3 = Button(origin,text="Google",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=Createnew.create_window)
	img3 = PhotoImage(file = "res/gbutton.png")
	b3.config(image=img3)
	b3.place(x=830,y=360)

	lab_conditions1 = Label(origin,text = "* By signing up, you agree to our Terms of Use ,Privacy \nPolicy and to receive emails, newsletters & updates from Bon Voyage",background="white",font = "Arial 11",foreground=lb_rgb)
	lab_conditions1.place(x=550,y=590)

	origin.mainloop()


def submit(origin):
	usrname = name.get()
	email = uname.get()
	password = passwd.get()
	password2 = passwd_re.get()

	if(usrname == ""):
		l = Label(origin,text = "Enter a Name",font = "Arial 14",bg= 'white',fg = 'red')
		l.place(x = 230 , y = 455)
	elif(password == ""):
		l = Label(origin,text = "Enter Password\t",font = "Arial 14",bg = 'white',fg = 'red')
		l.place(x = 230 , y = 455)
	elif(email == ""):
		l = Label(origin,text = "Enter valid Email-Id",font = "Arial 14",bg= 'white',fg = 'red')
		l.place(x = 230 , y = 455)
	elif(password == ""):
		l = Label(origin,text = "Retype Password\t",font = "Arial 14",bg = 'white',fg = 'red')
		l.place(x = 230 , y = 455)
	elif(password2 == ""):
		l = Label(origin,text = "Retype Password\t",font = "Arial 14",bg = 'white',fg = 'red')
		l.place(x = 230 , y = 455)
	elif(password != password2):
		l = Label(origin,text = "Passwords Mismatch",font = "Arial 14",bg = 'white',fg = 'red')
		l.place(x = 230 , y = 455)
	else:
		l = Label(origin,text = "\t\t",font = "Arial 14",bg = 'white',fg = 'red')
		l.place(x = 230 , y = 455)
		boo = f.register_data(usrname,email,password)


	if boo == 1:
		HomePage.frontpage(origin)
	




#create_register()
