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

		#Add Sig List

		#Add Sig Entry Field

		#Add Sig Buttons (Add)


def main():
	EVERouter().mainloop()

main()
