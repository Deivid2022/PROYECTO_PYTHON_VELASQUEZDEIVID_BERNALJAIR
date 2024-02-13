
def pruebaInicial():
    import json
    
    with open('InscritosCampers.json', 'r') as archivo:
        datos = json.load(archivo)
        
    with open('aprobadosYreprobados.json', 'r') as archivo:
        datos2 = json.load(archivo)
    
    inscritos = datos['datos']['Inscripcion']  
    aprobados = datos2['inscritos']['aprobados'] 
    reprobados = datos2['inscritos']['reprobados']
    
    
    id_camper = int(input('Ingresa el numero de identidad del camper: '))
        
    ids_utilizados = [aprobad['identidad'] for aprobad in aprobados]
    ids_utilizados2 = [reprobado['identidad'] for reprobado in reprobados]

    if id_camper in ids_utilizados:
        print("Este ID ya ha sido registrado. Por favor, ingresa un ID diferente.")
        
    if id_camper in ids_utilizados2:
        print("Este ID ya ha sido registrado. Por favor, ingresa un ID diferente.")
        
        
    estado = 'Aprobado'
    estadoR = 'Reprobado'
    
    for inscrito in inscritos:
        if inscrito['identidad'] == id_camper:
            notaPractica = int(input('Ingrese la nota de la prueba practica: '))
            notaTeorica = int(input('Ingrese la nota de la prueba teorica: '))
            notafinal = (notaPractica + notaTeorica)/2
            nuevo_estudiante = {
                'identidad': inscrito['identidad'],
                'nombre': inscrito['nombre'],
                'apellido1': inscrito['apellido1'],
                'apellido2': inscrito['apellido2'],
                'estado': estado if notafinal >= 60 else estadoR
            }
            if nuevo_estudiante['estado'] == 'Aprobado':
                datos2['inscritos']['aprobados'].append(nuevo_estudiante)
            else:
                datos2['inscritos']['reprobados'].append(nuevo_estudiante)

    with open('aprobadosYreprobados.json', 'w') as archivo:
        json.dump(datos2, archivo, indent=4)  

pruebaInicial()
