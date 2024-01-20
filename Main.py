"""
This is the main file for EVERouter

Inspired by Chloroken and his routing software: https://github.com/chloroken/routed

Version: 1.0
"""

from tkinter import*

class EVERouter(Frame):
	"""docstring for EVERouter"""


	def __init__(self):
		Frame.__init__(self)
		self.master.title("EVEGuide")
		self.grid()

		#New System Button
		self.SysButton = Button(self, text = "New System", command = self.CreateSystem)
		self.SysButton.grid(row = 0, column = 0, rowspan = 2)

		#System Input Field
		self.SysVar = StringVar()
		self.SysInput = Entry(self, textvariable = self.SysVar)
		self.SysInput.grid(row = 0, column = 3)

	def CreateSystem(self):
		#Event Handler for SysButton
		
		#Create Sys Frame
		self.SystemWidget = Frame(self)
		self.SystemWidget.grid(row = 0, column = 20)

		#Add Sig List
		
		self.SigList()

		#Add Sig Entry Field

		#self.SigScroll = Scrollbar(self.SystemWidget, orient = VERTICAL)
		#self.SigScroll.grid(row = 0, column = 1, sticky = N+S)

		#self.SigList = Listbox(self.SystemWidget, width = 6, height = 10, selectmode = SINGLE, yscrollcommand = self.SigScroll.set)
		#self.SigList.grid(row = 0, column = 0, sticky = N+S)
		#self.SigScroll["command"] = self.SigList.yview

		#Add Sig Buttons (Add)

	def SigList(self):

		#System = self.SysVar.get() (Doesn't work at all lmao)

		self.SigSys = Entry(self.SystemWidget, textvariable = self.SysVar) #Makes the input field update real time with entry box
		self.SigSys.grid(row = 0, column = 0, sticky = N)

		self.SigScroll = Scrollbar(self.SystemWidget, orient = VERTICAL)
		self.SigScroll.grid(row = 1, column = 1, sticky = N+S)

		self.SigList = Listbox(self.SystemWidget, width = 6, height = 10, selectmode = SINGLE, yscrollcommand = self.SigScroll.set)
		self.SigList.grid(row = 1, column = 0, sticky = N+S)
		self.SigScroll["command"] = self.SigList.yview

def main():
	EVERouter().mainloop()

main()
