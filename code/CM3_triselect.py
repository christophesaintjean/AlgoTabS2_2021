from random import randint, seed
from utils import estTrie


def triselect(T):
    """
    Version en place
    """
    for i in range(len(T)-1):
        # print(T[0:i], T[i:])
        imin = i
        for j in range(i+1, len(T)):
            if T[j] <= T[imin]:
                imin = j
        if imin != i:
            T[i], T[imin] = T[imin], T[i]
    return T


def triselect2(T):
    """
    Autre version
    """
    res = []
    while len(T) > 0:
        imin = 0
        for i in range(1, len(T)):
            if T[i] < T[imin]:
                imin = i
        res.append(T[imin])
        del T[imin]
    return res

if __name__ == "__main__":
    seed(13)
    T = [randint(1, 100) for _ in range(10)]
    print(T)
    triselect(T)
    print(T)

    seed(13)
    T = [randint(1, 100) for _ in range(3000)]
    print("Le tableau de 3000 éléments est trié:", estTrie(triselect(T)))
    
    seed(13)
    T = [randint(1, 100) for _ in range(10)]
    print(T)
    T = triselect2(T)
    print(T)

    seed(13)
    T = [randint(1, 100) for _ in range(3000)]
    print("Le tableau de 3000 éléments est trié:", estTrie(triselect2(T)))



