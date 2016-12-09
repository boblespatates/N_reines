# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:54 2016

@author: emacedegastines
"""
import numpy as np
from Fonctions import Fonctions
from Liste import Liste

class ParcoursEnLargeur(Fonctions):
    
    
    def parcoursEnLargeurRec( listeSolution, n ):
        ''' fonction récursive pour le parcours en largeur
        - listeSolution : liste de solutions partielles 
        - i : nombre de ligne déjà remplies à l'entrée de la fonction 
        - n : taille de l'échiquier '''
        if listeSolution == []:
            return []
        permutation = Liste.premierListe(listeSolution)
        i = len(permutation)
        if (i == n ):
            return Liste.construit(permutation, ParcoursEnLargeur.parcoursEnLargeurRec( Liste.resteListe(listeSolution), n ) )

        #vérifie quand l'ajout d'une reine marche
        for j in range( n ):
            permutation.append(j) 
            if Fonctions.test2( permutation, i+1, i ):
                #Si l'ajout d'une reine marche, l'ajoute a la collection
                listeSolution.append( list(permutation) )
            permutation.pop(i)

        #Comme on n'est pas encore à la dernière ligne, ajoute une nouvelle reine
        return ParcoursEnLargeur.parcoursEnLargeurRec( Liste.resteListe(listeSolution), n )
        
    def algorithme(n):
        ''' parcourt le graphe en largeur pour chercher les solutions
        - n : taille de l'échiquier '''
        return( ParcoursEnLargeur.parcoursEnLargeurRec( [[]], n ) )
        


    algorithme = staticmethod(algorithme)
    parcoursEnLargeurRec = staticmethod(parcoursEnLargeurRec)
    
    
