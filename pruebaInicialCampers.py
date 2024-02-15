def pruebaInicial():
    import json
    
    # Cargar datos de los archivos JSON
    with open('InscritosCampers.json', 'r') as archivo:
        datos_inscritos = json.load(archivo)
        
    with open('aprobadosYreprobados.json', 'r') as archivo:
        datos_aprobados_reprobados = json.load(archivo)
    
    inscritos = datos_inscritos['datos']['Inscripcion']  
    aprobados = datos_aprobados_reprobados['inscritos']['aprobados'] 
    reprobados = datos_aprobados_reprobados['inscritos']['reprobados']
    
    id_camper = int(input('Ingresa el número de identidad del camper: '))
        
    ids_utilizados = [aprobad['identidad'] for aprobad in aprobados]
    ids_utilizados2 = [reprobado['identidad'] for reprobado in reprobados]

    if id_camper in ids_utilizados:
        print("Este ID ya ha sido registrado. Por favor, ingresa un ID diferente.")
        return
        
    if id_camper in ids_utilizados2:
        print("Este ID ya ha sido registrado. Por favor, ingresa un ID diferente.")
        return
        
    estado = 'Aprobado'
    estadoR = 'Reprobado'
    
    for inscrito in inscritos:
        if inscrito['identidad'] == id_camper:
            notaPractica = int(input('Ingrese la nota de la prueba práctica: '))
            notaTeorica = int(input('Ingrese la nota de la prueba teórica: '))
            notafinal = (notaPractica + notaTeorica) / 2
            nuevo_estudiante = {
                'identidad': inscrito['identidad'],
                'nombre': inscrito['nombre'],
                'apellido1': inscrito['apellido1'],
                'apellido2': inscrito['apellido2'],
                'estado': estado if notafinal >= 60 else estadoR
            }
            # Agregar estudiante a la lista correspondiente
            if nuevo_estudiante['estado'] == 'Aprobado':
                datos_aprobados_reprobados['inscritos']['aprobados'].append(nuevo_estudiante)
                inscrito['estado'] = 'Cursando'
            else:
                datos_aprobados_reprobados['inscritos']['reprobados'].append(nuevo_estudiante)
            
            

    # Actualizar los archivos JSON
    with open('InscritosCampers.json', 'w') as archivo:
        json.dump(datos_inscritos, archivo, indent=4)  
    
    with open('aprobadosYreprobados.json', 'w') as archivo:
        json.dump(datos_aprobados_reprobados, archivo, indent=4)  

pruebaInicial()
