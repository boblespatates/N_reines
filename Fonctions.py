    # -*- coding: utf-8 -*-


import numpy as np

class Fonctions:
    
    ''' classe de fonctions statiques pour calculer les solutions '''
    
    
    def enregistre(listePermutation,n):
        '''Enregistre la solution dans un fichier texte
        - listePermutation : permutation à afficher
        - n : taille de l'échiquier'''
        # pour l'instant, l'affiche
        G = np.zeros(n)
        # copie la solution
        for i in range(n):
            G[i] = abs(listePermutation[i])
        #affiche la solution (ascii)
        B=""
        for i in range(n-1):
            B+= "██"
        for i in range(n):
            p = 2*int(G[i])
            print(B[:p] + "☺" + B[p:])
        print("*************************************************")

        
    def test(listePermutation,n):
        ''' vérifie que la permutation est solution
        - listePermutation : permutation à vérifier
        - n : taille de l'échiquier
        - i : ligne à vérifier'''
        for i in range(n-1):
            for j in range(i+1,n):
                if  j!=i and abs(j - i) == abs(abs(listePermutation[j])-abs(listePermutation[i])):
                    return False
        return True
        
    def test2(listePermutation,n,i):
        ''' teste les conflits d'une permutation sur la i-ème ligne 
        - listePermutation : permutation à vérifier
        - n : taille de l'échiquier
        - i : ligne à vérifier'''
        for j in range(n):
            if  j!=i and ( L[j] == L[i] or abs(j - i) == abs(abs(L[j])-abs(L[i])) ):
                return False
        return True
    
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
            

        
    def nextPermutationSJT(listePermutation,n):
        ''' pour une permutation donnée, calcule la permutation suivante selon l'algorithme de Steinhaus–Johnson–Trotter.
        Il faut que la direction soit précisée (nombre positif: direction vers la gauche, nombre négatif: direction vers la droite) 
        - listePermutation : permutation actuelle
        - n : taille de l'échiquier'''
        #cherche le plus grand élément, 
        for j in range(n-1,-1,-1): 
            for i in range(n):
                if listePermutation[i] == j or listePermutation[i] == -j:
                    p = i
                    break
            #vérifie la possibilité d'un décalage à gauche
            if listePermutation[p]>0 and p>0 and abs(listePermutation[p-1]) < abs(listePermutation[p]):
                (listePermutation[p],listePermutation[p-1]) = (listePermutation[p-1], listePermutation[p])
                return (True,p,p-1)
            #vérifie la possibilité d'un décalage à droite        
            if listePermutation[p]<0 and p<n-1 and abs(listePermutation[p+1]) < abs(listePermutation[p]):
                (listePermutation[p],listePermutation[p+1]) = (listePermutation[p+1], listePermutation[p])
                return (True,p,p+1)
            #si le décalage n'est pas possible, change la direction
            listePermutation[p] = -listePermutation[p]
        return (False,0,0)
                
    def forceBrute(n):
        ''' parcourt les permutations, vérifie si elles sont solutions
        - n : taille de l'échiquier '''
        # variable testant si l'algorithme de permutations est arrivé à terme (True: l'algorithme n'est pas terminé, False: toutes les      permutations ont été parcourues
        isPermutation = True
        #initialise la première permutation
        listePermutation = np.linspace(0,n-1,n)
        compteur=0
        if test(listePermutation,n):
            enregistre(listePermutation,n)
        #parcourt les permutations
        while isPermutation:
            #calcul de la permutation suivante
            resultat = nextPermutationSJT(listePermutation,n)
            isPermutation = resultat[0]
            # si la permutation est solution, l'enregistre
            if isPermutation and test(listePermutation,n):
                compteur+=1
                enregistre(listePermutation,n)
        #affiche le nombre de solutions
        print(compteur)
        

