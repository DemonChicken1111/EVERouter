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
		#print(clipboard)

		#Parses Text
		clipboard = clipboard.split("\n")
		NewSigList = list(clipboard)

		#print(NewSigList)

		if NewSigList[0][3] != "-":
			return
		if NewSigList == '':
			return
		if NewSigList.len() == 0:
			return

		SigList = ['RMM-936\tCosmic Anomaly\tOre Site\tMedium Jaspet Deposit\t100.0%\t6.17 AU', 'UIY-608\tCosmic Anomaly\tCombat Site\tAngel Den\t100.0%\t7.47 AU', 'HQJ-988\tCosmic Anomaly\tCombat Site\tAngel Den\t100.0%\t7.57 AU', 'VSG-874\tCosmic Anomaly\tCombat Site\tDrone Assembly\t100.0%\t7.82 AU', 'KTA-296\tCosmic Anomaly\tCombat Site\tAngel Rally Point\t100.0%\t7.97 AU', 'PSH-909\tCosmic Anomaly\tCombat Site\tAngel Hideaway\t100.0%\t7.97 AU', 'JUX-749\tCosmic Anomaly\tCombat Site\tAngel Hidden Den\t100.0%\t8.60 AU', 'WFM-672\tCosmic Anomaly\tCombat Site\tAngel Hideaway\t100.0%\t8.88 AU', 'GOU-950\tCosmic Anomaly\tOre Site\tGlacial Mass Belt\t100.0%\t8.96 AU', 'AYQ-296\tCosmic Anomaly\tCombat Site\tAngel Yard\t100.0%\t9.03 AU', 'UCZ-104\tCosmic Signature\t\t\t0.0%\t49.06 AU', 'BAS-475\tCosmic Anomaly\tCombat Site\tAngel Rally Point\t100.0%\t49.20 AU']

		i = 0
		j = 0
		while i < NewSigList.len():
			i += 1
			while j < SigList.len():
				j += 1
				if NewSigList[0:7] == SigList[0:7]:
					print("existing sig found")



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
