listapre=[[150,20],[325,40],[600,50],[805,36],[430,25],[1200,64],[770,54],[60,18],[930,46],[353,28]]
listaGreedy=[]
listaOrdenada=[]

for i in range(10):
    listaGreedy.append(float(listapre[i][1]/listapre[i][0]))
listaOrdenada=sorted(listaGreedy,reverse=True)

mochila=[]
sumVol=0
sumPrecio=0
for i in range(10):
    for j in range(10):
        if (listaOrdenada[i]==float(listapre[j][1]/listapre[j][0])):
            ind=j
    sumVol= sumVol + listapre[ind][0]
    if sumVol<=4200:
        mochila.append(listapre[ind])
        sumPrecio= sumPrecio + listapre[ind][1]
    else:
        sumVol=sumVol - listapre[ind][0]

volumenes=[]
greedy=[]
indices=[]
for i in range(len(mochila)):
    volumenes.append(mochila[i][0])#muestra volúmenes
for i in range(len(mochila)):
    greedy.append(float(mochila[i][1]/mochila[i][0]))#muestra cociente Greedy
for i in range(len(mochila)):
    for j in range(10):
        if (mochila[i]==listapre[j]):
            indices.append(j+1)


print(volumenes)
print(greedy)
print(indices)
print(sumPrecio)
print(sumVol)
    