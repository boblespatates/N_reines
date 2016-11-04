    # -*- coding: utf-8 -*-


import numpy as np

#class Fonctions:
    
''' classe de fonctions statiques pour calculer les solutions '''



    
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



def parcoursEnProfondeurRec(permutation, i, n):
    ''' fonction récursive pour le parcours en profondeur
    - permutation : solution partielle étudiée
    - i : nombre de ligne déjà remplies à l'entrée de la fonction
    - n : taille de l'échiquier
    - compteur : compte le nombre de solutions '''
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
    
    

def parcoursEnProfondeur( n ):
    ''' parcourt le graphe en profondeur pour chercher les solutions
    - n : taille de l'échiquier '''
    permutation = np.zeros( n )
    return( parcoursEnProfondeurRec( permutation, 0, n) )

    
    
def parcoursEnLargeurRec( listeSolution, i, n ):
    ''' fonction récursive pour le parcours en largeur
    - collection : liste de solutions partielles 
    - i : nombre de ligne déjà remplies à l'entrée de la fonction 
    - n : taille de l'échiquier '''
    nouvelleListeSolution = []
    #parcourt la collection des solutions partielles
    for L in listeSolution:
        #pour chaque solution partielle, vérifie si l'ajout d'une reine marche toujours
        for j in range( n ):
            L.append( j )
            if test2( L, i + 1, i ):
                #Si l'ajout d'une reine marche, l'ajoute a la collection
                nouvelleListeSolution.append( list(L) )
            L.pop(i)
    #Si on n'est pas encore à la dernière ligne, ajoute une nouvelle reine
    if i < n - 1:
        return parcoursEnLargeurRec( nouvelleListeSolution, i + 1, n ) 

    return listeSolution


    
def parcoursEnLargeur(n):
    ''' parcourt le graphe en largeur pour chercher les solutions
    - n : taille de l'échiquier '''
    return( parcoursEnLargeurRec( [[]], 0, n ) )
    
        
    
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

            
def forceBrute(n):
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
        isCollision = test( permutation, n )
    return isCollision
            
    
    
def forceBruteAmelioree( n ):
    ''' même principe que force brute, retient la matrice des collisions pour une verication plus rapide de la permutation (la permutation suivante différant seulement d'une transposition)
    - n : taille de l'échiquier '''
    listeSolution = []
    # variable testant si l'algorithme de permutations est arrivé à terme (True: l'algorithme n'est pas terminé, False: toutes les      permutations ont été parcourues
    isPermutation = True
    #matrice de coillision : la i-ème ligne ou colonne correspond à la i-ème dame. A_ij = 1 si les dames i et j sont en collison, 0 sinon.
    matriceCollision = np.ones( ( n, n ) )
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
        if miseAJourCollisions( permutation, resultat[1], resultat[2], matriceCollision, n ):
            permutationPositive = [ abs(x) for x in permutation ]
            listeSolution.append(permutationPositive)
    return(listeSolution)
                
print(forceBruteAmelioree(5))
