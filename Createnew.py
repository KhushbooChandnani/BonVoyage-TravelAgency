from tkinter import *
from PIL import ImageTk, Image
import os	

def create_window():
	class FullScreenApp(object):
	    def __init__(self, master, **kwargs):
	        self.master=master
	        pad=3
	        self._geom='200x200+0+0'
	        master.geometry("{0}x{1}+0+0".format(
	            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
	        master.bind('<Escape>',self.toggle_geom)            
	    def toggle_geom(self,event):
	        geom=self.master.winfo_geometry()
	        print(geom,self._geom)
	        self.master.geometry(self._geom)
	        self._geom=geom
	master=Toplevel()
	app=FullScreenApp(master)
	master.config(bg="White")
	lab_cont = Label(master,text="Page is Under Construction.",background="white",font = "Arial 42",foreground="Black")
	lab_cont.place(x=220,y=200)

	path = "res/logoc.png"
	img = ImageTk.PhotoImage(Image.open(path))
	panel = Label(master, image=img,background="white")
	panel.place(x=0,y=0)
	master.mainloop()
















'''def page_under_construction() :
	class FullScreenApp(object):
		def __init__(self, master, **kwargs):
			self.master=master
			pad=3
			self._geom='200x200+0+0'
			master.geometry("{0}x{1}+0+0".format(
			master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
			master.bind('<Escape>',self.toggle_geom)            
		def toggle_geom(self,event):
			geom=self.master.winfo_geometry()
			print(geom,self._geom)
			self.master.geometry(self._geom)
			self._geom=geom
		master=Toplevel()
		app=FullScreenApp(master)
		master.config(bg="White")
		lab_cont = Label(master,text="Page is Under Construction.",background="white",font = "Arial 42",foreground="Black")
		lab_cont.place(x=220,y=200)

		path = "res/logoc.png"
		img = ImageTk.PhotoImage(Image.open(path))
		panel = Label(master, image=img,background="white")
		panel.place(x=0,y=0)
		master.mainloop()
'''