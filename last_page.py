from tkinter import *
from tkinter.tix import *
from datetime import date
from Createnew import create_window
import functions as f


def create_page(origin,hotelName,guestName,roomFare,flightFare,inDate,outDate,roomCount,guestCount):

	origin.destroy()

	root=Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	main_frame = Frame(root,width = screen_width,height = screen_height)
	main_frame.pack()
	swin = ScrolledWindow(main_frame, width=screen_width, height=screen_height)
	swin.pack()
	win = swin.window
	root.minsize(width=screen_width, height=screen_height)
	root.config(bg="#6699FF")
	
	def btnclicked():
		state = f.booking_data(hotelName,guestName,inDate,outDate,roomCount,guestCount,total)
		if state == 1:
			create_window()
		else:
			Label(root,text = "Failed to connect to Server...",font = ("Arial" ,18),fg = 'red').place(x=300,y=500)


	total = roomFare + flightFare

	b=Button(win)
	img=PhotoImage(file="res/home_butt.png")
	b.config(image=img,width="60",height="40")
	b.place(x=1250,y=10)

	l1 = Label(win,text = "Name of Hotel : ",font =("Lucida Calligraphy",20,"bold"))
	l1.place(x=70,y=80)
	
	l2 = Label(win,width=20,height=1,text = hotelName,font =("Arial",20),bg="#E8E8E8")
	l2.place(x=420,y=80)
	
	l3 = Label(win,text = "Guest name : ",font =("Lucida Calligraphy",20,"bold"))
	l3.place(x=70,y=130)
	
	l4 = Label(win,width=20,height=1,text = guestName,font =("Arial",20),bg="#E8E8E8")
	l4.place(x=420,y=130)
	
	l5 = Label(win,text = "Hotel Rent : ",font =("Lucida Calligraphy",20,"bold"))
	l5.place(x=70,y=180)
	
	l6 = Label(win,width=20,height=1,text = str(roomFare),font =("Arial",20),bg="#E8E8E8")
	l6.place(x=420,y=180)
	
	l7 = Label(win,text = "Flight cost : ",font =("Lucida Calligraphy",20,"bold"))
	l7.place(x=70,y=230)
	
	l8 = Label(win,width=20,height=1,text = str(flightFare),font =("Arial",20),bg="#E8E8E8")
	l8.place(x=420,y=230)
	
	l9 = Label(win,text = "Total Amount : ",font =("Lucida Calligraphy",20,"bold"))
	l9.place(x=70,y=480)
	
	l10 = Label(win,width=20,height=1,text = str(total),font =("Arial",20),bg="#E8E8E8")
	l10.place(x=420,y=480)
	
	l11 = Label(win,text = "Check In Date : ",font =("Lucida Calligraphy",20,"bold"))
	l11.place(x=70,y=280)
	
	l12 = Label(win,width=20,height=1,text = str(inDate),font =("Arial",20),bg="#E8E8E8")
	l12.place(x=420,y=280)
	
	l13 = Label(win,text = "Check Out Date : ",font =("Lucida Calligraphy",20,"bold"))
	l13.place(x=70,y=330)
	
	l14 = Label(win,width=20,height=1,text = str(outDate),font =("Arial",20),bg="#E8E8E8")
	l14.place(x=420,y=330)
	
	l15 = Label(win,text = "No. of rooms : ",font =("Lucida Calligraphy",20,"bold"))
	l15.place(x=70,y=380)
	
	l16 = Label(win,width=20,height=1,text = str(roomCount),font =("Arial",20),bg="#E8E8E8")
	l16.place(x=420,y=380)

	l17 = Label(win,text = "Guests per Room : ",font =("Lucida Calligraphy",20,"bold"))
	l17.place(x=70,y=430)

	l18 = Label(win,width=20,height=1,text = str(guestCount),font =("Arial",20),bg="#E8E8E8")
	l18.place(x=420,y=430)

	b5=Button(win,text="Proceed To Payment",padx=20,pady=10,bd=5,bg="#0099FF",fg="white", command = btnclicked)
	b5.place(x=450,y=550)


	root.mainloop()



