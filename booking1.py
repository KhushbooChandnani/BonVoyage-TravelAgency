from tkinter import *
from tkinter.tix import *
from datetime import date

import last_page as lp

import functions as f

class booking1:
	
	def backToHome(self,root):
		from HomePage import frontpage
		frontpage(root)

	def btnClicked(self,name,root):
		self.CheckInDate = date(self.inYr.get(),self.monthsDic[self.inMnth.get()],self.inDate.get())
		self.CheckOutDate = date(self.outYr.get(),self.monthsDic[self.outMnth.get()],self.outDate.get())
		l7 = Message(self.win,text='',width = 250)
		l7.place(x=550,y=460)

		if (self.CheckInDate < date.today()):
			l7.config(text ="Invalid Check in Date",font =("Times",15),fg = 'red')
		elif(self.CheckOutDate <= date.today() or self.CheckOutDate <= self.CheckInDate):
			l7.config(text ="Invalid Check out Date",font =("Times",15),fg = 'red')
		else:
			self.roomCount = self.rooms.get()
			self.pax = self.guests.get()
			self.x = self.flight.get()
			self.x = int(self.x)
			rent = f.rentCal(self.CheckInDate,self.CheckOutDate,self.roomCount,name,self.pax,self.x)
			print(rent[0])
			print(rent[1])
			l7.config(text = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t",width = 250)
			self.submit(root,name,rent)




	def __init__(self,root,screen_height,screen_width,name):
		self.monthsDic = {'January':1,'February':2,'March':3,'April':4,'May':5,'June':6,'July':7,'August':8,'September':9,'October':10,'November':11,'December':12}
		self.months = ('January','February','March','April','May','June','July','August','September','October','November','December')
		
		self.inDate  = IntVar()
		self.outDate  = IntVar()
		self.inMnth = StringVar()
		self.outMnth = StringVar()
		self.inYr = IntVar()
		self.outYr = IntVar()
		self.rooms = IntVar()
		self.guests = IntVar()
		self.flight = IntVar()

		self.mainframe = Frame(root,width = screen_width,height = screen_height)
		self.mainframe.pack()
		self.swin = ScrolledWindow(self.mainframe, width=screen_width, height=screen_height)
		self.swin.pack()
		self.win = self.swin.window
		self.win.config(bg="#F5F5F5")

		self.l0 = Label(self.win,text = str(name),font=("Lucida",23),fg = "#039BE5",bg="#F5F5F5").place(x=450,y=100)		
		self.l1=Label(self.win,text="Please fill in the following details.",font=("Lucida calligraphy",25,"bold"),bg="#F5F5F5",fg="#039BE5")
		self.l1.place(x=400,y=25)

		self.l2 = Label(self.win,text = "Name of guest :",font=("Times",20),bg="#F5F5F5")
		self.l2.place(x=100,y=175)

		self.l3 = Label(self.win,text = "Check in date :",font=("Times",20),bg="#F5F5F5")
		self.l3.place(x=100,y=225)

		self.l4 = Label(self.win,text = "Check out date :",font=("Times",20),bg="#F5F5F5")
		self.l4.place(x=100,y=275)

		self.l5 = Label(self.win,text = "No. of rooms :",font=("Times",20),bg="#F5F5F5")
		self.l5.place(x=100,y=325)

		self.l6 = Label(self.win,text = "Guests per room :",font=("Times",20),bg="#F5F5F5")
		self.l6.place(x=100,y=375)
		

		self.b=Button(self.win,command=lambda:self.backToHome(root))
		self.img=PhotoImage(file="res/home_login.png")
		self.b.config(image=self.img,width="60",height="60",bg="#F5F5F5",bd=0)
		self.b.place(x=screen_width-100,y=18)


		self.nameEntry = Entry(self.win,font = ("Times",16))
		self.nameEntry.place(x=500,y=175)

		self.roomEntry = Spinbox(self.win,from_=1,to=5,width=2,textvariable = self.rooms,fg='black',bg='#F5F5F5',font=('Times',16))
		self.roomEntry.place(x=500,y=325)
		self.guestEntry = Spinbox(self.win,from_=1,to=4,width=2,textvariable = self.guests,fg='black',bg='#F5F5F5',font=('Times',16))
		self.guestEntry.place(x=500,y=375)
		
		self.chkIndt=Spinbox(self.win,from_=1,to=31,width=2,textvariable = self.inDate,fg='black',bg='#F5F5F5',font=('Times',16)).place(x=500,y=225)
		self.chkInMnth=Spinbox(self.win, values= self.months,textvariable = self.inMnth,width=10,fg='black',bg='#F5F5F5',font=('Times',16)).place(x=550,y=225)
		self.chkInYr=Spinbox(self.win,from_=2018,to=2026,width=5,textvariable = self.inYr,fg='black',bg='#F5F5F5',font=('Times',16)).place(x=705,y=225)
		
		self.chkOutdt=Spinbox(self.win,from_=1,to=31,width=2,textvariable = self.outDate,fg='black',bg='#F5F5F5',font=('Times',16)).place(x=500,y=275)
		self.chkOutMnth=Spinbox(self.win, values= self.months,width=10,textvariable = self.outMnth,fg='black',bg='#F5F5F5',font=('Times',16)).place(x=550,y=275)
		self.chkOutYr=Spinbox(self.win,from_=2018,to=2026,width=5,textvariable = self.outYr,fg='black',bg='#F5F5F5',font=('Times',16)).place(x=705,y=275)

		self.confirmBtn = Button(self.win,text="CONFIRM",font=("Times",22,'bold'),bg='red',fg='#F5F5F5',command = lambda : self.btnClicked(name,root)).place(x=700,y=550)


		self.checkBox = Checkbutton(self.win,text = "Include Flight Fare",variable = self.flight,onvalue = 1,offvalue = 0,font=("Times",20),bg="#F5F5F5")
		self.checkBox.place(x=100,y=460) 

	def submit(self,root,name,rent):
		guestName = str(self.nameEntry.get())
		if (guestName == ""):
			l7 = Label(self.win,text ="Please Enter a Name",font =("Times",15),fg = 'red',bg="#F5F5F5").place(x=500,y=460)
			return
		lp.create_page(root,name,guestName,rent[0],rent[1],self.CheckInDate,self.CheckOutDate,self.roomCount,self.pax)
		
def main(origin,name = None):	
	if origin :
		origin.destroy()
	root = Tk()
	screen_width = root.winfo_screenwidth()
	screen_height = root.winfo_screenheight()
	root.minsize(width=screen_width, height=screen_height)
	root.config(bg="#FA8072")
	root.title("Bon Voyage")
	
	bk = booking1(root,screen_height,screen_width,name)
	root.mainloop()
