import random
import math
import simpy

SEMILLA = 124
NUM_SERVIDORES = 1
TIEMPO_SERVICIO_MIN = 3
TIEMPO_SERVICIO_MAX = 8
T_LLEGADAS = 6
#TIEMPO_SIMULACION = 0
TOT_CLIENTES = 100

te  = 0.0 # tiempo de espera total
dt  = 0.0 # duracion de servicio total
fin = 0.0 # minuto en el que finaliza

def atender(cliente):
	global dt  #Para poder acceder a la variable dt declarada anteriormente
	R = random.random()  # Obtiene un numero aleatorio y lo guarda en R
	tiempo = TIEMPO_SERVICIO_MAX - TIEMPO_SERVICIO_MIN
	tiempo_servicio = TIEMPO_SERVICIO_MIN + (tiempo*R) # Distribucion uniforme
	yield env.timeout(tiempo_servicio) # deja correr el tiempo n minutos
	print(" \o/ %s atendido en %.2f minutos" % (cliente,tiempo_servicio))
	dt = dt + tiempo_servicio # Acumula los tiempos de uso de la i


def cliente (env, name, personal ):
	global te
	global fin
	llega = env.now # Guarda el minuto de llegada del cliente
	print ("---> %s llego en el minuto %.2f" % (name, llega))
	with personal.request() as request: # Espera su turno
		yield request # Obtiene turno
		pasa = env.now # Guarda el minuto cuado comienza a ser atendido
		espera = pasa - llega # Calcula el tiempo que espero
		te = te + espera # Acumula los tiempos de espera
		print ("** %s pasa al servidor para ser atendido en minuto %.2f habiendo esperado %.2f" % (name, pasa, espera))
		yield env.process(atender(name)) # Invoca al proceso atender
		deja = env.now #Guarda el minuto en que termina el proceso atender
		print ("<--- %s se retira en minuto %.2f" % (name, deja))
		fin = deja # Conserva globalmente el ultimo minuto de la simulacion


def principal (env, personal):
	llegada = 0
	i = 0
	for i in range(TOT_CLIENTES): # Para n clientes
		R = random.random()
		llegada = -T_LLEGADAS * math.log(R) # Distribucion exponencial
		yield env.timeout(llegada)  # Deja transcurrir un tiempo entre uno y otro
		i += 1
		env.process(cliente(env, 'Cliente %d' % i, personal))

print ("------------------- Simulacion MM1  ------------------")
random.seed (SEMILLA)  # Cualquier valor
env = simpy.Environment() # Crea el objeto entorno de simulacion
personal = simpy.Resource(env, NUM_SERVIDORES) #Crea los recursos (servidores)
env.process(principal(env, personal)) #Invoca el proceso princial
env.run() #Inicia la simulacion

print ("\n---------------------------------------------------------------------")
print ("\nIndicadores obtenidos: ")

lpc = te / fin
print ("\nLongitud promedio de la cola: %.2f" % lpc)
tep = te / TOT_CLIENTES
print ("Tiempo de espera promedio = %.2f" % tep)
upi = (dt / fin) / NUM_SERVIDORES
print ("Uso promedio de la instalacion = %.2f" % upi)
print ("\n---------------------------------------------------------------------")