import json

def distribucionAulas():
    with open('aprobadosYreprobados.json', 'r') as archivo:
        data_aprobados = json.load(archivo)
    with open('aulas.json', 'r') as archivo:
        data_aulas = json.load(archivo)

    aprobados = data_aprobados['inscritos']['aprobados']
    ids_utilizados = set()

    while aprobados:
        id_camper = int(input('Ingresa el número de identidad del camper: '))
        if id_camper in ids_utilizados:
            print('Este ID ya ha sido registrado. Por favor ingrese otro')
            continue

        ids_utilizados.add(id_camper)
        Aula = input('Ingresa el aula donde se va establecer el camper(Aula1,Aula2,Aula3): ').capitalize()
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
            continue

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

        # Remover al estudiante de la lista de aprobados
        aprobados = [aprobado for aprobado in aprobados if aprobado['identidad'] != id_camper]

        with open('aulas.json', 'w') as archivo:
            json.dump(data_aulas, archivo, indent=4)

        print('Estudiante asignado exitosamente al salón', salon)

distribucionAulas()
