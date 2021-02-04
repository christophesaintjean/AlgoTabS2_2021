import matplotlib.pyplot as plt
from math import factorial

n = list(range(10, 30, 1))
#n = list(range(10, 50, 1))
#n = list(range(10, 150, 1))
deux_n = [2 * n_ for n_ in n]
cent_n = [100 * n_ for n_ in n]

n2 = [n_ ** 2 for n_ in n]
dix_n2 = [10 * n_ ** 2 for n_ in n]
cent_n2 = [100 * n_ ** 2 for n_ in n]

n3 = [n_ ** 3 for n_ in n]
cinq_n3 = [5 * n_ ** 3 for n_ in n]

#fact = [factorial(n_) for n_ in n]

plt.xlabel('n')
plt.ylabel('Ops')
plt.plot(n, n, '-b', label='n')
plt.plot(n, deux_n, ':b', label='2n')
plt.plot(n, cent_n, '-.b', label='100n')
plt.plot(n, n2, '-k', label='$n^2$')
plt.plot(n, dix_n2, ':k', label='$10n^2$')
plt.plot(n, cent_n2, '-.k', label='$100n^2$')
plt.plot(n, n3, '-r', label='$n^3$')
plt.plot(n, cinq_n3, ':r', label='$5n^3$')
#plt.plot(n, fact, '-k', label='n!')
plt.legend()
plt.show()
