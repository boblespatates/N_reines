    # -*- coding: utf-8 -*-


import numpy as np

class Fonctions:
    
    ''' Permet de résoudre le problème des N Reines. Les différents algorithmes héritent de cette classes'''

    
    def test( permutation, n ):
        ''' vérifie que la permutation est solution
        - permutation : permutation à vérifier
        - n : taille de l'échiquier'''
        for i in range( n - 1 ):
            for j in range( i + 1, n ):
                if  j != i and abs( j - i ) == abs( abs( permutation[j] )-abs( permutation[i] ) ):
                    return False
        return True
    
    
        
    def test2( permutation, n, i ): 
        ''' teste les conflits d'une permutation sur la i-ème ligne 
        - permutation : permutation à vérifier
        - n : taille de l'échiquier
        - i : ligne à vérifier '''
        for j in range( n ):
            if  j != i and ( permutation[j] == permutation[i] or abs( j - i ) == abs( abs( permutation[j] )-abs( permutation[i] ) ) ):
                return False
        return True
    
    
    def nextPermutationSJT(permutation, n):
        ''' pour une permutation donnée, calcule la permutation suivante selon l'algorithme de Steinhaus–Johnson–Trotter.
        Il faut que la direction soit précisée (nombre positif: direction vers la gauche, nombre négatif: direction vers la droite) 
        - permutation : permutation actuelle
        - n : taille de l'échiquier '''
        #cherche le plus grand élément, 
        for j in range(n-1, -1, -1): 
            for i in range(n):
                if permutation[i] == j or permutation[i] == -j:
                    p = i
                    break
            #vérifie la possibilité d'un décalage à gauche
            if permutation[p] > 0 and p > 0 and abs( permutation[p - 1] ) < abs( permutation[p] ):
                ( permutation[p], permutation[p - 1] ) = ( permutation[p - 1], permutation[p] )
                return ( True, p , p - 1 )
            #vérifie la possibilité d'un décalage à droite        
            if permutation[p] < 0 and p < n - 1 and abs( permutation[p + 1] ) < abs( permutation[p] ):
                ( permutation[p], permutation[p + 1] ) = ( permutation[p + 1], permutation[p] )
                return ( True, p, p + 1 )
            #si le décalage n'est pas possible, change la direction
            permutation[p] = -permutation[p]
        return ( False, 0, 0 )
    
    
    test = staticmethod(test)
    test2 = staticmethod(test2)
    nextPermutationSJT = staticmethod(nextPermutationSJT)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    

    
    
    

        
        
    

    
        

        
            
        

    
                

        

                
