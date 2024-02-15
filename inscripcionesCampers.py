import os
import json

def validarIden(identidad):
    if identidad == "":
        return False
    try:
        identidad = int(identidad) 
        if identidad > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def validarEdad(edad):
    try:
        edad = int(edad)
        if 16 <= edad <= 28:
            return True
        else:
            return False
    except ValueError:
        return False

def inscripciones():
    
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    estado = 'Inscrito'
    nueva_inscripcion = {}
    identidad = input('Ingresa el número de identidad del camper: ')
    while not validarIden(identidad):
        print('El número de identidad debe ser un entero positivo.')
        identidad = input('Ingresa el número de identidad del camper: ')
    nueva_inscripcion['identidad'] = int(identidad)
    nueva_inscripcion['nombre'] = input('Ingresa el nombre del camper: ')
    nueva_inscripcion['apellido1'] = input('Ingrese el primer apellido del camper: ')
    nueva_inscripcion['apellido2'] = input('Ingrese el segundo apellido del camper: ')
    nueva_inscripcion['direccion'] = input('Ingrese la direccion del camper: ')
    edad = input('Ingrese la edad del camper: ')
    while not validarEdad(edad):
        print('La edad debe estar entre 16 y 28 años.')
        edad = input('Ingrese la edad del camper: ')
    nueva_inscripcion['edad'] = int(edad)
    if nueva_inscripcion['edad'] <= 17:
        nueva_inscripcion['acudiente'] = input('Ingrese el nombre del acudiente del camper: ')
        celular_acudiente = input('Ingrese el número de celular del acudiente: ')
        while not validarIden(celular_acudiente):
            print('El número de celular del acudiente debe ser un entero positivo.')
            celular_acudiente = input('Ingrese el número de celular del acudiente: ')
        nueva_inscripcion['celular_acudiente'] = int(celular_acudiente)
    else:
        nueva_inscripcion['acudiente'] = None
        nueva_inscripcion['celular_acudiente'] = None

    celular = input('Ingresa el número de celular del camper: ')
    while not validarIden(celular):
        print('El número de celular debe ser un entero positivo.')
        celular = input('Ingresa el número de celular: ')
    nueva_inscripcion['celular'] = int(celular)
    telefono = input('Ingrese el número fijo: ')
    while not validarIden(telefono):
        print('El número fijo debe ser un entero positivo.')
        telefono = input('Ingrese el número fijo: ')
    nueva_inscripcion['telefono'] = int(telefono)
    nueva_inscripcion['estado'] = estado
    
    
    datos_json['datos']['Inscripcion'].append(nueva_inscripcion)
    with open(ruta,'w') as archivo:
        json.dump(datos_json,archivo,indent=4)
      

def actualizar_campers():
    ruta = os.path.join(os.path.dirname(__file__), 'InscritosCampers.json')
    with open(ruta,'r') as archivo:
        datos_json = json.load(archivo)
    campers = datos_json["datos"]["Inscripcion"]
    identidad = input("Ingresa el id del Camper que quieras actualizar: ")
    try:
        identidad = int(identidad)
    except ValueError:
        print('El id del Camper debe ser un número válido.')
    for camper in campers:
        if camper['identidad'] == identidad:
            preguntas = {
                'identidad': ('Ingresa el número de identidad del camper: ', validarIden),
                'nombre': ('Ingresa el nombre del camper: ', None),
                'apellido1': ('Ingrese el primer apellido del camper: ', None),
                'apellido2': ('Ingrese el segundo apellido del camper: ', None),
                'direccion': ('Ingrese la direccion del camper: ', None),
                'edad': ('Ingrese la edad del camper: ', validarEdad),
                'acudiente': ('Ingrese el nombre del acudiente del camper: ', None),
                'celular_acudiente': ('Ingrese el número de celular del acudiente: ', validarIden),
                'celular': ('Ingresa el número de celular del camper: ', validarIden),
                'telefono': ('Ingrese el número fijo: ', validarIden),
                'estado': ('Ingrese el estado del camper: ', None)
            }
            for clave, valor in preguntas.items():
                mensaje, validacion = valor
                nuevo_dato = input(mensaje)
                if validacion:
                    while not validacion(nuevo_dato):
                        print(f'El {clave} debe ser válido.')
                        nuevo_dato = input(mensaje)
                if clave in ['identidad', 'edad', 'celular_acudiente', 'celular', 'telefono']:
                    nuevo_dato = int(nuevo_dato)
                camper[clave] = nuevo_dato
            print(f'Se ha actualizado el camper con id {identidad}')
            break
    else:
        print(f'No se encontró ningún camper con id {identidad}')
    with open(ruta, 'w') as archivo:
        json.dump(datos_json, archivo, indent=4)


def buscar():
    identidad = input("Ingresa el id del Camper que quieras buscar: ")
    try:
        identidad = int(identidad)
    except ValueError:
        print('El id del Camper debe ser un número válido.')
    return identidad

def mostrar_datos(ruta):
  with open(ruta, 'r') as archivo:
    datos_json = json.load(archivo)
  campers = datos_json["datos"]["Inscripcion"]
  for camper in campers:
    print(f"Id: {camper['identidad']}")
    print(f"Nombre: {camper['nombre']}")
    print(f"Apellido 1: {camper['apellido1']}")
    print(f"Apellido 2: {camper['apellido2']}")
    print(f"Dirección: {camper['direccion']}")
    print(f"Edad: {camper['edad']}")
    print(f"Acudiente: {camper['acudiente']}")
    print(f"Celular acudiente: {camper['celular_acudiente']}")
    print(f"Celular: {camper['celular']}")
    print(f"Teléfono: {camper['telefono']}")
    print(f"Estado: {camper['estado']}")
    print()
    
inscripciones()
#actualizar_campers()
#buscar()
#mostrar_datos()

