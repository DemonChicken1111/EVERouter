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


	def CreateSystem(self):
		#Event Handler for SysButton
		
		#Create Sys Frame
		self.SystemWidget = Frame(self)
		self.SystemWidget.grid(row = 0, column = 20)

		#Add Sig List
		self.SigScroll = Scrollbar(self.SystemWidget, orient = VERTICAL)
		self.SigList = Listbox(self.SystemWidget, width = 6, height = 10, selectmode = SINGLE, yscrollcommand = self.SigScroll.set)

		if bool(self.SigList.winfo_exists()) == True:
			print("True")
		else:
			self.SigScroll.grid(row = 0, column = 1, sticky = N+S)
			self.SigList.grid(row = 0, column = 0, sticky = N+S)
			self.SigScroll["command"] = self.SigList.yview

		#Add Sig Entry Field
		#self.SigScroll.grid(row = 0, column = 1, sticky = N+S)

		#self.SigList.grid(row = 0, column = 0, sticky = N+S)
		#self.SigScroll["command"] = self.SigList.yview

		#Add Sig Buttons (Add)



def main():
	EVERouter().mainloop()

main()
