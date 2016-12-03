# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:53 2016

@author: emacedegastines
"""
import numpy as np
from Fonctions  import Fonctions

class ForceBruteAmelioree(Fonctions):

    def miseAJourCollisions( permutation, i, j, matriceCollision, n ):
        ''' met à jour la matrice de collision M selon L sachant que les dames i et j ont été permutées
        - permutation : permutation actuelle
        - i : première dame déplacée
        - j : deuxième dame déplacée
        - matriceCollision : matrice de transposition
        - n : taille de l'échiquier'''
        #True si il n'y a pas de collisions sur les deux dames interverties, False sinon        
        isCollision = True
        for k in range(n):
            if  k != i  and abs( k - i ) == abs( abs( permutation[k] )-abs( permutation[i] ) ) :
                isCollision = False
                matriceCollision[k][i] = 1
                matriceCollision[i][k] = 1
            else:
                matriceCollision[k][i] = 0
                matriceCollision[i][k] = 0
            if  k != j  and abs( k - j ) == abs( abs( permutation[k] )-abs( permutation[j] ) ) :
                isCollision = False
                matriceCollision[k][j] = 1
                matriceCollision[j][k] = 1
            else:
                matriceCollision[k][j] = 0
                matriceCollision[j][k] = 0
        if isCollision:
            #s'il n'y a pas de nouvelles collisions, teste toute la matrice
            isCollision = Fonctions.test( permutation, n )
        return isCollision
                
        
        
    def algorithme( n ):
        ''' même principe que force brute, retient la matrice des collisions pour une verication plus rapide de la permutation (la permutation suivante différant seulement d'une transposition)
        - n : taille de l'échiquier '''
        listeSolution = []
        # variable testant si l'algorithme de permutations est arrivé à terme (True: l'algorithme n'est pas terminé, False: toutes les      permutations ont été parcourues
        isPermutation = True
        #matrice de coillision : la i-ème ligne ou colonne correspond à la i-ème dame. A_ij = 1 si les dames i et j sont en collison, 0 sinon.
        matriceCollision = np.ones( ( n, n ) )
        #initialise la première permutation
        permutation = np.linspace( 0, n - 1, n )
        if Fonctions.test( permutation, n ):
            listeSolution.append(list(permutation))
        #parcourt les permutations
        while isPermutation:
            #calcul de la permutation suivante
            resultat = Fonctions.nextPermutationSJT( permutation, n )
            isPermutation = resultat[0]
            # si la permutation est solution, l'enregistre
            if ForceBruteAmelioree.miseAJourCollisions( permutation, resultat[1], resultat[2], matriceCollision, n ):
                permutationPositive = [ abs(x) for x in permutation ]
                listeSolution.append(permutationPositive)
        return(listeSolution)


    algorithme = staticmethod(algorithme)
    miseAJourCollisions = staticmethod(miseAJourCollisions)