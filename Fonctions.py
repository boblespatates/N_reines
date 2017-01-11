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
    
    
    def test3( matriceDeCollision, i, n):
        '''teste le nombre de placements viables sur la i-ème ligne
        - matriceDeCollision : matrice indiquant les cases menacées où occupées par une dame
        - i : ligne où compter le nombre de placements viables
        - n : taille de l'échiquier'''
        compteur = 0
        for k in range(n):
            if ( matriceDeCollision[i][k] == 1 ) :
                compteur = compteur + 1
        return compteur
        
    def test4( permutation, L, i):
        ''' teste les conflits d'une permutation sur la i-ème ligne
        - permutation : permutation à vérifier
        - L : liste des indices dans l'ordre de remplissage
        - i : nombre de lignes remplies'''
        for k in range(i):
            if  int(L[k]) != int(L[i]) and ( permutation[ int(L[k]) ] == permutation[ int(L[i]) ] or abs( int(L[k]) - int(L[i]) ) == abs( abs( permutation[ int(L[k]) ] )-abs( permutation[ int(L[i]) ] ) ) ): #int car probleme de float     
                return False
        return True
    
    def miseAJourCollisions( i, j, matriceCollision, n ):
        ''' met à jour la matrice de collision M selon L sachant que une dame en (i,j) a été ont été ajoutée
        - listePermutation : permutation actuelle
        - i,j coordonnées de la nouvelle dame
        - matriceCollision : matrice de transposition
        - n : taille de l'échiquier'''
        for k in range(n):
            matriceCollision[k][j] = 1
            matriceCollision[i][k] = 1
            if ( j - i + k >= 0 ) and  (j - i + k < n):
                matriceCollision[k][j-i+k] = 1
            if ( j + i - k >= 0 ) and  (j + i - k < n):
                matriceCollision[k][j+i-k] = 1
        
        
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
                return True
            #vérifie la possibilité d'un décalage à droite        
            if permutation[p] < 0 and p < n - 1 and abs( permutation[p + 1] ) < abs( permutation[p] ):
                ( permutation[p], permutation[p + 1] ) = ( permutation[p + 1], permutation[p] )
                return True
            #si le décalage n'est pas possible, change la direction
            permutation[p] = -permutation[p]
        return False
    
    test = staticmethod(test)
    test2 = staticmethod(test2)
    test3 = staticmethod(test3)
    test4 = staticmethod(test4)
    miseAJourCollisions = staticmethod(miseAJourCollisions)
    nextPermutationSJT = staticmethod(nextPermutationSJT)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



    

    
    
    

        
        
    

    
        

        
            
        

    
                

        

                
