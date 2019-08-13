import random as ran
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import math as m

#procedimiento del limite central

x=[]
u=0.0
sigma=0.0

u=float(input("Ingrese media: "))
sigma=float(input("Ingrese desviacion: "))

#eligiendo el valor de K resulta...
k = int(input("Ingrese valor de K:"))
for i in range(1000):
    sum = 0.0
    for j in range(k):
        r = ran.uniform(0,1)
        sum += r
    x.append(round(sigma * ((12/k)**(1/2)) * 
            (sum - (k/2)) + u ,2))
plt.title(f"Distribucion Normal K = {k} ")
mybins = np.arange(-15,15,1)
plt.hist(x, bins= mybins, alpha=0.5,
weights=np.zeros_like(x)+1./len(x),
edgecolor="black", linewidth=1.3)
x_1 = np.linspace(sp.norm(u, sigma).ppf(0.01), 
        sp.norm(u,sigma).ppf(0.99), 1000)
plt.plot(x_1,
        sp.norm(u, sigma).pdf(x_1), 
        color="red")
plt.show()


#valor fijo... K = 12 

for i in range(1000):
	sum=0.0
	for j in range(12):
		r=ran.uniform(0,1)
		sum=sum + r
	x.append(round(sigma *(sum-6.0) + u , 2))

plt.title("Distribucion Normal K=12")
mybins = np.arange(-15,15,1)
plt.hist(x, bins= mybins, alpha=0.5,
weights=np.zeros_like(x)+1./len(x),
edgecolor="black", linewidth=1.3)
x_1 = np.linspace(sp.norm(u, sigma).ppf(0.01),
        sp.norm(u,sigma).ppf(0.99), 1000)
plt.plot(x_1, sp.norm(u, sigma).pdf(x_1),
        color="red")
plt.show()