# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:30:52 2016

@author: emacedegastines
"""

import Fonctions

class ForceBrute(Fonctions.Fonctions):

    def algorithme(n):
        ''' parcourt les permutations, vérifie si elles sont solutions
        - n : taille de l'échiquier '''
        listeSolution = []
        permutation = []
        # variable testant si l'algorithme de permutations est arrivé à terme (True: l'algorithme n'est pas terminé, False: toutes les permutations ont été parcourues
        isPermutation = True
        #initialise la première permutation
        permutation = np.linspace( 0, n - 1, n )
        if test( permutation, n ):
            listeSolution.append(permutation)
        #parcourt les permutations
        while isPermutation:
            #calcul de la permutation suivante
            resultat = nextPermutationSJT( permutation, n )
            isPermutation = resultat[0]
            # si la permutation est solution, l'enregistre
            if isPermutation and test( permutation, n ):
                permutationPositive = [ abs(x) for x in permutation ]
                listeSolution.append(permutationPositive)
        return(listeSolution)
        
