from time import time
from random import randint
import matplotlib.pyplot as plt
from tqdm.gui import tqdm

def diss(a, b):
    return abs(a-b)


def plus_proche(T, ref, diss):
    i_min = 0
    d_min = diss(ref, T[i_min])
    if d_min == 0:
        return i_min
    for i in range(1, len(T)):
        d_i = diss(ref, T[i])
        if d_i == 0:
            return i
        if d_i < d_min:
            d_min = d_i
            i_min = i
    return i_min

def tps_plus_proche(n):
    T = []
    for _ in range(n):
        T.append(randint(0, n))
    ref = randint(0, n)
    #ref = -1    # a tester
    
    debut = time()
    _ = plus_proche(T, ref, diss)
    fin = time()
    duree = fin - debut
    return duree


if __name__ == "__main__":
    #print(diss(3, 3), diss(3, 4), diss(3, 2))
    T  = [3, 5, 0, 3, -1, 2]
    ref = -2
    print(plus_proche(T, ref, diss))
    
    n = 10 # petite
    T = []
    for _ in range(n):
        T.append(randint(0, n))
    ref = randint(0, n)
    
    debut = time()
    _ = plus_proche(T, ref, diss)
    fin = time()
    duree = fin - debut
    print("Duree (petit): ", duree)
    
    n = 1000 # moyen
    T = []
    for _ in range(n):
        T.append(randint(0, n))
    ref = randint(0, n)
    
    debut = time()
    _ = plus_proche(T, ref, diss)
    fin = time()
    duree = fin - debut
    print("Duree (moyen): ", duree)
        
    
    n = 100000 # grand
    T = []
    for _ in range(n):
        T.append(randint(0, n))
    ref = randint(0, n)
    
    debut = time()
    _ = plus_proche(T, ref, diss)
    fin = time()
    duree = fin - debut
    print("Duree (grand): ", duree)
    
    print(f"Duree (grand): {tps_plus_proche(n)}")
    
    N = []
    Tps = []
    for n in tqdm(range(10, 10**5, 200)):
        N.append(n)
        # calcul
        Tps.append(tps_plus_proche(n))
        
    #affichage de la courbe N vs Tps
    plt.figure()
    plt.plot(N, Tps)
    plt.show()
    
        
    
    
    

    
    
    

