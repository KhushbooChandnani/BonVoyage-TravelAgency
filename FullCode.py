from tkinter import *
from tkinter.tix import *
from PIL import Image,ImageTk


#================PAGE UNDER CONSTRUCTION=======================#
def page_under_construction() :
	from PIL import Image,ImageTk
	newpage_root=Toplevel()
	newpage_root.title("Page is Under Construction.")
	screen_width = newpage_root.winfo_screenwidth()
	screen_height = newpage_root.winfo_screenheight()
	newpage_root.minsize(width=screen_width, height=screen_height)
	newpage_root.config(bg="White")
	lab_cont = Label(newpage_root,text="Page is Under Construction.",background="white",font = "Arial 42",foreground="Black")
	lab_cont.place(x=220,y=200)

	path10 = "logoc.png"
	image10 = Image.open(path10)
	img = ImageTk.PhotoImage(image10)
	panel = Label(newpage_root, image=img,background="white")
	panel.place(x=0,y=0)
	newpage_root.mainloop()
#==============================================================#
#============================HOME PAGE=========================#
def frontpage() :
	home_root = Tk()
	home_root.title("HomePage")
	screen_width = home_root.winfo_screenwidth()
	screen_height = home_root.winfo_screenheight()
	main_frame = Frame(home_root,width = screen_width,height = screen_height)
	main_frame.pack()
	swin = ScrolledWindow(main_frame, width=screen_width, height=screen_height)
	swin.pack()
	win = swin.window

	home_root.minsize(width=screen_width, height=screen_height)
	home_root.config(bg="white")
	#home_root.attributes("-fullscreen",True)

	top=Frame(win,width=screen_width,height=screen_height,bg="white")
	top.pack()

	path1 = "background.jpg"
	imgobj1 = Image.open(path1)
	backimg = ImageTk.PhotoImage(imgobj1)
	backimg_lab = Label(top,image = backimg,background="white")
	backimg_lab.image = backimg
	backimg_lab.pack()

	lab_top = Label(top,bg = "black")
	lab_top.place(x=0,y=0,width=screen_width,height=50)

	#--------------------------------------------------------------------------------#
	#Top Buttons 

	about=Button(top,text="About",bd=0,font=("arial",15),fg="white",bg="black")
	about.place(x=50,y=0,width=150,height=50)
	services=Button(top,text="Services",bd=0,font=("arial",15),fg="white",bg="black")
	services.place(x=200,y=0,width=150,height=50)
	contact=Button(top,text="Contact",bd=0,font=("arial",15),fg="white",bg="black")
	contact.place(x=350,y=0,width=150,height=50)
	login = Button(top,text="My Profile",bd=0,font=("arial",15),fg="white",bg="black",command=lambda:loginpage(home_root))
	login.place(x=screen_width-200,y=0,width=150,height=50)
	down=Label(top,bg="white")
	down.place(x=0,y=100,width=1500,height=68)

	#--------------------------------------------------------------------------------#
	#Main Header
	bon=Label(top,text="BON VOYAGE ",font=("arial",40,"bold"),bg="white")
	bon.place(x=100,y=100)
	come=Label(top,text="Come Explore your Dreams!!!",font=("Lora",25),bg="white")
	come.place(x=465,y=118)

	#For Flight
	path1='flight.jpg'
	image2 = Image.open(path1)
	img1 = ImageTk.PhotoImage(image2)
	panel1 = Label(top, image = img1)
	panel1.place(x=100,y=190,width=650,height=450)
	top=Label(top,text="TAKE ONLY MEMORIES..LEAVE ONLY FOOTPRINTS!!",font=("arial",20),fg="BLACK")
	top.place(x=100,y=650,width=700,height=30)

	heel='heel.png'
	image3 = Image.open(heel)
	heelimg= ImageTk.PhotoImage(image3)
	panel2 = Label(top, image = heelimg)
	panel2.place(x=100,y=700,width=400,height=200)

	home_root.mainloop()
