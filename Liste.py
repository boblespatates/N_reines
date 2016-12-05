# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 14:48:42 2016

@author: emacedegastines
"""

class Liste():

    
    def construit(e, L):
        L.insert(0,e)
        return (L )

    def premierListe(L):
        return( L[0] )
    
    def resteListe(L):
        return(L[1:])
    
    def concatene(L1,L2):
        return(L1+L2)
        
    construit = staticmethod(construit)
    premierListe = staticmethod(premierListe)
    resteListe = staticmethod(resteListe)
    concatene = staticmethod(concatene)
