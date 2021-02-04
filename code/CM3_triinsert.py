from random import randint, seed
from utils import estTrie

def triinsert(T):
    for i in range(1, len(T)):
        cle = T[i]
        j = i - 1
        # print(T[:i])
        while j >= 0 and T[j] > cle:
            T[j+1] = T[j]
            j = j - 1
        T[j+1] = cle
    return T

if __name__ == "__main__":
    seed(13)
    T = [randint(1, 100) for _ in range(10)]
    print(T)
    triinsert(T)
    print(T)

    seed(13)
    T = [randint(1, 100) for _ in range(3000)]
    print("Le tableau de 3000 éléments est trié:", estTrie(triinsert(T)))
