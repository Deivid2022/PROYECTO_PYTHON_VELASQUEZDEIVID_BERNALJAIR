def distribucionAulas():
    import json
    with open('aprobadosYreprobados.json', 'r') as archivo:
        data_aprobados = json.load(archivo)
    with open('aulas.json', 'r') as archivo:
        data_aulas = json.load(archivo)

    aprobados = data_aprobados['inscritos']['aprobados']
    
    ids_utilizados = []
    for grupo in data_aulas['aulas']:
        for salon in data_aulas['aulas'][grupo]:
            for asignado in data_aulas['aulas'][grupo][salon]:
                ids_utilizados.append(asignado['identidad'])
    
    id_camper = int(input('Ingresa el número de identidad del camper: '))
    
    if id_camper in ids_utilizados:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return

    Aula = input('Ingresa el aula donde se va establecer el camper (Aula1, Aula2, Aula3): ').capitalize()
    if Aula not in ['Aula1', 'Aula2', 'Aula3']:
        print('Aula inválida. Por favor ingresa una aula válida.')
        return

    if Aula == 'Aula1':
        print('Grupos: P1(6 a 10), P2(10 a 2), P3(2 a 6), P4(6 a 10)')
    elif Aula == 'Aula2':
        print('Grupos: M1(6 a 10), M2(10 a 2), M3(2 a 6), M4(6 a 10)')
    elif Aula == 'Aula3':
        print('Grupos: J1(6 a 10), J2(10 a 2), J3(2 a 6), J4(6 a 10)')

    salon = input('Ingrese el horario en donde quieres asignar el camper: ').upper()

    capacidad = 33
    
    if Aula in data_aulas['aulas'] and salon in data_aulas['aulas'][Aula]:
        if len(data_aulas['aulas'][Aula][salon]) >= capacidad:
            print('Salón lleno. No se puede asignar más estudiantes.')
        else:
            for aprobado in aprobados:
                if aprobado['identidad'] == id_camper:
                    asignar = {
                        'identidad': id_camper,
                        'nombre': aprobado['nombre'],
                        'apellido1': aprobado['apellido1'],
                        'apellido2': aprobado['apellido2'],
                        'estado': 'Cursando'
                    }

                    data_aulas['aulas'][Aula][salon].append(asignar)
                    with open('aulas.json', 'w') as archivo:
                        json.dump(data_aulas, archivo, indent=4)

                    print('Estudiante asignado exitosamente al salón', salon)
                    return

            print('No se encontró ningún estudiante con este número de identidad.')
    else:
        print('El aula o el horario ingresado no es válido.')

distribucionAulas()
