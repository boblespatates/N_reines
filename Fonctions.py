    # -*- coding: utf-8 -*-


import numpy as np

#class Fonctions:
    
''' classe de fonctions statiques pour calculer les solutions '''



def enregistre( listePermutation, n ):
    '''Enregistre la solution dans un fichier texte
    - listePermutation : permutation à afficher
    - n : taille de l'échiquier '''
    # pour l'instant, l'affiche
    G = np.zeros( n )
    # copie la solution
    for i in range( n ):
        G[i] = abs( listePermutation[i] )
    #affiche la solution (ascii)
    B=""
    for i in range( n - 1 ):
        B += "██"
    for i in range(n):
        p = 2 * int( G[i] )
        print( B[:p] + "☺" + B[p:] )
    print( "*************************************************" )


    
def test( listePermutation, n ):
    ''' vérifie que la permutation est solution
    - listePermutation : permutation à vérifier
    - n : taille de l'échiquier
    - i : ligne à vérifier '''
    for i in range( n - 1 ):
        for j in range( i + 1, n ):
            if  j != i and abs( j - i ) == abs( abs( listePermutation[j] )-abs( listePermutation[i] ) ):
                return False
    return True


    
def test2( listePermutation, n, i ): # la fonction marche aussi si on a pas une permutation
    ''' teste les conflits d'une permutation sur la i-ème ligne 
    - listePermutation : permutation à vérifier
    - n : taille de l'échiquier
    - i : ligne à vérifier '''
    for j in range( n ):
        if  j != i and ( listePermutation[j] == listePermutation[i] or abs( j - i ) == abs( abs( listePermutation[j] )-abs( listePermutation[i] ) ) ):
            return False
    return True



def parcoursEnProfondeurRec(listePermutation, i, n, compteur):
    ''' fonction récursive pour le parcours en profondeur
    - listePermutation : solution partielle étudiée
    - i : nombre de ligne déjà remplies à l'entrée de la fonction
    - n : taille de l'échiquier
    - compteur : compte le nombre de solutions '''
    for j in range( n ):
        listePermutation[i] = j
        if not test2( listePermutation, i + 1, i ): 
            #si oui, déplace la reine vers la droite           
            continue
        #sinon, passe à la ligne suivante
        else :
            if i < n - 1:
                compteur = parcoursEnProfondeurRec( listePermutation, i + 1, n, compteur )
            #enregistre la solution car on a parcouru toute les lignes
            else :
                enregistre( listePermutation, n )
                compteur += 1
    #si une reine ne peut pas se placer sur une ligne, revient à la ligne précédente
    return compteur
    
    

def parcoursEnProfondeur( n ):
    ''' parcourt le graphe en profondeur pour chercher les solutions
    - n : taille de l'échiquier '''
    L = np.zeros( n )
    print( parcoursEnProfondeurRec( L, 0, n, 0 ) )

    
    
def parcoursEnLargeurRec( collection, i, n ):
    ''' fonction récursive pour le parcours en largeur
    - collection : liste de solutions partielles 
    - i : nombre de ligne déjà remplies à l'entrée de la fonction 
    - n : taille de l'échiquier '''
    nouvelleCollection = []
    #parcourt la collection des solutions partielles
    for L in collection:
        #pour chaque solution partielle, vérifie si l'ajout d'une reine marche toujours
        for j in range( n ):
            L.append( j )
            if test2( L, i + 1, i ):
                #Si l'ajout d'une reine marche, l'ajoute a la collection
                nouvelleCollection.append( list(L) )
            L.pop(i)
    #Si on n'est pas encore à la dernière ligne, ajoute une nouvelle reine
    if i < n - 1:
        return parcoursEnLargeurRec( nouvelleCollection, i + 1, n ) 
    #Sinon, enregistre toute les solutions
    for L in nouvelleCollection:
        enregistre( L , n )
    return len( nouvelleCollection )


    
def parcoursEnLargeur(n):
    ''' parcourt le graphe en largeur pour chercher les solutions
    - n : taille de l'échiquier '''
    print( parcoursEnLargeurRec( [[]], 0, n ) )
    
        
    
