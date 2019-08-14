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
        #las listas siguientes se utilizan sólo con el fin de generar las gráficas
        self.cliColaEnT = []
        self.relojEnT = []
        self.tsAcuEnT = []
    
    def inicializar(self):
        
        self.estado_servidor = "D"
        self.proximo_evento = ""
        
        
        self.iniciado = False

    def run(self,server1,server2):
        global ListaArribos
        global ListaPartidas
        global RELOJ
        print("Inicializando simulacion")
        server1.inicializar()
        server2.inicializar()

        #Tiempo del primer arribo
        ListaArribos.append([np.random.exponential(1/self.tm_entre_arribos),1])
        ListaArribos.append([np.random.exponential(1/self.tm_entre_arribos),2])
    
        #Numero grande para asegurar que el primer evento sea un arribo
        ListaPartidas.append([999999,1])
        ListaPartidas.append([999999,2])
        
        while RELOJ < 50:
            if server1.estado_servidor == 'D':
                print("reloj: "+ str(RELOJ))
                tiempos1()
                
                if server1.proximo_evento == "A":
                    arribo1()
                else:
                    partida1()
            elif server2.estado_servidor == 'D':
                print("reloj: "+ str(RELOJ))
                tiempos2()
                
                if server2.proximo_evento == "A":
                    arribo2()
                else:
                    partida2()

            minArribo = min(ListaArribos)
            minPartida = min(ListaPartidas)
            if minArribo < minPartida: #server1.nro_clientes_cola <= server2.nro_clientes_cola
                print("reloj: "+ str(RELOJ))
                self.tiempos(minArribo,'A')                
                self.arribo(minArribo)
            else:
                self.tiempos(minPartida,'P')
                self.partida(minPartida)
            

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
        indice = evento[1] - 1
        ListaArribos[indice] = [RELOJ + np.random.exponential(1/self.tm_entre_arribos),evento[1]]

        if self.estado_servidor == "D":
            sim1.estado_servidor = "O"
            ListaPartidas[indice] = [RELOJ + np.random.exponential(1/self.tm_servicio),evento[1]]
            self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
            self.completaron_demora += 1    
            #grafica  
            sim1.relojEnT.append(RELOJ)  
            sim1.cliColaEnT.append(sim1.nro_clientes_cola)
            sim1.tsAcuEnT.append(sim1.ts_acumulado)
        else:
            sim1.area_q_t += sim1.nro_clientes_cola * (RELOJ - sim1.tiempo_ultimo_evento)
            sim1.nro_clientes_cola += 1
            sim1.cola.append(RELOJ)
            #grafica
            sim1.cliColaEnT.append(sim1.nro_clientes_cola)
            sim1.relojEnT.append(RELOJ)
            sim1.tsAcuEnT.append(sim1.ts_acumulado)
    
    def partida(self,evento):
        pass
        
        


if __name__=='__main__':
    server1 = Simulacion(servidor=1,tpoEntreArribos=10.0,tpoDeServicio=7.0)
    server2 = Simulacion(servidor=2,tpoEntreArribos=10.0,tpoDeServicio=5.0)