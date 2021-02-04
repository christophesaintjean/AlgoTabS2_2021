import matplotlib.pyplot as plt
from time import time
from random import randint, seed
from statistics import mean

from CM3_triinsert import triinsert
from CM3_triselect import triselect
from CM4_trifusion import trifusion


algos = [triinsert, triselect, trifusion]
seed(13)

rep = 10
pmax = 12
N = [2**p for p in range(pmax)]


for algo in algos:
    tps_min, tps_mean, tps_max = [], [], [] 
    for n in N:
        tps_n = []
        for _ in range(rep):
            T = [randint(1, 10000) for _ in range(n)]
            debut = time()
            _ = algo(T)
            fin = time()
            tps_n.append(fin - debut)
        tps_min.append(min(tps_n))
        tps_mean.append(mean(tps_n))
        tps_max.append(max(tps_n))

    plt.fill_between(N, tps_min, tps_max, label=algo.__name__, alpha=0.5)
    plt.scatter(N, tps_mean)
plt.legend()
plt.xscale("log")
plt.show()