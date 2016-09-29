    # -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

import numpy as np

def dames(n):
    L=np.zeros(n)
    a = damesRec(L,0,n)
    if a:
        B=""
        for i in range(n-1):
            B+= "██"
        for i in range(n):
            p = 2*int(L[i])
            #print(C)
            print(B[:p] + "☺" + B[p:])
    
        


def damesRec(L,i,n):
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
                c = damesRec(L,i+1,n)
            #s'arrete si on a parcouru toute les lignes
            else :
                return 1
    #si une reine ne peut pas se placer sur une ligne, revient à la ligne précédente
    if c==1:
        return 1    
    if i > 0:
        L[i] = 0
        """
        L[i-1]+= 1
        L[i] = 0
        return damesRec(L, i-1,n)"""
    else :
        return 0
    
""" if L [i] > n-1:
        if i > 0:
            L[i-1]+= 1
            L[i] = 0
            return damesRec(L, i-1,n)
        else :
            return 0
    elif L[i] in L[0:i] or L[i] - i in L[0:i] - np.linspace(0,i-1,i) or L[i] - (n - i - 1) in L[0:i] - np.linspace(n-1,n-i,i):
        L[i]+= 1
        return damesRec(L,i,n)
    else :
        if i < n-1:
            return damesRec(L,i+1,n)
        else :
            return L"""

