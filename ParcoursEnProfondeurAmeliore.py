# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 13:34:47 2016

@author: emacedegastines
"""
import numpy as np
from Fonctions import Fonctions
from Liste import Liste

class ParcoursEnProfondeurAmeliore(Fonctions):
    
    def parcoursLigne(permutation, L, i, j, matriceDeCollision, n):
        ''' fonction récursive pour le parcours en profondeur
        - permutation : solution partielle étudiée
        - L : liste des indices dans l'ordre de remplissage
        - i : nombre de lignes déjà remplies
        - j : colonne à tester
        - matriceDeCollision : matrice indiquant les zones occupées ou menacées par une reine
        - n : taille de l'échiquier'''
        permutation[ int(L[i]) ] = j #int car probleme de float
        if Fonctions.test4( permutation, L, i):
            if i == n - 1:
                #retourne une solution
                return [list(permutation)]
            
            else:
                nouvelleMatriceDeCollision = list(matriceDeCollision)
                Fonctions.miseAJourCollisions( int(L[i]), j, nouvelleMatriceDeCollision, n )
                if j == n - 1:
                    # retourne les solutions en ajoutant un pion
                    return( ParcoursEnProfondeurAmeliore.parcoursEnProfondeurRec( list(permutation), L, i + 1, nouvelleMatriceDeCollision,  n ) )
                else:
                    #retourne les solutions en ajoutant un pion ou en déplacant le dernier pion selon j
                    return Liste.concatene( ParcoursEnProfondeurAmeliore.parcoursLigne( list(permutation), L, i, j + 1, matriceDeCollision, n ), ParcoursEnProfondeurAmeliore.parcoursEnProfondeurRec( list(permutation), L, i + 1, nouvelleMatriceDeCollision, n ) )
        else:
            if j != n - 1:
                #retourne les solutions en déplacant le dernier pion selon j
                return ParcoursEnProfondeurAmeliore.parcoursLigne( list(permutation), L, i, j + 1, matriceDeCollision, n )
        return []
        
    def parcoursEnProfondeurRec(permutation, L, i, matriceDeCollision, n):
        ''' fonction récursive pour le parcours en profondeur
        - permutation : solution partielle étudiée
        - L : liste des indices dans l'ordre de remplissage
        - i : nombre de lignes déjà remplies
        - matriceDeCollision : matrice indiquant les zones occupées ou menacées par une reine
        - n : taille de l'échiquier'''
        minNombrePlacement = n+1
        # cherche la ligne possédant le moins de placements viables pour un pion
        for j in range(i,n):        
            nombrePlacement = Fonctions.test3( matriceDeCollision, int(L[j]), n )
            if (minNombrePlacement > nombrePlacement):
                minNombrePlacement = nombrePlacement
                ligneMinimale = j
                
        if (minNombrePlacement == 0 ):
            return []
        #met à jour la liste des indices considérés
        (L[i],L[ligneMinimale]) = (L[ligneMinimale], L[i])
        return ParcoursEnProfondeurAmeliore.parcoursLigne(permutation, L, i, 0, matriceDeCollision, n)
        
    
    
    def algorithme( n ):
        ''' parcourt le graphe en profondeur pour chercher les solutions
        - n : taille de l'échiquier '''
        permutation = np.zeros( n )
        L = np.linspace(0,n-1,n)
        matriceDeCollision = np.zeros((n,n))
        return( ParcoursEnProfondeurAmeliore.parcoursLigne( permutation, L, 0, 0, matriceDeCollision, n) )

    algorithme = staticmethod(algorithme)
    parcoursEnProfondeurRec = staticmethod(parcoursEnProfondeurRec)
    parcoursLigne = staticmethod(parcoursLigne)
    