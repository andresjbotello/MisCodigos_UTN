import numpy as np 
from matplotlib import pyplot as plt

class R():
    def __init__(self):
        self.reloj = 0.0

class sim1():
    ts_acumulado, demora_acumulada, area_q_t, tiempo_ultimo_evento = 0.0,0.0,0.0,0.0
    nro_clientes_cola, completaron_demora, paso = 0,0,0
    tm_entre_arribos = 10.0
    tm_servicio = 7.0
    iniciado = False
    estado_servidor = "" #D - disponible | O - ocupado
    proximo_evento = ""  #A - Arribo | P - partida
    lista_eventos = []
    cola = []
    #las listas siguientes se utilizan sólo con el fin de generar las gráficas
    cliColaEnT = []
    relojEnT = []
    tsAcuEnT = []

class sim2():
    ts_acumulado, demora_acumulada, area_q_t, tiempo_ultimo_evento = 0.0,0.0,0.0,0.0
    nro_clientes_cola, completaron_demora, paso = 0,0,0
    tm_entre_arribos = 10.0
    tm_servicio = 5.0
    iniciado = False
    estado_servidor = "" #D - disponible | O - ocupado
    proximo_evento = ""  #A - Arribo | P - partida
    lista_eventos = []
    cola = []
    #las listas siguientes se utilizan sólo con el fin de generar las gráficas
    cliColaEnT = []
    relojEnT = []
    tsAcuEnT = []



def inicializar1():
    sim1.estado_servidor = "D"
    sim1.proximo_evento = ""
    sim1.ts_acumulado, sim1.demora_acumulada, sim1.area_q_t, sim1.tiempo_ultimo_evento = 0.0,0.0,0.0,0.0
    sim1.nro_clientes_cola, sim1.completaron_demora, sim1.paso = 0,0,0
    
    #Tiempo del primer arribo
    sim1.lista_eventos.append(np.random.exponential(1/sim1.tm_entre_arribos))

    #Numero grande para asegurar que el primer evento sea un arribo
    sim1.lista_eventos.append(99999999)
    sim1.iniciado = False

def inicializar2():
    sim2.estado_servidor = "D"
    sim2.proximo_evento = ""
    sim2.ts_acumulado, sim2.demora_acumulada, sim2.area_q_t, sim2.tiempo_ultimo_evento = 0.0,0.0,0.0,0.0
    sim2.nro_clientes_cola, sim2.completaron_demora, sim2.paso = 0,0,0
    
    #Tiempo del primer arribo
    sim2.lista_eventos.append(np.random.exponential(1/sim2.tm_entre_arribos))

    #Numero grande para asegurar que el primer evento sea un arribo
    sim2.lista_eventos.append(99999999)
    sim2.iniciado = False

def run():
    print("Inicializando simulacion")
    inicializar1()
    inicializar2()
    while re.reloj < 50:
    




        if sim1.estado_servidor == 'D':
            print("reloj: "+ str(re.reloj))
            tiempos1()
            
            if sim1.proximo_evento == "A":
                arribo1()
            else:
                partida1()
        elif sim2.estado_servidor == 'D':
            print("reloj: "+ str(re.reloj))
            tiempos2()
            
            if sim2.proximo_evento == "A":
                arribo2()
            else:
                partida2()
        elif sim1.lista_eventos[1] <= sim2.lista_eventos[1]: #sim1.nro_clientes_cola <= sim2.nro_clientes_cola
            print("reloj: "+ str(re.reloj))
            tiempos1()
            
            if sim1.proximo_evento == "A":
                arribo1()
            else:
                partida1()
        elif sim1.lista_eventos[1] > sim2.lista_eventos[1]:
            print("reloj: "+ str(re.reloj))
            tiempos2()
            
            if sim2.proximo_evento == "A":
                arribo2()
            else:
                partida2()


    #reportes()

