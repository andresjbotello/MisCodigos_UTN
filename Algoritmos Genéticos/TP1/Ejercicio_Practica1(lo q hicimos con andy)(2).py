#Error de la line75 y line76 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#Maximo de la funcion 1073741823
from random import randint
from random import random
import xlwt
wb = xlwt.Workbook()#creamos archivo de Excel
ws = wb.add_sheet('AG')#agregamos hoja
pm=0.05
pc=0.75
cr=[['' for j in range(10)]for i in range(31)]
"""for i in range (10):
    cr.append('')"""
for j in range(30):
    for i in range(10):  #Crea poblacion inicial   
        cr[0][i]+=str(randint(0,1))
#print(cr[0])
tab=[[0 for j in range(5)]for i in range(31)] #Creacion tabla
for c in range(30):
    dec=[]
    sum=0
    for i in range(10):
        num= int(str(cr[c][i]),2)
        sum+=num
        dec.append(num) 
    tab[c][0]=max(dec) #"Llena tabla."
    tab[c][1]=str(bin(tab[c][0])[2:].zfill(30))
    tab[c][2]=min(dec)
    tab[c][3]=str(bin(tab[c][2])[2:].zfill(30))
    tab[c][4]=sum/10 
    ws.write(c,0,tab[c][0])#Llenamos filas y columnas de la hoja de Excel
    ws.write(c,1,tab[c][1])
    ws.write(c,2,tab[c][2])
    ws.write(c,3,tab[c][3])
    ws.write(c,4,tab[c][4])

    fit=[[0 for j in range(4)]for i in range(10)] #"Creacion funcion Fitness"
    sum=0
    for i in range(10): #"Llenado tabla fitness"
        fit[i][0]=str(bin(dec[i])[2:].zfill(30))
        fit[i][1]=dec[i]
        fit[i][2]=(fit[i][1]/((2**30)-1))**2
        sum+=fit[i][2]
    for i in range(10): #"Calculo Probabilidades" 
        if round(fit[i][2]*100/sum)==0:
            fit[i][3]=1
        else:
            fit[i][3]=round(fit[i][2]*100/sum) 
    print(fit)
    print(tab[c])
    ru=[] #Ruleta
    for i in range(10): #"Carga Ruleta"
        for j in range (fit[i][3]):
            ru.append(fit[i][1])
    for i in range (5): #crossover
        cr1=randint(0, len(ru)-1) #"Selecciona Candidatos"
        cr2=randint(0, len(ru)-1) 
        cr1h=str(bin(ru[cr1])[2:].zfill(30)) #Transforma a binario con 30 digitos
        cr2h=str(bin(ru[cr2])[2:].zfill(30))
        pc1= random()
        """print(cr1h)
        print(cr2h)
        print(cr1)
        print(cr2)
        print(pc1)"""
        if pc1<=pc: #"Crossover"
            gen= randint (0,29)
            aux1=cr1h[gen:30]
            aux2=cr2h[gen:30]
            cr1hijo=cr1h.replace(aux1,aux2) 
            cr2hijo=cr2h.replace(aux2,aux1)
            """print(gen)
            print(aux1)
            print(aux2)  
            print(cr1hijo)          
            print(cr2hijo)"""
            """pos1=[a for a in range(10) if (cr1h==cr[a])]  #Busca la posiciones de los cr que fueron intercambiados
            pos2=[a for a in range(10) if (cr2h==cr[a])]
            print(cr1hijo)
            print(cr2hijo)
            print(int(pos1[0]))
            print(int(pos2[0]))
            print(cr[int(pos1[0])])
            print(cr[int(pos2[0])])"""
            cr[c+1][i*2]=(cr1hijo) 
            cr[c+1][(i*2)+1]=(cr2hijo) 
        else:
            cr[c+1][i*2]=cr1h
            cr[c+1][(i*2)+1]=cr2h
        pm1=random()
        if pm1<=pm:
            gen= randint(0,29)
            cr1hijo=list(map(int,str(cr1h))) #Separa los elementos de la lista como un elemento c/u
            cr2hijo=list(map(int,str(cr2h))) 
            if(cr1hijo[gen]==0):
                cr1hijo.insert(gen,1)   #Inserta el elemento y luego borra el que estaba
                cr1hijo.pop(gen+1)
            else:
                cr1hijo.insert(gen,0)
                cr1hijo.pop(gen+1)       
            cr1hijo=("".join(map(str,cr1hijo)))     #Junta todos los elementos en un binario de 30
            cr[c+1][i*2]=cr1hijo
            if(cr2hijo[gen]==0):
                cr2hijo.insert(gen,1)
                cr2hijo.pop(gen+1)
            else:
                cr2hijo.insert(gen,0)
                cr2hijo.pop(gen+1)
            cr2hijo=("".join(map(str,cr2hijo)))     #Junta todos los elementos en un binario de 30
            cr[c+1][(i*2)+1]=cr2hijo
            """print(gen)
            print(cr1hijo)
            print(cr2hijo)"""
    
        """pos1=[a for a in range(10) if (cr1h==cr[a])]  #Busca la posiciones de los cr que fueron intercambiados
        pos2=[a for a in range(10) if (cr2h==cr[a])]
        print(str(pos1[0]))
        print(str(pos2[0]))
        cr[int(pos1[0])]=cr1hijo
        cr[int(pos2[0])]=cr2hijo"""     #No se xq mierda no toma la asignacion jaja
         

#Falta definir cuantas veces se hace el crossover, para ver como se completa la matriz cr con los nuevos hijos
#Tambien falta la mutacion, cuantas veces se hace como se completa etc etc
#Exportar cosas a excel (libreria xlwt)"""

wb.save(r'C:\Users\Orne\Google Drive\Facu\3ro\Algoritmos Genéticos\Python Codigos\Ejercicios\Ejercicio1\AG.xls')


