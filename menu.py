#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from Tkinter import *

class Menu(Frame):
	''' Classe definissant un menu
	qui va demander le nombre de dames,
	et la technique de resolution.'''
	
	def __init__(self,fenetre):
		''' Constructeur de la classe 
		La fenetre menu'''

		Frame.__init__(self,fenetre, width=768, height=576)
		self.pack(fill=BOTH)
		
		# Spinbox pour N_REINES
		self.spinbox1 = Spinbox(self, from_=8, to=50, textvariable=Number)
		self.spinbox1.pack()
		
		# Radio boutton pour ALGORITHME
		for algo in ['Arbre Binaire', 'Brute Force']:
			rb = Radiobutton(self, text=algo, value=algo, variable=Algorithme)
			rb.pack()

		# Fermer la fenetre
		self.bouton_valider = Button(self, text="Valider", command=self.valider)
		self.bouton_valider.pack()		

		
	def valider(self):
		''' Recupere les donnees et ferme la fenetre '''

		self.ALGORITHME = Algorithme.get()
		self.N_REINES = Number.get()
		print(self.N_REINES)
		print(self.ALGORITHME)
		self.destroy()
fenetre = Tk()
Number = IntVar()
Algorithme = StringVar()
a1 = Menu(fenetre)
a1.mainloop()
print(a1.N_REINES)
print(a1.ALGORITHME)
