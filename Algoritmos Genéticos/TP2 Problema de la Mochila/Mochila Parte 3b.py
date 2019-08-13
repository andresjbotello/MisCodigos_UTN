listapre=[[1800,72],[600,36],[1200,60]]
listaGreedy=[]
listaOrdenada=[]

for i in range(3):
    listaGreedy.append(float(listapre[i][1]/listapre[i][0]))
listaOrdenada=sorted(listaGreedy,reverse=True)

mochila=[]
sumPeso=0
sumPrecio=0
for i in range(3):
    for j in range(3):
        if (listaOrdenada[i]==float(listapre[j][1]/listapre[j][0])):
            ind=j
    sumPeso= sumPeso + listapre[ind][0]
    if sumPeso<=3000:
        mochila.append(listapre[ind])
        sumPrecio= sumPrecio + listapre[ind][1]
    else:
        sumPeso=sumPeso - listapre[ind][0]

pesos=[]
greedy=[]
indices=[]
for i in range(len(mochila)):
    pesos.append(mochila[i][0])#muestra volúmenes
for i in range(len(mochila)):
    greedy.append(float(mochila[i][1]/mochila[i][0]))#muestra cociente Greedy
for i in range(len(mochila)):
    for j in range(3):
        if (mochila[i]==listapre[j]):
            indices.append(j+1)


print(pesos)
print(greedy)
print(indices)
print(sumPrecio)
print(sumPeso)