import random as ran
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import math as m


#con formula teorica

p=float(input("Ingrese el valor de p: "))
x=[]

for i in range(500):
    acu=0
    tr=1
    b=np.exp(-p)
    r=ran.uniform(0,1)
    tr=tr*r
    while((tr-b)>=0):
        acu+= 1
        r=ran.uniform(0,1)
        tr=tr*r
    x.append(acu)

print("La media es: ",
"%.2f" % np.mean(x))
print("La varianza es: ",
"%.2f" % np.var(x))
print("La desviacion estandar es: ",
"%.2f" % m.sqrt(np.var(x)))

plt.title("Distribucion Poisson")
plt.hist(x, bins=100, alpha=0.5,
weights=np.zeros_like(x)+1./len(x),
edgecolor="black", linewidth=1.3)


#con la funcion incluida en python

poisson = sp.poisson(p)
w = np.arange(poisson.ppf(0.01),
                poisson.ppf(0.99))
fmp = poisson.pmf(w) 
plt.plot(w, fmp)
plt.vlines(w, 0, fmp, colors='b',
            lw=5, alpha=0.5)



y = np.random.poisson(p, 1000)
plt.hist(y,alpha=0.7, bins=100,
weights=np.zeros_like(y)+1./len(y),
edgecolor='black')
plt.ylabel("frequencia")
plt.xlabel("valores")
plt.title("Histograma Poisson")
plt.show()

print("La media es: ",
"%.2f" % np.mean(y))
print("La varianza es: ",
"%.2f" % np.var(y))
print("La desviacion estandar es: ",
"%.2f" % m.sqrt(np.var(y)))