def nextPermutationSJT(listePermutation, n):
    ''' pour une permutation donnée, calcule la permutation suivante selon l'algorithme de Steinhaus–Johnson–Trotter.
    Il faut que la direction soit précisée (nombre positif: direction vers la gauche, nombre négatif: direction vers la droite) 
    - listePermutation : permutation actuelle
    - n : taille de l'échiquier '''
    #cherche le plus grand élément, 
    for j in range(n-1, -1, -1): 
        for i in range(n):
            if listePermutation[i] == j or listePermutation[i] == -j:
                p = i
                break
        #vérifie la possibilité d'un décalage à gauche
        if listePermutation[p] > 0 and p > 0 and abs( listePermutation[p - 1] ) < abs( listePermutation[p] ):
            ( listePermutation[p], listePermutation[p - 1] ) = ( listePermutation[p - 1], listePermutation[p] )
            return ( True, p , p - 1 )
        #vérifie la possibilité d'un décalage à droite        
        if listePermutation[p] < 0 and p < n - 1 and abs( listePermutation[p + 1] ) < abs( listePermutation[p] ):
            ( listePermutation[p], listePermutation[p + 1] ) = ( listePermutation[p + 1], listePermutation[p] )
            return ( True, p, p + 1 )
        #si le décalage n'est pas possible, change la direction
        listePermutation[p] = -listePermutation[p]
    return ( False, 0, 0 )

            
def forceBrute(n):
    ''' parcourt les permutations, vérifie si elles sont solutions
    - n : taille de l'échiquier '''
    # variable testant si l'algorithme de permutations est arrivé à terme (True: l'algorithme n'est pas terminé, False: toutes les      permutations ont été parcourues
    isPermutation = True
    #initialise la première permutation
    listePermutation = np.linspace( 0, n - 1, n )
    compteur = 0
    if test( listePermutation, n ):
        enregistre( listePermutation, n )
    #parcourt les permutations
    while isPermutation:
        #calcul de la permutation suivante
        resultat = nextPermutationSJT( listePermutation, n )
        isPermutation = resultat[0]
        # si la permutation est solution, l'enregistre
        if isPermutation and test( listePermutation, n ):
            compteur += 1
            #enregistre( listePermutation, n )
	    print(listePermutation)    

    #affiche le nombre de solutions
    #print( compteur )
    
    
def miseAJourCollisions( listePermutation, i, j, matriceCollision, n ):
    ''' met à jour la matrice de collision M selon L sachant que les dames i et j ont été permutées
    - listePermutation : permutation actuelle
    - i : première dame déplacée
    - j : deuxième dame déplacée
    - matriceCollision : matrice de transposition
    - n : taille de l'échiquier'''
    #True si il n'y a pas de collisions sur les deux dames interverties, False sinon        
    isCollision = True
    for k in range(n):
        if  k != i  and abs( k - i ) == abs( abs( listePermutation[k] )-abs( listePermutation[i] ) ) :
            isCollision = False
            matriceCollision[k][i] = 1
            matriceCollision[i][k] = 1
        else:
            matriceCollision[k][i] = 0
            matriceCollision[i][k] = 0
        if  k != j  and abs( k - j ) == abs( abs( listePermutation[k] )-abs( listePermutation[j] ) ) :
            isCollision = False
            matriceCollision[k][j] = 1
            matriceCollision[j][k] = 1
        else:
            matriceCollision[k][j] = 0
            matriceCollision[j][k] = 0
    if isCollision:
        #s'il n'y a pas de nouvelles collisions, teste toute la matrice
        isCollision = test( listePermutation, n )
    return isCollision
            
    
    
def forceBruteAmelioree( n ):
    ''' même principe que force brute, retient la matrice des collisions pour une verication plus rapide de la permutation (la permutation suivante différant seulement d'une transposition)
    - n : taille de l'échiquier '''
    # variable testant si l'algorithme de permutations est arrivé à terme (True: l'algorithme n'est pas terminé, False: toutes les      permutations ont été parcourues
    isPermutation = True
    #matrice de coillision : la i-ème ligne ou colonne correspond à la i-ème dame. A_ij = 1 si les dames i et j sont en collison, 0 sinon.
    matriceCollision = np.ones( ( n, n ) )
    #initialise la première permutation
    listePermutation = np.linspace( 0, n - 1, n )
    compteur = 0
    if test( listePermutation, n ):
        enregistre( listePermutation, n )
    #parcourt les permutations
    while isPermutation:
        #calcul de la permutation suivante
        resultat = nextPermutationSJT( listePermutation, n )
        isPermutation = resultat[0]
        # si la permutation est solution, l'enregistre
        if miseAJourCollisions( listePermutation, resultat[1], resultat[2], matriceCollision, n ):
            compteur += 1
            enregistre( listePermutation, n )
    #affiche le nombre de solutions
    print( compteur )
                
