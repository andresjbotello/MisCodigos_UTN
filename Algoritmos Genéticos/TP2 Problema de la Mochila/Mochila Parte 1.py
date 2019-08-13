lista=[[150],[325],[600],[805],[430],[1200],[770],[60],[930],[353]]
listavol=[150,325,600,805,430,1200,770,60,930,353]
listapre=[[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]
combinaciones=[]
 
for i in range(len(lista)): #Crea Lista de combinaciones
    combinaciones.append([]) 

for a in range(len(lista)):
    combinaciones[0].append(lista[a])
    for b in range(a+1,len(lista)):
        combinaciones[1].append(lista[a] + lista[b])
        for c in range(b+1,len(lista)):
            combinaciones[2].append(lista[a] + lista[b] + lista[c])
            for d in range(c+1,len(lista)):
                combinaciones[3].append(lista[a] + lista[b]+ lista[c]+ lista[d])
                for e in range(d+1,len(lista)):
                    combinaciones[4].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e])
                    for f in range (e+1,len(lista)):
                        combinaciones[5].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f])
                        for g in range (f+1,len(lista)):
                            combinaciones[6].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g])
                            for h in range (g+1,len(lista)):
                                combinaciones[7].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g]+lista[h])
                                for i in range (h+1,len(lista)):
                                    combinaciones[8].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g]+lista[h]+lista[i])
                                    for j in range (i+1,len(lista)):
                                        combinaciones[9].append(lista[a] + lista[b]+ lista[c]+ lista[d]+ lista[e]+lista[f]+lista[g]+lista[h]+lista[i]+lista[j])

combinacionesvol=[]
for i in range (len(combinaciones)): #Filtra volumenes menores o iguales a 4200
    for j in range (len(combinaciones[i])):
        sum=0
        for k in range (len(combinaciones[i][j])):
            sum= sum + combinaciones[i][j][k]
        if (sum<=4200):
            combinacionesvol.append(combinaciones[i][j])
mx=0
sumVol=0
listaindice=[]
for i in range (len(combinacionesvol)): #busca y suma el beneficio de cada combinacion, y guarda la de mayor beneficio
    sum=0
    sumV=0
    for j in range (len(combinacionesvol[i])):
        ind=listavol.index(combinacionesvol[i][j])
        sum= sum+ listapre[ind][1]
        sumV= sumV + listapre[ind][0]
    if (sum>mx):
        indmax=i
        mx=sum
        sumVol= sumV
for i in range (len(combinacionesvol[indmax])):
    ind=listavol.index(combinacionesvol[indmax][i])
    listaindice.append(ind+1)

print(combinacionesvol[indmax]) #Combinacion de mayor beneficio
print(listaindice) #Indices de los elementos
print(mx) #Valor del beneficio
print(sumVol) #Volúmen total



