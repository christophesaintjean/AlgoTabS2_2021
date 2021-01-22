import matplotlib.pyplot as plt

allocated = [0]
for size in range(1, 10**5):
    if size <= allocated[-1]:
        allocated.append(allocated[-1])
    else:
        newsize  = size + size // 8
        if size < 9:
            allocated.append(newsize+3)
        else:
            allocated.append(newsize+6)
plt.figure()            
plt.plot(allocated)
plt.show()