import random
import matplotlib.pyplot as plt
import numpy as np

z = [1.3,1.8,2.3,2.8,3.3,3.8,4.3,
    4.8,5.3,5.8,6.3]
fra = [0.1,0.25,0.35,0.45,0.6,0.75,
        0.8,0.95,1]
a = 0
b = 0
arreglo = []

for i in range(1000):
    cont = 0
    flag = True

    r1 = random.uniform(0,1)
    while (flag):
        if (r1 >= fra[cont]):
            cont += 1
        else:
            a = z[cont]
            b = z[cont+1]
            flag = False
    r2 = random.uniform(0,1)
    x = a + (b-a)*r2
    arreglo.append(x)

print("E",np.mean(arreglo))
print("V",np.var(arreglo))
plt.hist(arreglo,bins=9,
    linewidth=0.2,edgecolor='pink')
plt.show()