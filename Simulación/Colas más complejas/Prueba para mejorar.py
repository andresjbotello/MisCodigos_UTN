import numpy as np 
from matplotlib import pyplot as plt

RELOJ = 0.0

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
        self.lista_eventos = []
        self.cola = []
        #las listas siguientes se utilizan sólo con el fin de generar las gráficas
        self.cliColaEnT = []
        self.relojEnT = []
        self.tsAcuEnT = []
    
    def inicializar(self):
        self.estado_servidor = "D"
        self.proximo_evento = ""
        
        #Tiempo del primer arribo
        self.lista_eventos.append(np.random.exponential(1/self.tm_entre_arribos))
    
        #Numero grande para asegurar que el primer evento sea un arribo
        self.lista_eventos.append(99999999)
        self.iniciado = False

    def run(self,server1,server2):
        print("Inicializando simulacion")
        server1.inicializar()
        server2.inicializar()

        global RELOJ
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
            elif server1.lista_eventos[1] <= server2.lista_eventos[1]: #server1.nro_clientes_cola <= server2.nro_clientes_cola
                print("reloj: "+ str(RELOJ))
                tiempos1()
                
                if server1.proximo_evento == "A":
                    arribo1()
                else:
                    partida1()
            elif server1.lista_eventos[1] > server2.lista_eventos[1]:
                print("reloj: "+ str(RELOJ))
                tiempos2()
                
                if server2.proximo_evento == "A":
                    arribo2()
                else:
                    partida2()

    def tiempos(self,server1,server2):
        global RELOJ
        """
        if sim1.lista_eventos[0]<sim2.lista_eventos[0]:
            sim1.lista_eventos[0] += global RELOJ
        if sim1.lista_eventos[1]<sim2.lista_eventos[1]:
            sim1.lista_eventos[1] = global RELOJ
        """
            #ESTO ES LO QUE TENEMOS QUE CAMBIAR
            #
            #lo de abajo está mal
        server1.tiempo_ultimo_evento = RELOJ
        if server1.lista_eventos[0] <= server1.lista_eventos[1]:
            RELOJ = server1.lista_eventos[0]
            sim1.proximo_evento = "A"
        else:
            RELOJ = server1.lista_eventos[1]
            sim1.proximo_evento = "P"
        


if __name__=='__main__':
    server1 = Simulacion(servidor=1,tpoEntreArribos=10.0,tpoDeServicio=7.0)
    server2 = Simulacion(servidor=1,tpoEntreArribos=10.0,tpoDeServicio=5.0)



#hola