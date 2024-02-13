

def distribucionAulas():
    import json
    with open('aprobadosYreprobados.json', 'r') as archivo:
        data_aprobados = json.load(archivo)
    with open('aulas.json', 'r') as archivo:
        data_aulas = json.load(archivo)

    aprobados = data_aprobados['inscritos']['aprobados']
    asignados = data_aulas['aulas']['Aula1']['P1']
    ids_utilizados = [asignado['identidad'] for asignado in asignados]
    asignados1 = data_aulas['aulas']['Aula1']['P2']
    ids_utilizados1 = [asignado['identidad'] for asignado in asignados1]
    asignados2 = data_aulas['aulas']['Aula1']['P3']
    ids_utilizados2 = [asignado['identidad'] for asignado in asignados2]
    asignados3 = data_aulas['aulas']['Aula1']['P4']
    ids_utilizados3 = [asignado['identidad'] for asignado in asignados3]
    asignados4 = data_aulas['aulas']['Aula2']['M1']
    ids_utilizados4 = [asignado['identidad'] for asignado in asignados4]
    asignados5 = data_aulas['aulas']['Aula2']['M2']
    ids_utilizados5 = [asignado['identidad'] for asignado in asignados5]
    asignados6 = data_aulas['aulas']['Aula2']['M3']
    ids_utilizados6 = [asignado['identidad'] for asignado in asignados6]
    asignados7 = data_aulas['aulas']['Aula2']['M4']
    ids_utilizados7 = [asignado['identidad'] for asignado in asignados7]
    asignados8 = data_aulas['aulas']['Aula3']['J1']
    ids_utilizados8 = [asignado['identidad'] for asignado in asignados8]
    asignados9 = data_aulas['aulas']['Aula3']['J2']
    ids_utilizados9 = [asignado['identidad'] for asignado in asignados9]
    asignados10 = data_aulas['aulas']['Aula3']['J3']
    ids_utilizados10 = [asignado['identidad'] for asignado in asignados10]
    asignados11 = data_aulas['aulas']['Aula3']['J4']
    ids_utilizados11 = [asignado['identidad'] for asignado in asignados11]
    
    id_camper = int(input('Ingresa el número de identidad del camper: '))
    
    if id_camper in ids_utilizados:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados1:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados2:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados3:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados4:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados5:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados6:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados7:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados8:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados9:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados10:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
    if id_camper in ids_utilizados11:
        print('Este ID ya ha sido registrado. Por favor ingrese otro.')
        return
           

    Aula = input('Ingresa el aula donde se va establecer el camper(Aula1, Aula2, Aula3): ').capitalize()
    if Aula == 'Aula1':
        print('Grupos: P1, P2, P3, P4')
    elif Aula == 'Aula2':
        print('Grupos: M1, M2, M3, M4')
    elif Aula == 'Aula3':
        print('Grupos: J1, J2, J3, J4')

    salon = input('Ingrese el grupo en donde quieres asignar el camper: ').upper()

    capacidad = 33

    if capacidad <= len(data_aulas['aulas'][Aula][salon]):
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
                break


        with open('aulas.json', 'w') as archivo:
            json.dump(data_aulas, archivo, indent=4)

        print('Estudiante asignado exitosamente al salón', salon)

distribucionAulas()
