import json

with open('data.json', 'r') as archivo:
        datos = json.load(archivo)

nuevo_cliente = {}
nuevo_cliente['id'] = int(input('Ingrese el ID del nuevo cliente: '))
nuevo_cliente['nombre'] = input('Ingrese el nombre del nuevo cliente: ')
nuevo_cliente['apellido1'] = input('Ingrese el primer apellido del nuevo cliente: ')
nuevo_cliente['apellido2'] = input('Ingrese el segundo apellido del nuevo cliente (opcional): ')
nuevo_cliente['ciudad'] = input('Ingrese la ciudad del nuevo cliente: ')
nuevo_cliente['categoria'] = int(input('Ingrese la categoría del nuevo cliente: '))

datos["ventas"]["clientes"].append(nuevo_cliente)

with open('data.json', 'w') as archivo:
    json.dump(datos, archivo,indent=4) 