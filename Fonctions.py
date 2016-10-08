    # -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np


def parcoursEnProfondeur(n):
    L=np.zeros(n)
    a = parcoursEnProfondeurRec(L,0,n)
    if a:
        B=""
        for i in range(n-1):
            B+= "██"
        for i in range(n):
            p = 2*int(L[i])
            #print(C)
            print(B[:p] + "☺" + B[p:])
    
        


def parcoursEnProfondeurRec(L,i,n):
    c=0
    for j in range(int(L[i]),n):
        #pour arreter la récursion
        if c==1:
            return 1    
        #print(L,i,j)
        #teste si la reine menace une autre reine
        if j in L[0:i] or j - i in L[0:i] - np.linspace(0,i-1,i) or j - (n - i - 1) in L[0:i] - np.linspace(n-1,n-i,i):
            #si oui, déplace la reine vers la droite           
            continue
        #sinon, passe à la ligne suivante
        else :
            L[i] = j
            if i < n-1:
                c = parcoursEnProfondeurRec(L,i+1,n)
            #s'arrete si on a parcouru toute les lignes
            else :
                return 1
    #si une reine ne peut pas se placer sur une ligne, revient à la ligne précédente
    if c==1:
        return 1    
    if i > 0:
        L[i] = 0
    else :
        return 0
    

#dames(21)
def enregistre(L,n):
    G = np.zeros(n)
    for i in range(n):
        G[i] = abs(L[i])
    B=""
    for i in range(n-1):
        B+= "██"
    for i in range(n):
        p = 2*int(G[i])
        #print(C)
        print(B[:p] + "☺" + B[p:])
    
def test(L,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if  j!=i and abs(j - i) == abs(abs(L[j])-abs(L[i])):
                return False
    return True
    
def test2(L,n,i):
    for j in range(n):
        if  j!=i and abs(j - i) == abs(abs(L[j])-abs(L[i])):
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
    
#print ( test2([1,3,0,2] ,4,2) )           
forceBrute(4)
print( test([1,3,5,0,2,4],6) )
