lista=[[1800],[600],[1200]]
listapeso=[1800,600,1200]
listapre=[[1800,72],[600,36],[1200,60]]
combinaciones=[]
for i in range(len(lista)): #Crea Lista de combinaciones
    combinaciones.append([]) 

for a in range(len(lista)):
    combinaciones[0].append(lista[a])
    for b in range(a+1,len(lista)):
        combinaciones[1].append(lista[a] + lista[b])
        for c in range(b+1,len(lista)):
            combinaciones[2].append(lista[a] + lista[b] + lista[c])

combinacionesvol=[]
for i in range (len(combinaciones)): #Filtra volumenes menores o iguales a 3000
    for j in range (len(combinaciones[i])):
        sum=0
        for k in range (len(combinaciones[i][j])):
            sum= sum + combinaciones[i][j][k]
        if (sum<=3000):
            combinacionesvol.append(combinaciones[i][j])

mx=0
sumPeso=0
listaindice=[]
for i in range (len(combinacionesvol)): #busca y suma el beneficio de cada combinacion, y guarda la de mayor beneficio
    sum=0
    sumP=0
    for j in range (len(combinacionesvol[i])):
        ind=listapeso.index(combinacionesvol[i][j])
        sum= sum+ listapre[ind][1]
        sumP= sumP + listapre[ind][0]
    if (sum>mx):
        indmax=i
        mx=sum
        sumPeso=sumP
for i in range (len(combinacionesvol[indmax])):
    ind=listapeso.index(combinacionesvol[indmax][i])
    listaindice.append(ind+1)

print(combinacionesvol[indmax]) #Combinacion de mayor beneficio
print(listaindice) #Indices de los elementos
print(mx) #Valor del beneficio        
print(sumPeso)