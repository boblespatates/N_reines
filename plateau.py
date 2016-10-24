#!/usr/bin/env python
# -*- coding utf-8 -*-

from Tkinter import *

class Plateau(Frame):
	''' Classe ou l'on pourra voir les
	resultats sur un plateau '''

	def __init__(self,fenetre,N_REINES):
		''' Constructeur de la classe plateau '''

		# Initialisation de la fentre
		Frame.__init__(self,fenetre)
		self.pack(fill=BOTH)
		self.initialize()
	
	def initialize(self):
			
		# La grille 
		canvas = Canvas(self, width=(1+N_REINES*50), height=(1+N_REINES*50))
		DIM_CASE = 50
		x0,y0 = 1,1

		for i in range(N_REINES+1):
			print(x0+ DIM_CASE*i)
			print(y0 + N_REINES*DIM_CASE)
			canvas.create_line(x0+DIM_CASE*i, y0,x0+DIM_CASE*i,y0 + N_REINES*DIM_CASE)
        		canvas.create_line(x0, y0+DIM_CASE*i,x0+N_REINES*DIM_CASE ,y0+DIM_CASE*i)
		canvas.pack()				
		
fenetre = Tk()
N_REINES = 8
a2 = Plateau(fenetre,N_REINES)
a2.mainloop()
print(bonjour)	
