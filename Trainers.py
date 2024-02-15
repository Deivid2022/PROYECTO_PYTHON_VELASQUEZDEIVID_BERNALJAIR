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
    
def leer_trainer():
    with open('Trainers.json','r') as archivo:
        data = json.load(archivo)
        return data
            

def Añadir_trainer():
    with open('Trainers.json', 'r') as archivo:
        data = json.load(archivo)
    
    nuevos_trainers = {}
    identidad = input('Ingresa el número de identidad del Trainer: ')
    while not validarIden(identidad):
        print('El número de identidad debe ser un entero positivo.')
        identidad = input('Ingresa el número de identidad del Trainer: ')
    nuevos_trainers['identidad'] = int(identidad)
    nuevos_trainers['nombre'] = input('Ingresa el nombre del Trainer: ')
    nuevos_trainers['apellido1'] = input('Ingrese el primer apellido del Trainer: ')
    nuevos_trainers['apellido2'] = input('Ingrese el segundo apellido del Trainer: ')
    nuevos_trainers['direccion'] = input('Ingrese la direccion del Trainer: ')
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

def Actualizar_trainer():
    with open('Trainers.json','r') as archivo:
        data = json.load(archivo)
    
    actualizar = data['Trainers']
    id_trainer = int(input('Ingresa el numero de identidad del Trainer que deseas actualizar: '))
    for actualiza in actualizar:
        if actualiza['identidad'] == id_trainer:
            actualiza['identidad'] = int(input('Ingresa el número de identidad: '))
            actualiza['nombre'] = input('Ingresa el nombre del Trainer:')
            actualiza['apellido1'] = input('Ingresa el primer apellido del Trainer: ')
            actualiza['apellido2'] = input('Ingresa el segundo apellido del Trainer: ')
            actualiza['direccion'] = input('Ingresa la direccion del Trainer: ')
            edad = input('Ingresa la edad del Trainer: ')
            while not validarIden(edad):
                print('El número de la edad debe ser un entero positivo.')
                edad = input('Ingresa la edad del Trainer: ')
            actualiza['edad'] = int(edad)
            celular = input('Ingresa el número de celular del Trainer: ')
            while not validarIden(celular):
                print('El número de celular debe ser un entero positivo.')
                celular = input('Ingresa el número de celular: ')
            actualiza['celular'] = int(celular)
    with open('Trainers.json','w') as archivo:
        json.dump(data,archivo,indent=4)
        
def Eliminar_trainer():
    with open('Trainers.json','r') as archivo:
        data = json.load(archivo)
    
    eliminar = data['Trainers']
    id_trianer = int(input('Ingrese el id del Trainer que desea eliminar: '))
    for elimina in eliminar:
        if elimina['identidad'] == id_trianer:
            eliminar.remove(elimina)
    
    with open('Trainers.json','w') as archivo:
        json.dump(data,archivo,indent=4)
    
#print(leer_trainer())
#Actualizar_trainer()
Añadir_trainer()
#Eliminar_trainer()

    
