import random as ran
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import math as m

#con formula teorica

n=int(input("Ingrese nº eventos \"n\": "))
p=float(input("Ingrese la prob. \"p\": "))

x=[]

for i in range(1000):
    prob=0
    for j in range(n):
        r=ran.uniform(0,1)
        if((r-p) <= 0):
            prob+= 1
    x.append(prob)

print("La media es: ",
"%.2f" % np.mean(x))
print("La varianza es: ",
"%.2f" % np.var(x))
print("La desviacion estandar es: ",
"%.2f" % m.sqrt(np.var(x)))

plt.title("Distribucion Binomial")
plt.hist(x, bins=100,
weights=np.zeros_like(x)+1./len(x),
alpha=0.5,edgecolor="black", linewidth=1.3)

#con la funcion incluida en python

valores = sp.binom.rvs(n, p, size=1000)
print("La media es: ",
"%.2f" % np.mean(valores))
print("La varianza es: ",
"%.2f" % np.var(valores))
print("La desviacion estandar es: ",
"%.2f" % m.sqrt(np.var(valores)))
plt.hist(valores, bins=100,
weights=np.zeros_like(x)+1./len(x),
alpha=0.3,edgecolor="black", linewidth=1)
plt.title('Distribución Binomial')

b = sp.binom(n, p) # Distribucion
x = np.arange(b.ppf(0.01),
              b.ppf(0.99))
fmp = b.pmf(x) # Funcion de Probabilidad
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5,
            alpha=0.5)
plt.show()



