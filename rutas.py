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
        
        ruta = input('Ingresa la ruta de este grupo: ').capitalize()
        Trainer = int(input('Ingrese el numero de identidad del Trainer: '))
        fechaInicio = input('Ingresa la fecha de inicio: ')
        fechaFinal = input('Ingresa la fecha de finalización: ')
        for estudiante in data_aulas['aulas'][aula][grupo]:
            for trainer in trainers:
                if trainer['identidad'] == Trainer:
                    estudiante['ruta'] = ruta
                    estudiante['trainer'] = trainer['nombre']
                    estudiante['Grupo'] = grupo
                    estudiante['Fecha de Inicio'] = fechaInicio
                    estudiante['Fecha de Finalizacion'] = fechaFinal
                    estudiante['Fundamentos de programacion'] = ""
                    estudiante['Programacion Web'] = ""
                    estudiante['Programacion formal'] = ""
                    estudiante['Bases de datos'] = ""
                    estudiante['Backend'] = ""
                    
        with open('aulas.json','w') as archivo:
            json.dump(data_aulas, archivo, indent=4)

        print(f'Ruta asignada exitosamente a todos los campers del grupo {grupo} en el aula {aula}.')
    else:
        print('El aula o el grupo ingresado no es válido.')

rutas()
