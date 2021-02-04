# Td2 Exo 2

def chaines_egales(s1, s2):
    """
    Egalité de chaines de même longueur.
    """
    i = 0
    while i < len(s1):
        if s1[i] != s2[i]:
            return False
        i += 1
    return True

def rechercheSousChaine(S, req):
    """
    Existence d'une sous-chaine req dans une chaine s
    """
    n, m = len(S), len(req)
    for i in range(n-m+1):
        if chaines_egales(S[i:i+m], req):
            return True   # on peut aussi retourner i si on veut la position
    return False
    
 
if __name__ == "__main__":
   
    
    S = "Le petit chat"
    req = "chat"
    print(rechercheSousChaine(S, req))
    
    S = [0,1,20,3,14,5]
    req = [20, 3, 14]
    print(rechercheSousChaine(S, req))
    
    
    S = "a"*10**5 + "b"
    req = "a"*10**2 + "b"   # m * (n-m+1) ~  m * n
    print(rechercheSousChaine(S, req))
    