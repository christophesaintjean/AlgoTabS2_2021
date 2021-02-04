from random import randint, seed
from utils import estTrie

def trifusion(T):
    if len(T) > 1:
        ## Partitionnement
        G, D = partitionnement(T)
        
        ## Execution récursive
        G = trifusion(G)
        D = trifusion(D)
        return fusion(G, D, T)
    return T


def partitionnement(T):
    mil = len(T) // 2
    return T[:mil], T[mil:]


def fusion(G, D, T):
    i_t, i_g, i_d = 0, 0, 0
    while i_g < len(G) and i_d < len(D):
        if G[i_g] <= D[i_d]:  # On cherche le + petit
            T[i_t] = G[i_g]  # il est dans G
            i_g = i_g + 1
        else:
            T[i_t] = D[i_d]  # il est dans D
            i_d = i_d + 1
        i_t = i_t + 1

    while i_g < len(G):  # On termine G
        T[i_t] = G[i_g]
        i_t += 1
        i_g += 1

    while i_d < len(D):  # On termine D
        T[i_t] = D[i_d]
        i_t += 1
        i_d += 1
    return T

if __name__ == "__main__":
    seed(13)
    T = [randint(1, 100) for _ in range(10)]
    print(T)
    trifusion(T)
    print(T)

    seed(13)
    T = [randint(1, 100) for _ in range(3000)]
    print("Le tableau de 3000 éléments est trié:", estTrie(trifusion(T)))
