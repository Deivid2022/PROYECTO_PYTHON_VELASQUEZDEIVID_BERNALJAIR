def inscripciones():
    
    import json
    
    with open('data.json','r') as archivo:
        data = json.load(archivo)
    ultimo_id = max([inscripcion['id'] for inscripcion in data['datos']['Inscripcion']]) if data['datos']['Inscripcion'] else 0


    nuevo_id = ultimo_id + 1
    nueva_inscripcion = {}
    nueva_inscripcion['id'] = nuevo_id 
    nueva_inscripcion['identidad'] = int(input('Ingresa el número de identidad del camper: '))
    nueva_inscripcion['nombre'] = input('Ingresa el nombre del camper: ')
    nueva_inscripcion['apellido1'] = input('Ingrese el primer apellido del camper: ')
    nueva_inscripcion['apellido2'] = input('Ingrese el segundo apellido del camper: ')
    nueva_inscripcion['direccion'] = input('Ingrese la direccion del camper: ')
    nueva_inscripcion['acudiente'] = input('Ingrese el nombre del acudiente del camper(opcional): ')
    nueva_inscripcion['celular'] = int(input('Ingresa el número de celular: '))
    nueva_inscripcion['telefono'] = int(input('Ingrese el número fijo: '))
    
    data['datos']['Inscripcion'].append(nueva_inscripcion)
    with open('data.json','w') as archivo:
        json.dump(data,archivo,indent=4)
        


