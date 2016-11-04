# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:54 2016

@author: emacedegastines
"""

class ParcoursEnProfondeur(Fonctions):
    
    def parcoursEnProfondeurRec(permutation, i, n):
        ''' fonction récursive pour le parcours en profondeur
        - permutation : solution partielle étudiée
        - i : nombre de ligne déjà remplies à l'entrée de la fonction
        - n : taille de l'échiquier'''
        for j in range( n ):
            permutation[i] = j
            if not test2( permutation, i + 1, i ): 
                #si oui, déplace la reine vers la droite           
                continue
            #sinon, passe à la ligne suivante
            else :
                if i < n - 1:
                    parcoursEnProfondeurRec( permutation, i + 1, n)
                #enregistre la solution car on a parcouru toute les lignes
                else :
                    listeSolution.append(permutation)
        #si une reine ne peut pas se placer sur une ligne, revient à la ligne précédente
        return listeSolution
        
    def algorithme( n ):
        ''' parcourt le graphe en profondeur pour chercher les solutions
        - n : taille de l'échiquier '''
        permutation = np.zeros( n )
        return( parcoursEnProfondeurRec( permutation, 0, n) )
