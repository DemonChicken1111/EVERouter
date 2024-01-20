"""
This is the main file for EVERouter

Inspired by Chloroken and his routing software: https://github.com/chloroken/routed

Version: 1.0
"""

from tkinter import*
from tkinter import ttk
from tkinter.ttk import *
import pyperclip

class EVERouter(Frame):
	"""docstring for EVERouter"""


	def __init__(self):
		Frame.__init__(self)
		self.master.title("EVERouter")
		self.grid()

		#Create Menu
		self.Menu = Menu(self.master)
		self.master.config(menu = self.Menu)

		self.FileMenu = Menu(self.Menu, tearoff = False)
		self.Menu.add_cascade(menu = self.FileMenu, label = "File")

		self.FileMenu.add_command(label = "New Route")
		self.FileMenu.add_command(label = "Open Route")
		self.FileMenu.add_command(label = "Copy clipboard", command = self.AddSigs)

		#Create Treeview
		self.Tree = Treeview(self, columns = ("lastupdate"), selectmode = BROWSE)
		self.Tree.heading("#0", text = "System")
		self.Tree.heading("lastupdate", text = "Last Updated")
		self.Tree.grid(row = 2, column = 0)

		#Create SigDisplay
		self.SigDisplay = Text(self, height = 10, width = 40)
		self.SigDisplay.grid(row = 2, column = 2)


	def AddSigs(self):

		#Reads Clipboard
		clipboard = pyperclip.paste()

		#Parses Text

		#Compares to a dictionary ['id': 'sig text'] 
		#If sigs no longer exist: Delete.

		#Change Sys Last Updated Value

	def OpenSigs(self):
		#Reads dictionary and looks for current selction id

		#Puts dictionary data into SigDisplay

	def ReadData():
		#Parses Text

		#Compares to a dictionary ['id': 'sig text'] 
		#If sigs no longer exist: Delete.

	def SaveData():
		#Change Sys Last Updated Value


def main():
	EVERouter().mainloop()

main()
