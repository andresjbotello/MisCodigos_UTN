import requests

# Objeto JSON enviado a random.org para solicitar los numeros aleatorios
data = {
    "jsonrpc": "2.0",
    "method": "generateDecimalFractions",
    "params": {
        "apiKey": "5e08badb-42c8-4d33-9433-40ff13fd4cc3", # API Key generada para un usuario de random.org. Es gratis.
        "n": 10,                                          # Cantidad de numeros solicitados
        "decimalPlaces": 16,                                         
        "replacement": True
    },
    "id": 42
}
r = requests.post('https://api.random.org/json-rpc/1', json=data)

print("Codigo de respuesta solicitud HTTP: " + str(r.status_code))
# print(r.json())

# Formato del JSON de respuesta
# {
#     "jsonrpc": "2.0",
#     "result": {
#     	"random": {
#             "data": [
#                 1, 5, 4, 6, 6, 4
#             ],
#             "completionTime": "2011-10-10 13:19:12Z"
#         },
#         "bitsUsed": 16,
#         "bitsLeft": 199984,
#         "requestsLeft": 9999,
#         "advisoryDelay": 0
#     },
#     "id": 42
# }
# datastore = json.loads(str(r.json()))
mi_JSON = r.json()

# En arreglo valores estan los valores obtenidos desde random.org
arreglo_valores = mi_JSON["result"]["random"]["data"]
print(arreglo_valores)