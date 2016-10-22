    # -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np




def enregistre(L,n):
    G = np.zeros(n)
    for i in range(n):
        G[i] = abs(L[i])
    B=""
    for i in range(n-1):
        B+= "██"
    for i in range(n):
        p = 2*int(G[i])
        print(B[:p] + "☺" + B[p:])
    print("*********************************************************************")
    
def test(L,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if  j!=i and abs(j - i) == abs(abs(L[j])-abs(L[i])):
                return False
    return True




def test2(L,n,i):
    for j in range(n):
        if  j!=i and ( L[j] == L[i] or abs(j - i) == abs(abs(L[j])-abs(L[i])) ):
            return False
    return True
    
def nextPermutationSJT(L,n):
    for j in range(n-1,-1,-1)    : 
        for i in range(n):
             #cherche le plus grand élément, 
            if L[i] == j or L[i] == -j:
                p = i
                break
        #vérifie la possibilité d'un décalage à gauche
        if L[p]>0 and p>0 and abs(L[p-1]) < abs(L[p]):
            (L[p],L[p-1]) = (L[p-1], L[p])
            return (True,p,p-1)
        #vérifie la possibilité d'un décalage à droite        
        if L[p]<0 and p<n-1 and abs(L[p+1]) < abs(L[p]):
            (L[p],L[p+1]) = (L[p+1], L[p])
            return (True,p,p+1)
        #si le décalage n'est pas possible, change la direction
        L[p] = -L[p]
    return (False,0,0)
            
def forceBrute(n):
    isPermutation = True
    L = np.linspace(0,n-1,n)
    c=0
    if test(L,n):
        enregistre(L,n)
    while isPermutation:
        resultat = nextPermutationSJT(L,n)
        isPermutation = resultat[0]
        #if isPermutation and test2(L,n,resultat[1]) and test2(L,n,resultat[2]):
        if isPermutation and test(L,n):
            c+=1
            #enregistre(L,n)
            #print("*************************************************")
    print(c)
    
def parcoursEnProfondeur(n):
    L = np.zeros(n)
    print( parcoursEnProfondeurRec(L, 0, n, 0) )


def parcoursEnProfondeurRec(L, i, n, compteur):
    for j in range(n):
        L[i] = j
        if not test2(L, i + 1, i): 
            #si oui, déplace la reine vers la droite           
            continue
        #sinon, passe à la ligne suivante
        else :
            if i < n - 1:
                compteur = parcoursEnProfondeurRec(L, i + 1, n, compteur)
            #enregistre la solution car on a parcouru toute les lignes
            else :
                enregistre(L, n)
                compteur += 1
    #si une reine ne peut pas se placer sur une ligne, revient à la ligne précédente
    return compteur
    
def parcoursEnLargeur(n):
    print( parcoursEnLargeurRec([[]], 0, n) )
    
def parcoursEnLargeurRec(collection, i, n):
    nouvelleCollection = []
    #parcourt la collection des solutions partielles
    for L in collection:
        #pour chaque solution partielle, vérifie si l'ajout d'une reine marche toujours
        for j in range(n):
            print(L)
            L.append(j)
            if test2(L, i + 1, i):
                #Si l'ajout d'une reine marche, l'ajoute a la collection
                print(L, i)
                nouvelleCollection.append( list(L) )
            L.pop(i)
    #Si on n'est pas encore à la dernière ligne, ajoute une nouvelle reine
    if i < n-1:
        return parcoursEnLargeurRec(nouvelleCollection, i+1, n) 
    #Sinon, enregistre toute les solutions
    for L in nouvelleCollection:
        enregistre(L, n)
    return len( nouvelleCollection )
        
parcoursEnProfondeur(8)

