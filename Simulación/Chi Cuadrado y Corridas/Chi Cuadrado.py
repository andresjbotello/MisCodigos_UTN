import random as rnd
from scipy import stats

m = 10000
aleatorios = []
for i in range(m):
    aleatorios.append(rnd.random())

k = 5
n = 25
confianza = 0.90 

u = []
f1 = 0
f2 = 0
f3 = 0
f4 = 0
f5 = 0

for i in range(n):
    p = rnd.randint(0,9999)
    u.append(aleatorios[p])
    if p in range(0,1999):
        f1 += 1
    elif p in range(2000,3999):
        f2 += 1
    elif p in range(4000,5999):
        f3 += 1
    elif p in range(6000,7999):
        f4 += 1
    elif p in range(8000,9999):
        f5 += 1

print("f1=",f1,"f2=",f2,"f3=",f3,"f4=",f4,"f5=",f5)


chicuadrado = (1/5)*((f1-5)**2+(f2-5)**2+(f3-5)**2+(f4-5)**2+(f5-5)**2)

print("X^2 = ",chicuadrado)
valorTabla = stats.chi2.ppf(confianza,k-1)
print(valorTabla)

if chicuadrado > valorTabla:
    print("No son uniformes")
else:
    print("Son uniformes")







