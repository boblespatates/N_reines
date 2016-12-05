# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:54 2016

@author: emacedegastines
"""
import numpy as np
from Fonctions import Fonctions

class ParcoursEnProfondeur(Fonctions):

        
    def parcoursEnProfondeurRec(permutation, i, j, n):
        ''' fonction récursive pour le parcours en profondeur
        - permutation : solution partielle étudiée
        - i : nombre de ligne déjà remplies à l'entrée de la fonction
        - j : colonne a tester dans la i-ème ligne
        - n : taille de l'échiquier'''
        permutation[i] = j
        print(permutation)
        if Fonctions.test2( permutation, i + 1, i ): 
            if i == n - 1:
                #retourne une solution
                return [list(permutation)]
            
            else:
                if j == n - 1:
                    # retourne les solutions en ajoutant un pion
                    return( ParcoursEnProfondeur.parcoursEnProfondeurRec( list(permutation), i + 1, 0,  n) )
                else:
                    #retourne les solutions en ajoutant un pion ou en déplacant le dernier pion selon j
                    return Fonctions.concatene( ParcoursEnProfondeur.parcoursEnProfondeurRec( list(permutation), i, j + 1, n), ParcoursEnProfondeur.parcoursEnProfondeurRec( list(permutation), i + 1, 0, n) )
        else:
            if j != n - 1:
                #retourne les solutions en déplacant le dernier pion selon j
                return ParcoursEnProfondeur.parcoursEnProfondeurRec( list(permutation), i, j + 1, n)
        return []
        
    def algorithme( n ):
        ''' parcourt le graphe en profondeur pour chercher les solutions
        - n : taille de l'échiquier '''
        permutation = np.zeros( n )
        return( ParcoursEnProfondeur.parcoursEnProfondeurRec( list(permutation), 0, 0, n) )

    algorithme = staticmethod(algorithme)
    parcoursEnProfondeurRec = staticmethod(parcoursEnProfondeurRec)
    


#print( ParcoursEnProfondeur.algorithme(5))
