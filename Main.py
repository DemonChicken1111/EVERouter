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

		self.FileMenu.add_command(label = "New Route", command = self.AddRoute)
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
		SigClipboard = pyperclip.paste()

		#Parses New Text
		NewSigList = SigClipboard.split("\n")
			#print(NewSigList)

    	#Pulls SigList from save file dictonary, based on current selection ID
    	#Current List is for testing purposes
		SigList = ['LCX-936\tCosmic Anomaly\tOre Site\tMedium Jaspet Deposit\t100.0%\t6.17 AU\r', 'UIY-608\tCosmic Anomaly\t\t\t100.0%\t7.47 AU\r', 'HQJ-988\tCosmic Anomaly\tCombat Site\tAngel Den\t100.0%\t7.57 AU\r', 'VSG-874\tCosmic Anomaly\tCombat Site\tDrone Assembly\t100.0%\t7.82 AU\r', 'KTA-296\tCosmic Anomaly\tCombat Site\tAngel Rally Point\t100.0%\t7.97 AU\r', 'PSH-909\tCosmic Anomaly\tCombat Site\tAngel Hideaway\t100.0%\t7.97 AU\r', 'JUX-749\tCosmic Anomaly\tCombat Site\tAngel Hidden Den\t100.0%\t8.60 AU\r', 'WFM-672\tCosmic Anomaly\tCombat Site\tAngel Hideaway\t100.0%\t8.88 AU\r', 'GOU-950\tCosmic Anomaly\tOre Site\tGlacial Mass Belt\t100.0%\t8.96 AU\r', 'AYQ-296\tCosmic Anomaly\t\t        \t100.0%\t9.03 AU\r', 'EFL-300\tCosmic Signature\t\t\t0.0%\t13.51 AU\r', 'UCZ-104\tCosmic Signature\t\t\t0.0%\t49.06 AU\r', 'BAS-475\tCosmic Anomaly\tCombat Site\tAngel Rally Point\t100.0%\t49.20 AU']

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

	def AddRoute(self):

		#Makes Route Name
		Route = self.Tree.insert("", END, text = "New Route")

		#Parses Clipboard (Route)
		RouteClipboard = pyperclip.paste()
		RouteList = []
	
		#Removes "Current Location:"
		#Looks for "(" and trims after it
		for line in RouteClipboard.splitlines("\n"):
			line = line.split("(")
			if len(line) > 1:
				RouteList.append(line[0])

		print(RouteList)

		#Adds Parsed Systesms as Subitems
		for i, r in enumerate(RouteList):
			self.Tree.insert(Route, END, text = r)



def main():
	EVERouter().mainloop()

main()
