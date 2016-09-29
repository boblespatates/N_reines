# -*- coding: utf-8 -*-

# CLASSE: Case

class Case:

	'''Classe caracterisée par:
	-une dimention
	-un centre (donc une coordonée x et une y)
	-un contenu
	-un numero'''

	def __init__(dimention,centreX,centreY,contenu,numero):
		
		self.dimention = dimention
		self.centreX = centreX
		self.centreY = centreY
		self.contenu = contenu
		self.numero = numero

