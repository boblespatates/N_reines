# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:34:47 2016

@author: emacedegastines
"""
import numpy as np
from Fonctions import Fonctions
from Liste import Liste

class ParcoursEnProfondeurAmeliore(Fonctions):

    def parcoursLigne(permutation, L, i, j, n):
        ''' fonction récursive pour le parcours en profondeur
        - permutation : solution partielle étudiée
        - L : liste des indices dans l'ordre de remplissage
        - i : nombre de lignes déjà remplies
        - j : colonne à tester
        - n : taille de l'échiquier'''
        permutation[ int(L[i]) ] = j #int car probleme de float
        if Fonctions.test4( permutation, L, i):
            if i == n - 1:
                #retourne une solution
                return [list(permutation)]
            
            else:
                if j == n - 1:
                    # retourne les solutions en ajoutant un pion
                    return( ParcoursEnProfondeurAmeliore.parcoursEnProfondeurRec( list(permutation), L, i + 1,  n ) )
                else:
                    #retourne les solutions en ajoutant un pion ou en déplacant le dernier pion selon j
                    return Liste.concatene( ParcoursEnProfondeurAmeliore.parcoursLigne( list(permutation), L, i, j + 1, n ), ParcoursEnProfondeurAmeliore.parcoursEnProfondeurRec( list(permutation), L, i + 1,  n ) )
        else:
            if j != n - 1:
                #retourne les solutions en déplacant le dernier pion selon j
                return ParcoursEnProfondeurAmeliore.parcoursLigne( list(permutation), L, i, j + 1, n )
        return []
        
    def parcoursEnProfondeurRec(permutation, L, i, n):
        ''' fonction récursive pour le parcours en profondeur
        - permutation : solution partielle étudiée
        - L : liste des indices dans l'ordre de remplissage
        - i : nombre de lignes déjà remplies
        - n : taille de l'échiquier'''
        minNombrePlacement = n
        # cherche la ligne possédant le moins de placements viables pour un pion
        for j in range(i,n):        
            nombrePlacement = Fonctions.test3( permutation, L, i, L[j], n )
            if (minNombrePlacement > nombrePlacement):
                minNombrePlacement = nombrePlacement
                ligneMinimale = j
                
        if (minNombrePlacement == 0 ):
            return []
        #met à jour la liste des indices considérés
        (L[i],L[ligneMinimale]) = (L[ligneMinimale], L[i])
        return ParcoursEnProfondeurAmeliore.parcoursLigne(permutation, L, i, 0, n)
        
    
    
    def algorithme( n ):
        ''' parcourt le graphe en profondeur pour chercher les solutions
        - n : taille de l'échiquier '''
        permutation = np.zeros( n )
        L = np.linspace(0,n-1,n)
        return( ParcoursEnProfondeurAmeliore.parcoursLigne( permutation, L, 0, 0, n) )

    algorithme = staticmethod(algorithme)
    parcoursEnProfondeurRec = staticmethod(parcoursEnProfondeurRec)
    parcoursLigne = staticmethod(parcoursLigne)
    