def tiempos1():
    """
    if sim1.lista_eventos[0]<sim2.lista_eventos[0]:
        sim1.lista_eventos[0] += re.reloj
    if sim1.lista_eventos[1]<sim2.lista_eventos[1]:
        sim1.lista_eventos[1] = re.reloj
    """

    sim1.tiempo_ultimo_evento = re.reloj
    if sim1.lista_eventos[0] <= sim1.lista_eventos[1]:
        re.reloj = sim1.lista_eventos[0]
        sim1.proximo_evento = "A"
    else:
        re.reloj = sim1.lista_eventos[1]
        sim1.proximo_evento = "P"

def tiempos2():
    """
    if sim2.lista_eventos[0]<sim1.lista_eventos[0]:
        sim2.lista_eventos[0] += re.reloj
    if sim2.lista_eventos[1]<sim1.lista_eventos[1]:
       sim2.lista_eventos[1] = re.reloj
    """
    sim2.tiempo_ultimo_evento = re.reloj
    if sim2.lista_eventos[0] <= sim2.lista_eventos[1]:
        re.reloj = sim2.lista_eventos[0]
        sim2.proximo_evento = "A"
    else:
        re.reloj = sim2.lista_eventos[1]
        sim2.proximo_evento = "P"


def arribo1():
    if re.reloj != 0:    
        if sim1.lista_eventos[0]<sim2.lista_eventos[0]:
            re.reloj = sim1.lista_eventos[0]
        else:
            re.reloj= sim2.lista_eventos[0]
    sim1.lista_eventos[0] = re.reloj + np.random.exponential(1/sim1.tm_entre_arribos)
    if sim1.estado_servidor == "D":
        sim1.estado_servidor = "O"
        sim1.lista_eventos[1] = re.reloj + np.random.exponential(1/sim1.tm_servicio)
        sim1.ts_acumulado += (sim1.lista_eventos[1] - re.reloj)
        sim1.completaron_demora += 1    
        #grafica  
        sim1.relojEnT.append(re.reloj)  
        sim1.cliColaEnT.append(sim1.nro_clientes_cola)
        sim1.tsAcuEnT.append(sim1.ts_acumulado)
    else:
        sim1.area_q_t += sim1.nro_clientes_cola * (re.reloj - sim1.tiempo_ultimo_evento)
        sim1.nro_clientes_cola += 1
        sim1.cola.append(re.reloj)
        #grafica
        sim1.cliColaEnT.append(sim1.nro_clientes_cola)
        sim1.relojEnT.append(re.reloj)
        sim1.tsAcuEnT.append(sim1.ts_acumulado)

def arribo2():
    if re.reloj != 0:    
        if sim1.lista_eventos[0]<sim2.lista_eventos[0]:
            re.reloj = sim1.lista_eventos[0]
        else:
            re.reloj= sim2.lista_eventos[0]
    sim2.lista_eventos[0] = re.reloj + np.random.exponential(1/sim2.tm_entre_arribos)
    if sim2.estado_servidor == "D":
        sim2.estado_servidor = "O"
        sim2.lista_eventos[1] = re.reloj + np.random.exponential(1/sim2.tm_servicio)
        sim2.ts_acumulado += (sim2.lista_eventos[1] - re.reloj)
        sim2.completaron_demora += 1    
        #grafica  
        sim2.relojEnT.append(re.reloj)  
        sim2.cliColaEnT.append(sim2.nro_clientes_cola)
        sim2.tsAcuEnT.append(sim2.ts_acumulado)
    else:
        sim2.area_q_t += sim2.nro_clientes_cola * (re.reloj - sim2.tiempo_ultimo_evento)
        sim2.nro_clientes_cola += 1
        sim2.cola.append(re.reloj)
        #grafica
        sim2.cliColaEnT.append(sim2.nro_clientes_cola)
        sim2.relojEnT.append(re.reloj)
        sim2.tsAcuEnT.append(sim2.ts_acumulado)


