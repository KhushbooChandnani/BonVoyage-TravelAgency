from tkinter import *
import os   
from tkinter.tix import *

def about_button():
    pass
    
def services_button():
    pass
    
def contact_button(top):
    from PIL import ImageTk, Image
    root=Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    top.destroy()

    mainframe=Frame(root,width=screen_width,height=screen_height,bg="white")
    mainframe.pack()
    #p='logoc.png'
    img7 = ImageTk.PhotoImage(Image.open("res/logoc.png"))
    pan = Label(mainframe, image = img7)
    pan.place(x=0,y=0,width=200,height=100)

#--------------------------------------------------------------------------------#
#Function that creates the main page
def create_main():
    from PIL import ImageTk, Image

    root=Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    main_frame = Frame(root,width = screen_width,height = screen_height)
    main_frame.pack()
    swin = ScrolledWindow(main_frame, width=screen_width, height=screen_height)
    swin.pack()
    win = swin.window

    root.minsize(width=screen_width, height=screen_height)
    root.config(bg="white")
    #root.attributes("-fullscreen",True)

    top=Frame(win,width=screen_width,height=screen_height,bg="white")
    top.pack()

    #Background
    path='res/bg.jpg'
    img = ImageTk.PhotoImage(Image.open(path))
    panel = Label(top, image = img)
    panel.pack(expand = "yes")

    remain1=Label(top,bg="black")
    remain1.place(x=0,y=0,width=screen_width,height=50)


#--------------------------------------------------------------------------------#
    #Top Buttons 

    about=Button(top,text="About",bd=0,font=("arial",15),fg="white",bg="black",command=about_button)
    about.place(x=50,y=0,width=150,height=50)
    services=Button(top,text="Services",bd=0,font=("arial",15),fg="white",bg="black",command=services_button)
    services.place(x=200,y=0,width=150,height=50)
    contact=Button(top,text="Contact",bd=0,font=("arial",15),fg="white",bg="black",command=contact_button(top))
    contact.place(x=350,y=0,width=150,height=50)
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
    img1 = ImageTk.PhotoImage(Image.open(path1))
    panel1 = Label(top, image = img1)
    panel1.place(x=100,y=190,width=650,height=450)
    top=Label(top,text="TAKE ONLY MEMORIES..LEAVE ONLY FOOTPRINTS!!",font=("arial",20),fg="BLACK")
    top.place(x=100,y=650,width=700,height=30)

    a='heel.png'
    b= ImageTk.PhotoImage(Image.open(a))
    panel2 = Label(top, image = b)
    panel2.place(x=100,y=700,width=400,height=200)

    root.mainloop()

#-------------------------------------------------------------#
create_main()
