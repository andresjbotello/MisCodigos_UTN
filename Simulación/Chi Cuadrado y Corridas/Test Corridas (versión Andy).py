import random as rnd
import math as ma
from scipy import stats

m = 10000
aleatorios = []
for i in range(m):
    aleatorios.append(rnd.random())

subcadenas = []

for i in range(0,m-1):
    if aleatorios[i] < aleatorios[i+1]:
        subcadenas.append('+')
    else:
        subcadenas.append('-')

#print(aleatorios,subcadenas)
total_cadenas = 1

ini = subcadenas[0]
for i in range(0,len(subcadenas)-1):
    if ini != subcadenas[i+1]:
        total_cadenas = total_cadenas + 1
        ini = subcadenas[i+1]

print("Total Cadenas: ",total_cadenas)

media = (2*m - 1)/3
varianza = (16*m - 29)/90
desvio = ma.sqrt(varianza)
print("media: ",media)
print("varianza: ",varianza)
print("desvio: ",desvio)

#calculo la Z
z_calculado = ma.fabs((total_cadenas - media)/desvio)
print("Z calculado: ",z_calculado)

alpha = 0.05
c = 1-(alpha/2)
#Z_1-alpha/2
z_alpha2 = stats.norm.ppf(c)
print("Z en 1 - (alpha/2): ",z_alpha2)

if z_calculado <= z_alpha2:
    print("La secuencia de numeros es independiente y por lo tanto la secuencia es aleatoria")
else:
    print("La secuencia de numeros NO es Independiente y por lo tanto la secuencia NO es aleatoria")
