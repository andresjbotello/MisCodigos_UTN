import numpy as np
from matplotlib import pyplot as plt

RELOJ = 0.0
ListaArribos = []
ListaPartidas = []
ColaUnica = []


class Simulacion():

    def __init__(self, servidor, tpoEntreArribos, tpoDeServicio):
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
        self.estado_servidor = ""  # D - disponible | O - ocupado
        self.proximo_evento = ""  # A - Arribo | P - partida
        self.cola = []
        self.cola.append(0)
        # las listas siguientes se utilizan sólo con el fin de generar las gráficas
        self.cliColaEnT = []
        self.relojEnT = []
        self.tsAcuEnT = []

        self.estado_servidor = "D"
        self.proximo_evento = ""
        self.iniciado = False

    def tiempos(self, evento, letra):
        global RELOJ
        if letra == 'A':
            RELOJ = evento[0]
            self.tiempo_ultimo_evento = RELOJ
        else:
            RELOJ = evento[0]
            self.tiempo_ultimo_evento = RELOJ

    def arribo(self, evento):
        global RELOJ
        global ListaArribos

        indice = evento[1] - 1  # posicion en lista arribos

        if self.nroServidor < 3:
            ListaArribos[indice] = [RELOJ + np.random.exponential(self.tm_entre_arribos), evento[1]]

            if self.estado_servidor == "D":
                self.estado_servidor = "O"
                ListaPartidas[indice] = [RELOJ + np.random.exponential(self.tm_servicio), evento[1]]
                self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
                self.completaron_demora += 1
                # grafica
                """
                sim1.relojEnT.append(RELOJ)  
                sim1.cliColaEnT.append(sim1.nro_clientes_cola)
                sim1.tsAcuEnT.append(sim1.ts_acumulado)
                """
            else:
                self.area_q_t += self.nro_clientes_cola * (RELOJ - self.cola[self.nro_clientes_cola])
                self.nro_clientes_cola += 1
                self.cola.append(RELOJ)
                # grafica
                """
                sim1.cliColaEnT.append(sim1.nro_clientes_cola)
                sim1.relojEnT.append(RELOJ)
                sim1.tsAcuEnT.append(sim1.ts_acumulado)
                """
        else:
            if self.nroServidor == 3:
                self.estado_servidor = "O"
                ListaPartidas[indice] = [RELOJ + np.random.exponential(self.tm_servicio), evento[1]]
                self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
                self.completaron_demora += 1
            elif self.nroServidor == 4:
                self.estado_servidor = "O"
                ListaPartidas[indice] = [RELOJ + np.random.exponential(self.tm_servicio), evento[1]]
                self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
                self.completaron_demora += 1
            else:
                self.estado_servidor = "O"
                ListaPartidas[indice] = [RELOJ + np.random.exponential(self.tm_servicio), evento[1]]
                self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
                self.completaron_demora += 1

    def partida(self, evento):
        global RELOJ
        global ListaPartidas
        global ColaUnica
        indice = evento[1] - 1  # posicion en lista partida

        if self.nroServidor < 3:
            if self.nro_clientes_cola > 0:
                ListaPartidas[indice] = [RELOJ + np.random.exponential(self.tm_servicio), evento[1]]
                self.demora_acumulada += RELOJ - self.cola[0]
                self.completaron_demora += 1
                self.ts_acumulado += (ListaPartidas[indice][0] - RELOJ)
                self.area_q_t += (self.nro_clientes_cola * (RELOJ - self.tiempo_ultimo_evento))
                self.nro_clientes_cola -= 1
                self.cola.pop(0)
                # grafica
                """
                sim1.cliColaEnT.append(sim1.nro_clientes_cola)
                sim1.relojEnT.append(RELOJ)
                sim1.tsAcuEnT.append(sim1.ts_acumulado)
                """
            else:
                self.estado_servidor = "D"
                ListaPartidas[indice] = [999999, evento[1]]
                # grafica
                """
                sim1.relojEnT.append(RELOJ)
                sim1.cliColaEnT.append(sim1.nro_clientes_cola)
                sim1.tsAcuEnT.append(sim1.ts_acumulado)
                """
        else:
            if self.nroServidor == 3:
                self.estado_servidor = 'D' #acá falta algo
            elif self.nroServidor == 4:
                self.estado_servidor = 'D'
            else:
                self.estado_servidor = 'D'


