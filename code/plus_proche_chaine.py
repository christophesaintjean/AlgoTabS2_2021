# TP1 Exo 3
from supp_tp1 import levenshteinDistance as levDist
from plus_proche import plus_proche

def diss(s1, s2):
    d = levDist(s1, s2)
    return d["distance"]
    
    
if __name__ == "__main__":
    dico = []
    with open('dico.txt', 'r') as f:
        for ligne in f:
            dico.append(ligne.rstrip('\n'))
    while True:
        m = input("Entrez un mot ? ")
        if not m:
            break
        i_min = plus_proche(dico, m, diss)
        print(f"Le plus proche est: {dico[i_min]}")
    


