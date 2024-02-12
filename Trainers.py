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
    


def Añadir_trainer():
    with open('Trainers.json', 'r') as archivo:
        data = json.load(archivo)
    
    nuevos_trainers = {}
    identidad = input('Ingresa el número de identidad del Trainer: ')
    while not validarIden(identidad):
        print('El número de identidad debe ser un entero positivo.')
        identidad = input('Ingresa el número de identidad del camper: ')
    nuevos_trainers['identidad'] = int(identidad)
    nuevos_trainers['nombre'] = input('Ingresa el nombre del camper: ')
    nuevos_trainers['apellido1'] = input('Ingrese el primer apellido del camper: ')
    nuevos_trainers['apellido2'] = input('Ingrese el segundo apellido del camper: ')
    nuevos_trainers['direccion'] = input('Ingrese la direccion del camper: ')
    edad = input('Ingresa la edad del Trainer: ')
    while not validarIden(edad):
        print('El número de la edad debe ser un entero positivo.')
        edad = input('Ingresa la edad del Trainer: ')
    nuevos_trainers['edad'] = int(edad)
    celular = input('Ingresa el número de celular del Trainer: ')
    while not validarIden(celular):
        print('El número de celular debe ser un entero positivo.')
        celular = input('Ingresa el número de celular: ')
    nuevos_trainers['celular'] = int(celular)
     
    data['Trainers'].append(nuevos_trainers)
    with open('Trainers.json','w') as Archivo:
        json.dump(data,Archivo,indent=4)







Añadir_trainer()

    
