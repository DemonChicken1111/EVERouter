"""
This is the main file for EVERouter

Inspired by Chloroken and his routing software: https://github.com/chloroken/routed

Version: 1.0
"""

from itertools import zip_longest
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

		#Parses New Text
		NewSigList = clipboard.split("\n")

    	#Pulls SigList from save file dictonary, based on current selection ID
		SigList = []

		#Making sure SigList is a valid input
		if NewSigList[0][3] != "-":
			return
		if len(NewSigList) == 0:
			return
    
    	#Comparing NewSigList to SigList
		for i, (n, s) in enumerate(zip_longest(NewSigList, SigList)):
			if n == None: #Turns "None" values due to zip_longest into empty strings
				n = ""
				print(n)
			if s == None:
				s = ""
				print(s)
			if n[:7] == s[:7]: 
				print("existing sig found")
				if len(n) < len(s):
					print("replacing with more detailed sig")
					n = s
					
		#Updates SigList to now collated list
		print("updated sigs")
		SigList[i] = n
		
		#Save SigList to Route file

	def ReadData():
		#Opens Save File

		#Loads to dictionary

	def WriteData():


def main():
	EVERouter().mainloop()

main()
