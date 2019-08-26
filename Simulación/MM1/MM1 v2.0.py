import numpy as np 
from matplotlib import pyplot as plt

class sim():
    reloj, ts_acumulado, demora_acumulada, area_q_t, tiempo_ultimo_evento = 0.0,0.0,0.0,0.0,0.0
    nro_clientes_cola, completaron_demora, paso = 0,0,0
    tm_entre_arribos = 7.0
    tm_servicio = 9.0
    iniciado = False
    estado_servidor = "" #D - disponible | O - ocupado
    proximo_evento = ""  #A - Arribo | P - partida
    lista_eventos = []
    cola = []
    #las listas siguientes se utilizan sólo con el fin de generar las gráficas
    cliColaEnT = []
    relojEnT = []
    tsAcuEnT = []

def inicializar():
    sim.estado_servidor = "D"
    sim.proximo_evento = ""
    sim.reloj, sim.ts_acumulado, sim.demora_acumulada, sim.area_q_t, sim.tiempo_ultimo_evento = 0.0,0.0,0.0,0.0,0.0
    sim.nro_clientes_cola, sim.completaron_demora, sim.paso = 0,0,0
    
    #Tiempo del primer arribo
    sim.lista_eventos.append(np.random.exponential(sim.tm_entre_arribos))

    #Numero grande para asegurar que el primer evento sea un arribo
    sim.lista_eventos.append(99999999)
    sim.iniciado = False

def run():
    print("Inicializando simulacion")
    inicializar()
    while sim.reloj < 5000:
        print("reloj: "+ str(sim.reloj))
        tiempos()
        
        if sim.proximo_evento == "A":
            arribo()
        else:
            partida()

    reportes()

def tiempos():
    sim.tiempo_ultimo_evento = sim.reloj
    if sim.lista_eventos[0] <= sim.lista_eventos[1]:
        sim.reloj = sim.lista_eventos[0]
        sim.proximo_evento = "A"
    else:
        sim.reloj = sim.lista_eventos[1]
        sim.proximo_evento = "P"

def arribo():
    sim.lista_eventos[0] = sim.reloj + np.random.exponential(sim.tm_entre_arribos)
    if sim.estado_servidor == "D":
        sim.estado_servidor = "O"
        sim.lista_eventos[1] = sim.reloj + np.random.exponential(sim.tm_servicio)
        sim.ts_acumulado += (sim.lista_eventos[1] - sim.reloj)
        sim.completaron_demora += 1    
        #grafica  
        sim.relojEnT.append(sim.reloj)  
        sim.cliColaEnT.append(sim.nro_clientes_cola)
        sim.tsAcuEnT.append(sim.ts_acumulado)
    else:
        sim.area_q_t += sim.nro_clientes_cola * (sim.reloj - sim.tiempo_ultimo_evento)
        sim.nro_clientes_cola += 1
        sim.cola.append(sim.reloj)
        #grafica
        sim.cliColaEnT.append(sim.nro_clientes_cola)
        sim.relojEnT.append(sim.reloj)
        sim.tsAcuEnT.append(sim.ts_acumulado)


def partida():
    if sim.nro_clientes_cola > 0:
        sim.lista_eventos[1] = sim.reloj + np.random.exponential(sim.tm_servicio)
        sim.demora_acumulada += sim.reloj - sim.cola[0]
        sim.completaron_demora += 1
        sim.ts_acumulado += sim.lista_eventos[1] - sim.reloj
        sim.area_q_t += (sim.nro_clientes_cola * (sim.reloj - sim.tiempo_ultimo_evento))
        sim.nro_clientes_cola -= 1
        sim.cola.pop(0)
        #grafica
        sim.cliColaEnT.append(sim.nro_clientes_cola)
        sim.relojEnT.append(sim.reloj)
        sim.tsAcuEnT.append(sim.ts_acumulado)
    else:
        sim.estado_servidor = "D"
        sim.lista_eventos[1] = 99999999
        #grafica
        sim.relojEnT.append(sim.reloj)
        sim.cliColaEnT.append(sim.nro_clientes_cola)
        sim.tsAcuEnT.append(sim.ts_acumulado)

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
    

   
if __name__ == '__main__':
    run()