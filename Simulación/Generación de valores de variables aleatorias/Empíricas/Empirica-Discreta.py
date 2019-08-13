import random
import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
fa = [0.1,0.2,0.4,0.6,0.7,0.8,
        0.85,0.9,0.95,1]

arreglo = []

for i in range(10):
    arreglo.append(1)
    arreglo.append(2)
    arreglo.append(6)
    arreglo.append(5)

for i in range(20):
    arreglo.append(3)
    arreglo.append(4)

for i in range(5):
    arreglo.append(7)
    arreglo.append(8)
    arreglo.append(9)
    arreglo.append(10)

valores = []
for i in range(1000):
    r = random.uniform(0,1)
    c = 0
    b = True
    while (b):
        if (r<=fa[c]):
            valores.append(x[c])
            b = False
        else:
            c += 1

plt.hist(valores,bins=len(valores),
edgecolor ='green',linewidth = 7,
color = 'green',
weights=np.zeros_like(valores)+1. /len(arreglo),
label = 'Metodo')
plt.legend()
plt.show()
