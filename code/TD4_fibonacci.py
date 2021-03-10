import math


def fib1(n):
    """
    Calcul Fn, le n-ième élément de la suite de Fibonacci
    (par récursion initiale)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib1(n-1) + fib1(n-2)
    
    
def fib_tab(n):
    """F[i] répresente la valeur de Fi (pré-allocation de F)"""
    if n == 0:
        return 0
    F = [0] * (n+1)
    F[1] = 1
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]
    return F[n]

def fib_tab_append(n):
    """F[i] répresente la valeur de Fi (sans pré-allocation de F)"""
    F = [0, 1]
    for i in range(2, n+1):     # calcul de F[i]
        F.append(F[i-1] + F[i-2])
    return F[n]

def fib_tab_append2(n):
    """F[i] répresente la valeur de Fi (sans pré-allocation de F)"""
    F = [0, 1]
    for _ in range(2, n+1):
        F.append(F[-1] + F[-2])
    return F[n]

def fib2(n, i=2, Fim1=1, Fim2=0):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif i == n:
        return Fim1 + Fim2
    else:
        return fib2(n, i+1, Fim1 + Fim2, Fim1)
    
def fib_iter(n, i=2, Fim1=1, Fim2=0):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    i=2
    Fim1, Fim2 = 1, 0
    while i < n:
        i = i + 1
        Fim1, Fim2 = Fim1 + Fim2, Fim1
    return Fim1 + Fim2

def fib_binet(n):
    phi = (1 + math.sqrt(5)) / 2
    phip = (1 - math.sqrt(5)) / 2
    return (phi**n - phip**n)/math.sqrt(5)

if __name__ == "__main__":
    n = 5
    n2 = 1000
    #print(fib1(n2))
    print(fib_tab(n2))
    print(fib_tab_append(n2))
    print(fib_tab_append2(n2))
    print(fib2(n2))
    print(fib_binet(n2))
    print(int(fib_binet(n2)) == fib2(n2))
    