def partida1():
    if sim1.nro_clientes_cola > 0:
        sim1.lista_eventos[1] = re.reloj + np.random.exponential(1/sim1.tm_servicio)
        sim1.demora_acumulada += re.reloj - sim1.cola[0]
        sim1.completaron_demora += 1
        sim1.ts_acumulado += sim1.lista_eventos[1] - re.reloj
        sim1.area_q_t += (sim1.nro_clientes_cola * (re.reloj - sim1.tiempo_ultimo_evento))
        sim1.nro_clientes_cola -= 1
        sim1.cola.pop(0)
        #grafica
        sim1.cliColaEnT.append(sim1.nro_clientes_cola)
        sim1.relojEnT.append(re.reloj)
        sim1.tsAcuEnT.append(sim1.ts_acumulado)
    else:
        sim1.estado_servidor = "D"
        sim1.lista_eventos[1] = 99999999
        #grafica
        sim1.relojEnT.append(re.reloj)
        sim1.cliColaEnT.append(sim1.nro_clientes_cola)
        sim1.tsAcuEnT.append(sim1.ts_acumulado)
        
def partida2():
    if sim2.nro_clientes_cola > 0:
        sim2.lista_eventos[1] = re.reloj + np.random.exponential(1/sim2.tm_servicio)
        sim2.demora_acumulada += re.reloj - sim2.cola[0]
        sim2.completaron_demora += 1
        sim2.ts_acumulado += sim2.lista_eventos[1] - re.reloj
        sim2.area_q_t += (sim2.nro_clientes_cola * (re.reloj - sim2.tiempo_ultimo_evento))
        sim2.nro_clientes_cola -= 1
        sim2.cola.pop(0)
        #grafica
        sim2.cliColaEnT.append(sim2.nro_clientes_cola)
        sim2.relojEnT.append(re.reloj)
        sim2.tsAcuEnT.append(sim2.ts_acumulado)
    else:
        sim2.estado_servidor = "D"
        sim2.lista_eventos[1] = 99999999
        #grafica
        sim2.relojEnT.append(re.reloj)
        sim2.cliColaEnT.append(sim2.nro_clientes_cola)
        sim2.tsAcuEnT.append(sim2.ts_acumulado)

"""
def nro_prom_clientes_cola():
    if sim.reloj != 0:
        nro_clientes_prom_cola = sim.area_q_t/sim.reloj
        return nro_clientes_prom_cola
    else:
        nro_clientes_prom_cola = 0
        return nro_clientes_prom_cola

def utilizacion_prom_servidor():
    if sim.reloj != 0:
        utilizacion_prom_servidor = sim.ts_acumulado/sim.reloj
        return utilizacion_prom_servidor
    else:
        utilizacion_prom_servidor = 0
        return utilizacion_prom_servidor

def demora_prom_cliente():
    if sim.completaron_demora != 0:
        demora_prom_cliente = sim.demora_acumulada/sim.completaron_demora
        return demora_prom_cliente
    else:
        demora_prom_cliente = 0
        return demora_prom_cliente

def graficaPromCliEnCola():
    media = []
    for i in range(len(sim.cliColaEnT)):
        media.append(sim.cliColaEnT[i]/sim.relojEnT[i])
    plt.title('Clientes en cola en un tiempo "t"')    
    plt.plot(sim.relojEnT,sim.cliColaEnT)
    plt.plot(sim.relojEnT,media)
    plt.xlabel('tiempo')    
    plt.ylabel('clientes en "t"')
    plt.show()

def graficaUtiServidor():
    uti = []
    for i in range(len(sim.relojEnT)):
        uti.append(sim.tsAcuEnT[i]/sim.relojEnT[i])   
    plt.title('Utilización del servidor')
    plt.plot(sim.relojEnT,uti)    
    plt.ylabel('Utilización del servidor')
    plt.xlabel('tiempo')
    plt.show()


def reportes():
    print(" Estadísticos ".center(101,'='),'\n')
    print(("Cantidad promedio de clientes en cola: "+ str(nro_prom_clientes_cola())).center(100,' '))
    print(("Utilizacion promedio del servidor: "+ str(utilizacion_prom_servidor())).center(100,' ')) 
    print(("Demora promedio de cliente: "+ str(demora_prom_cliente())).center(100,' '))
    #graficas
    graficaPromCliEnCola()
    graficaUtiServidor()
    
"""
   
if __name__ == '__main__':
    re = R()
    run()



#prueba para GitHub