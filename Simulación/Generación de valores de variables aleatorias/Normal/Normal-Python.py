import random as ran
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
#con la funcion incluida en python

u=float(input("Ingrese media: "))
sigma=float(input("Ingrese desviacion: "))
normal = sp.norm(u, sigma)
x = np.linspace(normal.ppf(0.01),
    normal.ppf(0.99), 100)
data = np.random.normal(loc=u, scale=sigma,
                        size=1000)
mybins = np.arange(-15,15,1)
plt.hist(data,bins=mybins,
weights=np.zeros_like(data)+1./len(data),
edgecolor='black',color='blue')
fp = normal.pdf(x)
plt.plot(x, fp)
plt.title('Distribucion Normal')
plt.show()