def run(server1, server2, server3, server4, server5):
    global ListaArribos
    global ListaPartidas
    global RELOJ
    global ColaUnica
    print("Inicializando simulacion")

    # Tiempo del primer arribo
    ListaArribos.append([np.random.exponential(server1.tm_entre_arribos), 1])
    ListaArribos.append([np.random.exponential(server2.tm_entre_arribos), 2])
    ListaArribos.append([99999, 3])
    ListaArribos.append([99999, 4])
    ListaArribos.append([99999, 5])

    # Numero grande para asegurar que el primer evento sea un arribo
    ListaPartidas.append([999999, 1])
    ListaPartidas.append([999999, 2])
    ListaPartidas.append([999999, 3])
    ListaPartidas.append([999999, 4])
    ListaPartidas.append([999999, 5])

    while RELOJ < 5000:
        minArribo = min(ListaArribos)
        minPartida = min(ListaPartidas)

        if minArribo < minPartida:
            print("reloj: " + str(RELOJ))
            nroServer = minArribo[1]
            if nroServer == 1:
                server1.tiempos(minArribo, 'A')
                server1.arribo(minArribo)
            else:
                server2.tiempos(minArribo, 'A')
                server2.arribo(minArribo)

        else:
            print("reloj: " + str(RELOJ))
            nroServer = minPartida[1]
            if nroServer == 1:
                server1.tiempos(minPartida, 'P')
                server1.partida(minPartida)
                if server3.estado_servidor == 'O' and server4.estado_servidor == 'O' and server5.estado_servidor == 'O':
                    ColaUnica.append(minPartida[0])  # solo se agrega a la cola si los 3 servidores de segunda linea estan ocupados
                elif server3.estado_servidor == 'D':
                    server3.arribo(minPartida)
                    if len(ColaUnica) > 0:
                        ColaUnica.pop(0)
                elif server4.estado_servidor == 'D':
                    server4.arribo(minPartida)
                    if len(ColaUnica) > 0:
                        ColaUnica.pop(0)
                else:
                    server5.arribo(minPartida)
                    if len(ColaUnica) > 0:
                        ColaUnica.pop(0)
            elif nroServer == 2:
                server2.tiempos(minPartida, 'P')
                server2.partida(minPartida)
                if server3.estado_servidor == 'O' and server4.estado_servidor == 'O' and server5.estado_servidor == 'O':
                    ColaUnica.append(minPartida[0])
                elif server3.estado_servidor == 'D':
                    server3.arribo(minPartida)
                    if len(ColaUnica) > 0:
                        ColaUnica.pop(0)
                elif server4.estado_servidor == 'D':
                    server4.arribo(minPartida)
                    if len(ColaUnica) > 0:
                        ColaUnica.pop(0)
                else:
                    server5.arribo(minPartida)
                    if len(ColaUnica) > 0:
                        ColaUnica.pop(0)
            elif nroServer == 3:
                server3.tiempos(minPartida, 'P')
                server3.partida(minPartida)
            elif nroServer == 4:
                server4.tiempos(minPartida, 'P')
                server4.partida(minPartida)
            elif nroServer == 5:
                server5.tiempos(minPartida, 'P')
                server5.partida(minPartida)
            """    
            else:
                ArribosLinea2 = ListaArribos[2:]
                PartidasLinea2 = ListaPartidas[2:]

                minArribo = min(ArribosLinea2)
                minPartida = min(PartidasLinea2)

                if minArribo < minPartida:  # server1.nro_clientes_cola <= server2.nro_clientes_cola
                    print("reloj: " + str(RELOJ))
                    nroServer = minArribo[1]
                    if nroServer == 3:
                        server3.tiempos(minArribo, 'A')
                        server3.arribo(minArribo)
                        ColaUnica.pop(0)
                    elif nroServer == 4:
                        server4.tiempos(minArribo, 'A')
                        server4.arribo(minArribo)
                        ColaUnica.pop(0)
                    else:
                        server5.tiempos(minArribo, 'A')
                        server5.arribo(minArribo)
                        ColaUnica.pop(0)
                else:
                    print("reloj: " + str(RELOJ))
                    nroServer = minPartida[1]
                    if nroServer == 3:
                        server3.tiempos(minPartida, 'P')
                        server3.partida(minPartida)
                    elif nroServer == 4:
                        server4.tiempos(minPartida, 'P')
                        server4.partida(minPartida)
                    else:
                        server5.tiempos(minPartida, 'P')
                        server5.partida(minPartida)
            """
    return server1, server2, server3, server4, server5

