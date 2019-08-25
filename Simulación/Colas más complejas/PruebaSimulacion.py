import numpy as np 
from matplotlib import pyplot as plt

RELOJ = 0.0
ListaArribos = []
ListaPartidas = []



class Simulacion():

    def __init__(self,servidor,tpoEntreArribos,tpoDeServicio):
        self.nroServidor = servidor
        self.tm_entre_arribos = tpoEntreArribos
        self.tm_servicio = tpoDeServicio
        self.ts_acumulado = 0.0
        self.demora_acumulada = 0.0
        self.area_q_t = 0.0
        self.tiempo_ultimo_evento = 0.0
        self.nro_clientes_cola = 0
        self.completaron_demora = 0
        self.paso = 0        
        self.iniciado = False
        self.estado_servidor = "" #D - disponible | O - ocupado
        self.proximo_evento = ""  #A - Arribo | P - partida        
        self.cola = []
        self.cola.append(0)
        #las listas siguientes se utilizan sólo con el fin de generar las gráficas
        self.cliColaEnT = []
        self.relojEnT = []
        self.tsAcuEnT = []

        self.estado_servidor = "D"
        self.proximo_evento = ""       
        self.iniciado = False
    
    
    def tiempos(self,evento,letra):
        global RELOJ        
        if letra == 'A':
            RELOJ = evento[0]
            self.tiempo_ultimo_evento = RELOJ
        else:
            RELOJ = evento[0]
            self.tiempo_ultimo_evento = RELOJ

    def arribo(self,evento):
        global RELOJ
        global ListaArribos
        indice = evento[1] - 1 #posicion en lista arribos
        ListaArribos[indice] = [RELOJ + np.random.exponential(1/self.tm_entre_arribos),evento[1]]                

        if self.estado_servidor == "D":
            self.estado_servidor = "O"
            ListaPartidas[indice] = [RELOJ + np.random.exponential(1/self.tm_servicio),evento[1]]
            self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
            self.completaron_demora += 1    
            #grafica  
            """
            sim1.relojEnT.append(RELOJ)  
            sim1.cliColaEnT.append(sim1.nro_clientes_cola)
            sim1.tsAcuEnT.append(sim1.ts_acumulado)
            """
        else:
            self.area_q_t += self.nro_clientes_cola * (RELOJ - self.cola[self.nro_clientes_cola])
            self.nro_clientes_cola += 1
            self.cola.append(RELOJ)
            #grafica
            """
            sim1.cliColaEnT.append(sim1.nro_clientes_cola)
            sim1.relojEnT.append(RELOJ)
            sim1.tsAcuEnT.append(sim1.ts_acumulado)
            """
    def partida(self,evento):
        global RELOJ
        global ListaPartidas
        indice = evento[1] - 1 #posicion en lista partida

        if self.nro_clientes_cola > 0:
            ListaPartidas[indice] = [RELOJ + np.random.exponential(1/self.tm_servicio),evento[1]]
            self.demora_acumulada += RELOJ - self.cola[0]
            self.completaron_demora += 1
            self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
            self.area_q_t += (self.nro_clientes_cola * (RELOJ - self.tiempo_ultimo_evento))
            self.nro_clientes_cola -= 1
            self.cola.pop(0)
            #grafica
            """
            sim1.cliColaEnT.append(sim1.nro_clientes_cola)
            sim1.relojEnT.append(RELOJ)
            sim1.tsAcuEnT.append(sim1.ts_acumulado)
            """
        else:
            self.estado_servidor = "D"
            ListaPartidas[indice] = [999999,evento[1]]
            #grafica
            """
            sim1.relojEnT.append(RELOJ)
            sim1.cliColaEnT.append(sim1.nro_clientes_cola)
            sim1.tsAcuEnT.append(sim1.ts_acumulado)
            """
        
def run(server1,server2):
        global ListaArribos
        global ListaPartidas
        global RELOJ
        print("Inicializando simulacion")        

        #Tiempo del primer arribo
        ListaArribos.append([np.random.exponential(1/server1.tm_entre_arribos),1])
        ListaArribos.append([np.random.exponential(1/server2.tm_entre_arribos),2])
    
        #Numero grande para asegurar que el primer evento sea un arribo
        ListaPartidas.append([999999,1])
        ListaPartidas.append([999999,2])
        
        while RELOJ < 50:
            """
            if server1.estado_servidor == 'D':
                print("reloj: "+ str(RELOJ))
                server1.tiempos(ListaArribos[0],'A')
                server1.arribo(ListaArribos[0])

            elif server2.estado_servidor == 'D':
                print("reloj: "+ str(RELOJ))
                server2.tiempos(ListaArribos[1],'A')
                server2.arribo(ListaArribos[1])
            """
            minArribo = min(ListaArribos)
            minPartida = min(ListaPartidas)

            if minArribo < minPartida: #server1.nro_clientes_cola <= server2.nro_clientes_cola
                print("reloj: "+ str(RELOJ))
                nroServer = minArribo[1]
                if nroServer == 1:
                    server1.tiempos(minArribo,'A') 
                    server1.arribo(minArribo)
                else:              
                    server2.tiempos(minArribo,'A') 
                    server2.arribo(minArribo)
            else:
                print("reloj: "+ str(RELOJ))
                nroServer = minPartida[1]
                if nroServer == 1:
                    server1.tiempos(minPartida,'P') 
                    server1.partida(minPartida)
                else:              
                    server2.tiempos(minPartida,'P') 
                    server2.partida(minPartida)
            
        return server1, server2


def nro_prom_clientes_cola(server1,server2):
    global RELOJ
    if RELOJ != 0:
        nro_clientes_prom_cola1 = server1.area_q_t/RELOJ
        nro_clientes_prom_cola2 = server2.area_q_t/RELOJ
        return nro_clientes_prom_cola1, nro_clientes_prom_cola2
    else:
        nro_clientes_prom_cola = 0 #no tiene sentido, ver
        return nro_clientes_prom_cola

def utilizacion_prom_servidor(server1,server2):
    if RELOJ != 0:
        utilizacion_prom_servidor1 = server1.ts_acumulado/RELOJ
        utilizacion_prom_servidor2 = server2.ts_acumulado/RELOJ
        return utilizacion_prom_servidor1, utilizacion_prom_servidor2
    else:
        utilizacion_prom_servidor = 0 #no tiene sentido, ver
        return utilizacion_prom_servidor

def demora_prom_cliente(server1,server2):
    demora_prom_cliente1 = server1.demora_acumulada/server1.completaron_demora
    demora_prom_cliente2 = server2.demora_acumulada/server2.completaron_demora
    return demora_prom_cliente1, demora_prom_cliente2
    


def reportes(server1,server2):
    print(" Estadísticos ".center(101,'='),'\n')
    print(("Cantidad promedio de clientes en cola del servidor 1 y servidor 2: "+ str(nro_prom_clientes_cola(server1,server2))).center(100,' '))
    print(("Utilizacion promedio del servidor 1 y servidor 2: "+ str(utilizacion_prom_servidor(server1,server2))).center(100,' ')) 
    print(("Demora promedio de cliente del servidor 1 y servidor 2: "+ str(demora_prom_cliente(server1,server2))).center(100,' '))
    """#graficas
    graficaPromCliEnCola()
    graficaUtiServidor()"""
        


if __name__=='__main__':
    server1 = Simulacion(servidor=1,tpoEntreArribos=10.0,tpoDeServicio=7.0)
    server2 = Simulacion(servidor=2,tpoEntreArribos=10.0,tpoDeServicio=5.0)
    run(server1,server2)
    reportes(server1,server2)