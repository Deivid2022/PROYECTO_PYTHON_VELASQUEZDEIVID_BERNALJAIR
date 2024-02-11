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
    
    import json
    
    with open('Inscritos.json','r') as archivo:
        data = json.load(archivo)
    ultimo_id = max([inscripcion['id'] for inscripcion in data['datos']['Inscripcion']]) if data['datos']['Inscripcion'] else 0

    estado = 'Inscrito'
    nuevo_id = ultimo_id + 1
    nueva_inscripcion = {}
    nueva_inscripcion['id'] = nuevo_id 
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
    if nueva_inscripcion['edad'] == 17:
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
    
    
    data['datos']['Inscripcion'].append(nueva_inscripcion)
    with open('Inscritos.json','w') as archivo:
        json.dump(data,archivo,indent=4)
      
inscripciones()
