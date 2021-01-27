def estTrie(T, deb=0, fin=None):
    if fin is None:
        fin = len(T)
    for i in range(deb, fin-1):
        if T[i] > T[i + 1]:
            return False
    return True

if __name__ == "__main__":
    T_trie = [1, 4, 6, 9]
    T_nontrie = [1, 6, 4, 9]
    print(estTrie(T_trie), estTrie(T_nontrie))
    print(estTrie([]), estTrie([3]))
    T2 = [4, 5, 3, 6, 7, -3, 2, 5]
    print(estTrie(T2))         # False
    print(estTrie(T2, 0, 2), estTrie(T2, fin=2)) 
    print(estTrie(T2, 2, 5))   # True
    print(estTrie(T2, 2, 6))   # False
    print(estTrie(T2, 5, 8), estTrie(T2, 5))
    
    
    
    
    


    