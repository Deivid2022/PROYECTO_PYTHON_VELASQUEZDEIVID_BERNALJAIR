def rutas():
    import json

    with open('aulas.json','r') as archivo:
        data_aulas = json.load(archivo)
    with open('Trainers.json','r') as archivo:
        data_trainer = json.load(archivo)
    trainers = data_trainer['Trainers']
    
    
    
    aula = input('Ingresa el aula donde está el grupo: ').capitalize()
    grupo = input('Ingresa el grupo al que le quieres asignar la ruta: ').upper()
    
    if aula in data_aulas['aulas'] and grupo in data_aulas['aulas'][aula]:
        
        ruta = input('Ingresa la ruta de este grupo: ')
        Trainer = int(input('Ingrese el numero de identidad del Trainer: '))
        
        for estudiante in data_aulas['aulas'][aula][grupo]:
            for trainer in trainers:
                if trainer['identidad'] == Trainer:
                    estudiante['ruta'] = ruta
                    estudiante['trainer'] = trainer['nombre']
        with open('aulas.json','w') as archivo:
            json.dump(data_aulas, archivo, indent=4)

        print(f'Ruta asignada exitosamente a todos los campers del grupo {grupo} en el aula {aula}.')
    else:
        print('El aula o el grupo ingresado no es válido.')

rutas()
