from tkinter import *
from tkinter.tix import *
from PIL import ImageTk, Image
import os
import Login as L
import about_page
import Maldives
import dubai
import paris
import uk

#============================HOME PAGE=========================#
def frontpage(root) :
        root.destroy()
        home_root = Tk()
        home_root.title("Bon Voyage")
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

        path1 ="res/blur_flight.png"
        imgobj1 = Image.open(path1)
        backimg = ImageTk.PhotoImage(imgobj1)
        backimg_lab = Label(top,image = backimg,background="white")
        backimg_lab.image = backimg
        backimg_lab.pack()

        lab_top = Label(top,bg = "black")
        lab_top.place(x=0,y=0,width=screen_width,height=50)

	#--------------------------------------------------------------------------------#
	#Top Buttons 

        about=Button(top,text="About",bd=0,font=("lora",15),fg="white",bg="black",command=lambda:about_page.about(home_root))
        about.place(x=50,y=0,width=150,height=50)
        services=Button(top,text="Services",bd=0,font=("lora",15),fg="white",bg="black")
        services.place(x=200,y=0,width=150,height=50)
        contact=Button(top,text="Contact",bd=0,font=("lora",15),fg="white",bg="black")
        contact.place(x=350,y=0,width=150,height=50)
        login = Button(top,text="LOG IN",bd=0,font=("lora",15),fg="white",bg="black",command=lambda:L.create_login(home_root))
        login.place(x=screen_width-200,y=0,width=150,height=50)
        down=Label(top,bg="white")
        down.place(x=0,y=100,width=1500,height=75)
        

	#--------------------------------------------------------------------------------#
	#Main Header
        bon=Label(top,text="BON VOYAGE ",font=("lucida calligraphy",40,"bold"),bg="white")
        bon.place(x=55,y=100)
      
        come=Label(top,text="   Come Explore your Dreams!!!",font=("lucida calligraphy",25),bg="white")
        come.place(x=490,y=123)
        	
	#--------------------------------------------------------------------------------#
	#Lower Buttons
        b3 = Button(top,bd=0,command=lambda:Maldives.maldivespage(home_root))
        img3 = PhotoImage(file = "res/Maldives_but1.png")
        b3.config(image=img3)
        b3.place(x=55,y=450,width=270,height=180)

        b4 = Button(top,bd=0,command=lambda:dubai.dubaipage(home_root))
        img4 = PhotoImage(file = "res/Dubai1.png")
        b4.config(image=img4)
        b4.place(x=375,y=450,width=270,height=180)

        b5 = Button(top,bd=0,command=lambda:paris.parispage(home_root))
        img5 = PhotoImage(file = "res/paris1.png")
        b5.config(image=img5)
        b5.place(x=695,y=450,width=282,height=180)

        b6 = Button(top,bd=0,command=lambda:uk.ukpage(home_root))
        img6 = PhotoImage(file = "res/uk_and_ireland1.png")
        b6.config(image=img6)
        b6.place(x=1022,y=450,width=270,height=180)

       
        home_root.mainloop()
#--------------------------------------------------------------------#