#==============================================================#
#============================LOGIN PAGE========================#
def loginpage(home_root):
	from PIL import Image,ImageTk
	home_root.destroy()
	login_root = Tk()
	login_root.title("Login Page")
	screen_width = login_root.winfo_screenwidth()
	screen_height = login_root.winfo_screenheight()
	login_root.minsize(width=screen_width, height=screen_height)
	login_root.config(bg="white")
	#login_root.attributes("-fullscreen",True)

	gg='#134e86'
	g="#0a2845#"
	gw="white"

	path = "logoc.png"
	image4 = Image.open(path)
	img = ImageTk.PhotoImage(image4)
	panel = Label(login_root, image=img,background="white")
	panel.image = img
	panel.place(x=0,y=0)

	tk_rgb = "#%02x%02x%02x" % (32,48,60)
	lb_rgb = "#%02x%02x%02x" % (133,143,150)

	lab_login = Label(login_root,text="Log In",background="white",font = "Arial 42",foreground=tk_rgb)
	lab_login.place(x=630,y=100)

	lab_newuser = Label(login_root,text="New to Bon Voyage? ",background="white",font = "Arial 15",foreground=tk_rgb)
	lab_newuser.place(x=570,y=170)

	lab_signup = Label(login_root,text="Sign Up.",background="white",font = "Arial 15",foreground=tk_rgb)
	lab_signup.place(x=760,y=170)

	b4 = Button(login_root,text="Sign Up",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 15",relief=RAISED,overrelief=RIDGE,command=lambda:registerpage(login_root))
	img5 = PhotoImage(file = "signup.png")
	b4.config(image=img5)
	b4.place(x=760,y=170)

	lab_username = Label(login_root,text="Email : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_username.place(x=230,y=310)

	uname = Entry(login_root,font="Arial 18")
	uname.place(x=375,y=315,width=250)

	lab_passwd = Label(login_root,text="Password : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_passwd.place(x=230,y=371)

	passwd = Entry(login_root,font="Arial 18",show="*")
	passwd.place(x=375,y=376,width=250)

	path1 = "separator.jpg"
	image5 = Image.open(path1)
	img1 = ImageTk.PhotoImage(image5)
	panel1 = Label(login_root, image = img1)
	panel1.image = img1
	panel1.place(x=700,y=265,width=1,height=280)

	check_remember=Checkbutton(login_root,text="Keep me logged in.",bg="white",font="Arial 14")
	check_remember.place(x=230,y=430)

	b1 = Button(login_root,text="Sign In",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE)
	image = PhotoImage(file="signin2.png",)
	b1.config(image=image)
	b1.place(x=380,y=500)

	b2 = Button(login_root,text="Facebook",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=lambda:page_under_construction())
	img2 = PhotoImage(file = "fbutton.png")
	b2.config(image=img2)
	b2.place(x=830,y=325)

	b3 = Button(login_root,text="Google",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=lambda:page_under_construction())
	img3 = PhotoImage(file = "gbutton.png")
	b3.config(image=img3)
	b3.place(x=830,y=400)

	lab_conditions1 = Label(login_root,text = "* By signing up, you agree to our Terms of Use ,Privacy \nPolicy and to receive Bon Voyage emails, newsletters & updates",background="white",font = "Arial 11",foreground=lb_rgb)
	lab_conditions1.place(x=550,y=590)

	
	login_root.mainloop()
#==============================================================#
#============================REGISTER PAGE=====================#
def registerpage(login_root) :
	from PIL import ImageTk, Image
	login_root.destroy()
	register_root=Tk()
	screen_width = register_root.winfo_screenwidth()
	screen_height = register_root.winfo_screenheight()
	#root.attributes('-fullscreen',True)
	register_root.minsize(width=screen_width, height=screen_height)
	register_root.config(bg="White")

	gg='#134e86'
	g="#0a2845#"
	gw="white"

	path = "logoc.png"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = Label(register_root, image=img,background="white")
	panel.place(x=0,y=0)

	tk_rgb = "#%02x%02x%02x" % (32,48,60)
	lb_rgb = "#%02x%02x%02x" % (133,143,150)

	lab_login = Label(register_root,text="Sign Up",background="white",font = "Arial 42",foreground=tk_rgb)
	lab_login.place(x=630,y=50)

	lab_newuser = Label(register_root,text="Already a Bon Voyage user?",background="white",font = "Arial 15",foreground=tk_rgb)
	lab_newuser.place(x=570,y=120)

	b4 = Button(register_root,text="Log in.",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 15",relief=RAISED,overrelief=RIDGE,command=lambda:loginpage(register_root))
	img5 = PhotoImage(file = "login1.png")
	b4.config(image=img5)
	b4.place(x=825,y=124)

	lab_name = Label(register_root,text="Name : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_name.place(x=230,y=210)

	name = Entry(register_root,font="Arial 18")
	name.place(x=375,y=215,width=250)

	lab_username = Label(register_root,text="Email : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_username.place(x=230,y=260)

	uname = Entry(register_root,font="Arial 18")
	uname.place(x=375,y=265,width=250)

	lab_passwd = Label(register_root,text="Password : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_passwd.place(x=228,y=318)

	passwd = Entry(register_root,font="Arial 16",show="*")
	passwd.place(x=375,y=321,width=250)

	lab_passwd_re = Label(register_root,text="Retype\nPassword : ",background="white",font = "Arial 20",foreground=tk_rgb)
	lab_passwd_re.place(x=228,y=370)

	passwd_re = Entry(register_root,font="Arial 16",show="*")
	passwd_re.place(x=375,y=390,width=250)

	path1 = "separator.jpg"
	img1 = ImageTk.PhotoImage(Image.open(path1))
	panel1 = Label(register_root, image = img1)
	panel1.place(x=700,y=205,width=1,height=330)

	sign_up = Button(register_root,text="Sign Up",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE)
	image7 = PhotoImage(file="sign_up1.png",)
	sign_up.config(image=image7)
	sign_up.place(x=380,y=470)

	b2 = Button(register_root,text="Facebook",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=lambda:page_under_construction())
	img2 = PhotoImage(file = "fbutton.png")
	b2.config(image=img2)
	b2.place(x=830,y=285)

	b3 = Button(register_root,text="Google",padx=20,pady=10,bd=0,bg="white",fg="white",font="Arial 14 bold",relief=RAISED,overrelief=RIDGE,command=lambda:page_under_construction())
	img3 = PhotoImage(file = "gbutton.png")
	b3.config(image=img3)
	b3.place(x=830,y=360)

	lab_conditions1 = Label(register_root,text = "* By signing up, you agree to our Terms of Use ,Privacy \nPolicy and to receive Bon Voyage emails, newsletters & updates",background="white",font = "Arial 11",foreground=lb_rgb)
	lab_conditions1.place(x=550,y=590)

	register_root.mainloop()
#==============================================================#
#============================HOTELS PAGE=======================#

#==============================================================#
#============================BOOKING PAGE======================#

#==============================================================#
#============================END PAGE==========================#

#==============================================================#
#====================DataBaseConnectivity======================#
	
#==============================================================#
#========================Function Calls========================#
frontpage()         #This function call starts the entire program
#==============================================================#
