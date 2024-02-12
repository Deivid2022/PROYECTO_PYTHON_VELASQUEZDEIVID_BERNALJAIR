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
        if 18 <= edad:
            return True
        else:
            return False
    except ValueError:
        return False 

def Coordinadores():
    
    import json
    
    with open('coordinadores.json','r') as archivo:
        data = json.load(archivo)
    ultimo_id = max([trainer['id'] for trainer in data['coordinadores']]) if data['coordinadores']else 0
    nuevo_id = ultimo_id + 1
    nueva_inscripcion = {}
    nueva_inscripcion['id'] = nuevo_id 
    identidad = input('Ingresa el número de identidad del coordinador: ')
    while not validarIden(identidad):
        print('El número de identidad debe ser un entero positivo.')
        identidad = input('Ingresa el número de identidad del coordinador: ')
    nueva_inscripcion['identidad'] = int(identidad)
    nueva_inscripcion['nombre'] = input('Ingresa el nombre del coordinador: ')
    nueva_inscripcion['apellido1'] = input('Ingrese el primer apellido del coordinador: ')
    nueva_inscripcion['apellido2'] = input('Ingrese el segundo apellido del coordinador: ') 
    nueva_inscripcion['direccion'] = input('Ingrese la direccion del coordinador: ') 
    edad = input('Ingrese la edad del coordinador: ')
    while not validarEdad(edad): 
        print('La edad debe ser mayor a 18 años.')
        edad = input('Ingrese la edad del coordinador: ')
    nueva_inscripcion['edad'] = int(edad)
    celular = input('Ingresa el número de celular: ')
    while not validarIden(celular):
        print('El número de celular debe ser un entero positivo.')
        celular = input('Ingresa el número de celular: ')
    nueva_inscripcion['celular'] = int(celular) 

    data['coordinadores'].append(nueva_inscripcion)
    with open('coordinadores.json','w') as archivo:
        json.dump(data,archivo,indent=4)
        
Coordinadores()
