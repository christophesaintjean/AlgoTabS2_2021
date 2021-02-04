# Td3 Exo 2

from utils import estTrie
from time import time
from random import choice


def DichoRec(T, x, g=0, d=None):
    """ Recherche x dans T[g..d] """
    if d is None:
        d = len(T) - 1
    #print(f"[{g} : {d}]")
    if g <= d:
        m = (g+d) // 2
        if T[m] == x:
            return m
        elif x < T[m]:
            return DichoRec(T, x, g, m-1)
        else:
            return DichoRec(T, x, m+1, d)
    else:
        return None
    
if __name__ == "__main__":
    #T = [3, 4, 7, 8, 11, 12, 14, 17, 18]
    #x = 4
    #print(DichoRec(T, x))
    
    #for x in T:
    #    print(DichoRec(T, x))
    
    #x = 9
    #print(DichoRec(T, x))
    #x = 19
    #print(DichoRec(T, x))
    #x = 1
    #print(DichoRec(T, x))
    
    dico = []
    with open('dico.txt', 'r') as f:
        for ligne in f:
            dico.append(ligne.rstrip('\n'))
    dico = sorted(dico)
    print(estTrie(dico))
    
    rep = 50
    X = [choice(dico) for _ in range(rep)]
    
    debut = time()
    for x in X:
        _ = dico.index(x)
    fin = time()
    print(f"Durée: {fin - debut}")
    
    debut = time()
    for x in X:
        _ = DichoRec(dico, x)
    fin = time()
    print(f"Durée: {fin - debut}")
    
    
    
    