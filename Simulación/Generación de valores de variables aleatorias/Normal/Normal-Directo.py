import random as ran
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as sp
import math as m

#mediante procedimiento directo
x = []
for i in range (1000):
    r1 = ran.uniform(0,1)
    r2 = ran.uniform(0,1)
    x1 = (m.sqrt(-2*m.log(r1,m.e))
            *m.cos(2*m.pi*r2))
    x2 = (m.sqrt(-2*m.log(r1,m.e))
            *m.sin(2*m.pi*r2))
    x.append(x1)
    x.append(x2)

print("La media es: ",
"%.2f" % np.mean(x))
print("La varianza es: ",
"%.2f" % np.var(x))
print("La desviacion estandar es: ",
"%.2f" % m.sqrt(np.var(x)))
mybins = np.arange(-10,10,1)
plt.hist(x, bins=mybins,
weights=np.zeros_like(x)+1./len(x),
alpha=0.5 ,edgecolor='black',
color ="orange",
linewidth = 1.3) 
plt.show()