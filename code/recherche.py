# Td1 Exo 2

def recherche(T, req):
    for i in range(0, len(T)):
        if T[i] == req:
            return i
    return None

def recherche_in(T, req):
    return req in T

def recherche_index(T, req):
    return T.index(req)
    


if __name__ == "__main__":
    T  = [-3, 3, 5000, 0, 3, -1, 2]
    x = 5000
    print(recherche(T, x))
    print(recherche_in(T, x))
    print(recherche_index(T, x))