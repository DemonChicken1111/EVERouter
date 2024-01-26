"""
EVE Tool for local explorers, nomads, and frequent scanners 

Inspired by Chloroken and his routing software: https://github.com/chloroken/routed

Version: 1.0
"""

from itertools import zip_longest
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import pyperclip
import pickle

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

		self.FileMenu.add_command(label = "New Route", command = self.AddRoute)
		self.FileMenu.add_command(label = "Open Route", command = self.OpenRoute)
		self.FileMenu.add_separator()
		self.FileMenu.add_command(label = "Save Route", command = self.SaveRoute)

		self.SigMenu = Menu(self.Menu, tearoff = False)
		self.SigMenu.add_command(label = "Add Sigs", command = self.AddSigs)

		#Create Treeview
		self.Tree = Treeview(self, columns = ("lastupdate"), selectmode = BROWSE)
		self.Tree.heading("#0", text = "System")
		self.Tree.heading("lastupdate", text = "Last Updated")
		self.Tree.grid(row = 2, column = 0)

		#Create SigDisplay
		self.SigDisplay = Text(self, height = 10, width = 40)
		self.SigDisplay.grid(row = 2, column = 2)


	def DisplayUpdate(self):

		#Updates SigDisplay's text based on TreeList current selection
		Selection = self.Tree.selection()[0]



	def AddSigs(self):

		#Reads Clipboard
		SigClipboard = pyperclip.paste()

		#Parses New Text
		NewSigList = SigClipboard.split("\n")
			#print(NewSigList)

    	#Pulls SigList from save file dictonary, based on current selection ID
    	#Current List is for testing purposes
		SigList = self.SigDict[Selection]


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
					print(n)
			SigList[i] = n
					
		#Updates SigList to now collated list
		print("updated sigs")
		print(SigList)

		#Gets ID, and Adds ID + SigList to Dictionary
		self.SigDict = {}
		Selection = self.Tree.selection()[0]

		self.SigDict[Selection] = SigList
		print("\n\n")
		print(self.SigDict)

		self.SigDisplay.insert(INSERT, self.SigDict[self.Tree.selection()[0]])

	def AddRoute(self):

		#Makes Route Name
		Route = self.Tree.insert("", END, text = "New Route")

		#Parses Clipboard (Route)
		RouteClipboard = pyperclip.paste()
		self.RouteList = []
	
		#Removes "Current Location:"
		#Looks for "(" and trims after it
		for line in RouteClipboard.splitlines("\n"):
			line = line.split("(")
			if len(line) > 1:
				self.RouteList.append(line[0])

		print(self.RouteList)

		#Adds Parsed Systesms as Subitems
		for i, r in enumerate(self.RouteList):
			self.Tree.insert(Route, END, text = r)

	def SaveRoute(self):

		#Makes save file
		RouteSave = "Route.pickle"
		SigSave = "Sig.pickle"

		#Adds RouteList and SigDict to file
		with open(RouteSave, "wb") as file:
			pickle.dump(self.RouteList, file)
			file.close()

		with open(SigSave, "wb") as file:
			pickle.dump(self.SigDict, file)
			file.close()

		print("Route Saved")

	def OpenRoute(self):

		RouteSave = "Route.pickle"
		SigSave = "Sig.pickle"
		Route = self.Tree.insert("", END, text = "New Route")

		#gets save file and opens it
		with open(RouteSave, "rb") as file:
			self.RouteList = pickle.load(file)
			file.close()

		with open(SigSave, "rb") as file:
			self.SigDict = pickle.load(file)
			file.close()

		#Adds systems to tree
		for i, r in enumerate(self.RouteList):
			self.Tree.insert(Route, END, text = r)

def main():
	EVERouter().mainloop()

main()
