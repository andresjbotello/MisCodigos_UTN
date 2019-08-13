from scipy import stats
import math as ma
import random as rnd

z0 = 7
m = 16
a = 5 
c = 3

n = 25
k = 5
confianza = 0.90


aleatorios = []
for i in range(10000):
    z = (a*z0+c)%m
    aleatorios.append(z)
    z0 = z
    

subcadenas = []

for i in range(0,len(aleatorios)-1):
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

media = (2*len(aleatorios) - 1)/3
varianza = (16*len(aleatorios) - 29)/90
desvio = ma.sqrt(varianza)
print("media: ",media)
print("varianza: ",varianza)
print("desvio: ",desvio)

#calculo la Z
z_calculado = ma.fabs((total_cadenas - media)/desvio)
print("Z calculado: ",z_calculado)



alpha = 0.05
con = 1-(alpha/2)
#Z_1-alpha/2
z_alpha2 = stats.norm.ppf(con)
print("Z en 1 - (alpha/2): ",z_alpha2)

if z_calculado <= z_alpha2:
    print("La secuencia de numeros es independiente y por lo tanto la secuencia es aleatoria")
else:
    print("La secuencia de numeros NO es Independiente y por lo tanto la secuencia NO es aleatoria")
