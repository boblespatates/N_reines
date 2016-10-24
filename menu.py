#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

class Menu(Frame):
	''' Classe definissant un menu
	qui va demander le nombre de dames,
	et la technique de resolution.'''
	
	def __init__(self,fenetre):
		''' Constructeur de la classe menu '''

		# Initialisation de la fentre
		Frame.__init__(self,fenetre)
		self.pack(fill=BOTH)
		self.initialize()


	def initialize(self):
		''' Place les widgets dans la fenetre '''

		# Spinbox pour N_REINES
		self.spinbox()
			
		# Pour la lisibilite du menu
		label_espace = Label(self, text=' ')
                label_espace.pack()
		
		# Radios bouttons pour ALGORITHME
		self.radio_boutton()
		
		# Fermer la fenetre
		self.boutton()
	
	def spinbox(self):
		''' Cree une spinbox pour
		le nombre de reines '''
		
		label1 = Label(self, text='Choix de N', font=('Arial 13'))
                label1.pack()
                self.spinbox1 = Spinbox(self, from_=4, to=50, textvariable=Number)
                self.spinbox1.pack()
		
	def radio_boutton(self):
		''' Cree des radiobouttons
		pour le choix de l'algo '''

		label2 = Label(self, text='Choix de l algorithme', font=('Arial 13'))
                label2.pack()
                for algo in ['Force Brute', 'Force Brute plus',
                 'Parcours en profondeur', 'Parcours en largeur']:
                        rb = Radiobutton(self, text=algo, value=algo, variable=Algorithme)
                        rb.pack(side=LEFT)
	
	def boutton(self):
		''' Cree un boutton pour
		fermer la fenetre '''

		self.bouton_valider = Button(self, text="Valider", command=self.valider)
                self.bouton_valider.pack(side=BOTTOM)	

	
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