"""
def nro_prom_clientes_cola(server1, server2, server3, server4, server5):
    global RELOJ
    if RELOJ != 0:
        nro_clientes_prom_cola1 = server1.area_q_t / RELOJ
        nro_clientes_prom_cola2 = server2.area_q_t / RELOJ
        return nro_clientes_prom_cola1, nro_clientes_prom_cola2
    else:
        nro_clientes_prom_cola = 0  # no tiene sentido, ver
        return nro_clientes_prom_cola


def utilizacion_prom_servidor(server1, server2, server3, server4, server5):
    if RELOJ != 0:
        utilizacion_prom_servidor1 = server1.ts_acumulado / RELOJ
        utilizacion_prom_servidor2 = server2.ts_acumulado / RELOJ
        return utilizacion_prom_servidor1, utilizacion_prom_servidor2
    else:
        utilizacion_prom_servidor = 0  # no tiene sentido, ver
        return utilizacion_prom_servidor


def demora_prom_cliente(server1, server2, server3, server4, server5):
    demora_prom_cliente1 = server1.demora_acumulada / server1.completaron_demora
    demora_prom_cliente2 = server2.demora_acumulada / server2.completaron_demora
    return demora_prom_cliente1, demora_prom_cliente2
"""
"""
def reportes(server1, server2, server3, server4, server5):
    print(" Estadísticos ".center(101, '='), '\n')
    print(("Cantidad promedio de clientes en cola de los servers: " + str(
        nro_prom_clientes_cola(server1, server2, server3, server4, server5))).center(100, ' '))
    print(("Utilizacion promedio de los servers: " + str(
        utilizacion_prom_servidor(server1, server2, server3, server4, server5))).center(100, ' '))
    print(("Demora promedio de cliente en los servidores: " + str(
        demora_prom_cliente(server1, server2, server3, server4, server5))).center(100, ' '))
    #graficas 
    #graficaPromCliEnCola()
    #graficaUtiServidor()
"""

if __name__ == '__main__':
    server1 = Simulacion(servidor=1, tpoEntreArribos=10.0, tpoDeServicio=7.0)
    server2 = Simulacion(servidor=2, tpoEntreArribos=10.0, tpoDeServicio=5.0)
    server3 = Simulacion(servidor=3, tpoEntreArribos=10.0, tpoDeServicio=6.0)
    server4 = Simulacion(servidor=4, tpoEntreArribos=10.0, tpoDeServicio=5.0)
    server5 = Simulacion(servidor=5, tpoEntreArribos=10.0, tpoDeServicio=5.0)

    run(server1, server2, server3, server4, server5)
    #  reportes(server1, server2, server3, server4, server5)



    # Los servers 3,4 y 5 no tienen que generar arribos, son los clientes que salen de 1 y 2.

