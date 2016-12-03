#!/usr/bin/env python
# -*- coding utf-8 -*-

from Tkinter import *

class Plateau(Frame):
	''' Classe ou l'on pourra voir les
	resultats sur un plateau '''

	def __init__(self,fenetre,N_REINES,matrice_solution):
		''' Constructeur de la classe plateau '''

		# Initialisation de la fentre
		Frame.__init__(self,fenetre)
		self.pack(fill=BOTH)
		self.solution = 0
		self.matrice_solution = matrice_solution
		self.N_REINES = N_REINES
		self.initialize()
	
	def initialize(self):
		''' Dessine la fentre avec
		ses differentes composantes '''	
		
		# La grille 
		self.grille(self.N_REINES,self.matrice_solution[self.solution])	
		# Le bouton suivant
		self.boutton_suivant()
			
	def grille(self,N_REINES,vecteur_position):
		''' Dessine la grille et place
		les pions '''
		
		self.canvas = Canvas(self, width=(1+N_REINES*50), height=(1+N_REINES*50))
		
		# Dessin de la grille
		DIM_CASE = 50
		x0,y0 = 1,1
		for i in range(N_REINES+1):
			coordonees_colonne = [x0 + DIM_CASE * i , y0 , x0 + DIM_CASE * i , y0 + N_REINES * DIM_CASE]
			coordonees_ligne = [x0 , y0 + DIM_CASE * i , x0 + N_REINES * DIM_CASE , y0 + DIM_CASE * i]
			self.canvas.create_line(coordonees_colonne)
			self.canvas.create_line(coordonees_ligne)
		
		# Place les pions
		n = 0
		x0,y0 = 4,4
		x1,y1 = 49,49
		for i in vecteur_position:
			temps = DIM_CASE*i
			coordonees = [x0+DIM_CASE*n,y0+temps,x1+DIM_CASE*n,y1+temps]
			self.canvas.create_oval(coordonees,fill='black',outline='white')
			n += 1	
		
		self.canvas.pack()				
	
	def boutton_suivant(self):
		''' Cree un bouton pour passer
		a la solution suivante '''
		
		self.bouton_suivant = Button(self, text="Suivant", command=self.suivant)
		self.bouton_suivant.pack()
	
	def suivant(self):
		''' Passe a la solution
		suivante '''
			
		# Prochaine solution	
		self.solution += 1
		
		#print(self.solution)
		#print(self.matrice_solution)
		#print (len(self.matrice_solution))

		#  A la fin, retour a la 1 ere solution
		if self.solution >= (len(self.matrice_solution)):
			self.solution = 0
		
		# Prochaine solution 
		self.restart()
	
	def restart(self):
		''' Suprime tout le contenu de la
		de la fenetre et en remet un nouveau '''
		
		self.canvas.destroy()
		self.bouton_suivant.destroy()
		self.initialize()
