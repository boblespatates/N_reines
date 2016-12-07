# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:54 2016

@author: emacedegastines
"""
import numpy as np
from Fonctions import Fonctions
from Liste import Liste

class ParcoursEnLargeur(Fonctions):
        
    def parcoursEnLargeurRec2( listeSolution, i, n ):
        ''' fonction récursive pour le parcours en largeur
        - listeSolution : liste de solutions partielles 
        - i : nombre de ligne déjà remplies à l'entrée de la fonction 
        - n : taille de l'échiquier '''
        nouvelleListeSolution = []
        #parcourt la collection des solutions partielles
        for L in listeSolution:
            #pour chaque solution partielle, vérifie si l'ajout d'une reine marche toujours
            for j in range( n ):
                L.append( j )
                if Fonctions.test2( L, i + 1, i ):
                    #Si l'ajout d'une reine marche, l'ajoute a la collection
                    nouvelleListeSolution.append( list(L) )
                L.pop(i)
                
        #Si on n'est pas encore à la dernière ligne, ajoute une nouvelle reine
        if i < n :
            return ParcoursEnLargeur.parcoursEnLargeurRec2( nouvelleListeSolution, i + 1, n ) 
        return listeSolution
    
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
        
    def algorithme2(n):
        ''' parcourt le graphe en largeur pour chercher les solutions
        - n : taille de l'échiquier '''
        return( ParcoursEnLargeur.parcoursEnLargeurRec2( [[]], 0, n ) )


    algorithme = staticmethod(algorithme)
    algorithme2 = staticmethod(algorithme2)
    parcoursEnLargeurRec = staticmethod(parcoursEnLargeurRec)
    parcoursEnLargeurRec2 = staticmethod(parcoursEnLargeurRec2)


    
    
print( ParcoursEnLargeur.algorithme(5) )