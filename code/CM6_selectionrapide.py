from random import seed, randint

def pivot_median(T, g, d):
    i1, i2, i3 = [randint(g, d) for _ in range(3)]
    if T[i2] <= T[i1] <= T[i3]: return i1
    if T[i3] <= T[i1] <= T[i2]: return i1
    if T[i1] <= T[i2] <= T[i3]: return i2
    if T[i3] <= T[i2] <= T[i1]: return i2
    return i3

def partition(T, g, d, ipivot=None):
    if ipivot is None:
        ipivot = pivot_median(T, g, d)
    if ipivot < d:
        T[ipivot], T[d] = T[d], T[ipivot]
    
    pivot = T[d]
    i = g
    for j in range(g, d):
        if T[j] <= pivot:
            T[i], T[j] = T[j], T[i]
            i = i + 1
    T[i], T[d] = T[d], T[i]
    return i


def selectionrapide(T, g=0, d=None, k=0):
    """ Selection rapide du k-ieme element dans T[g..d]"""
    if d is None:
        d = len(T)-1
    ipivot = partition(T, g, d)
    if ipivot == k:  return T[k]
    if k < ipivot:  
        return selectionrapide(T, g, ipivot-1, k)
    else:
        return selectionrapide(T, ipivot+1, d, k)
    
if __name__ == "__main__":
    k = 3
    T = [1, 5, 2, -1, 2, 7, 2, 5, 9, -4, 2, 13, -2, 5, 2]
    print(selectionrapide(T, k=k))