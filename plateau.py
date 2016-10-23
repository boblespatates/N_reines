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
		
		# La grille 
		canvas = Canvas(self, width=(550+(N_REINES-8)*50), height=(550+(N_REINES-8)*50))
		DIM_CASE = 50
		x0,y0 = 9,9

		for i in range(N_REINES+1):
			canvas.create_line(x0+DIM_CASE*i, y0,x0+DIM_CASE*i,y0 + N_REINES*DIM_CASE)
        		canvas.create_line(x0, y0+DIM_CASE*i,x0+N_REINES*DIM_CASE ,y0+DIM_CASE*i)
						
		
fenetre = Tk()
N_REINES = 8
a2 = Plateau(fenetre,N_REINES)
a2.mainloop()
print(bonjour)	
