def pruebaInicial():
    import json 
    
    with open('InscritosCampers.json', 'r') as archivo:
        datos = json.load(archivo)
    with open('aprobadosYreprobados.json', 'r') as archivo:
        datos2 = json.load(archivo)
    
    inscritos = datos['datos']['Inscripcion']  
    
    ids_utilizados = set()  
    
    # Continuar el bucle mientras haya inscritos por procesar
    while inscritos:
        
        id_camper = int(input('Ingresa el ID del camper: '))
        
     
        if id_camper in ids_utilizados:
            print("Este ID ya ha sido registrado. Por favor, ingresa un ID diferente.")
            continue  
        
        ids_utilizados.add(id_camper)  
        
        aprobados = {}
        estado = 'Aprobado'
        estadoR = 'Reprobado'
        
        for inscrito in inscritos:
            if inscrito['id'] == id_camper:
                notaPractica = int(input('Ingrese la nota de la prueba practica: '))
                notaTeorica = int(input('Ingrese la nota de la prueba teorica: '))
                notafinal = (notaPractica + notaTeorica)/2
                if notafinal >= 60:
                    aprobados['identidad'] = inscrito['identidad']
                    aprobados['nombre'] = inscrito['nombre']
                    aprobados['apellido1'] = inscrito['apellido1']
                    aprobados['apellido2'] = inscrito['apellido2']
                    aprobados['estado'] = estado 
                    datos2['inscritos']['aprobados'].append(aprobados)
                else:
                    aprobados['identidad'] = inscrito['identidad']
                    aprobados['nombre'] = inscrito['nombre']
                    aprobados['apellido1'] = inscrito['apellido1']
                    aprobados['apellido2'] = inscrito['apellido2']
                    aprobados['estado'] = estadoR
                    datos2['inscritos']['reprobados'].append(aprobados)
        
        
        # Eliminar el inscrito actual de la lista
        inscritos = [inscrito for inscrito in inscritos if inscrito['id'] != id_camper]
        
        with open('aprobadosYreprobados.json', 'w') as archivo:
            json.dump(datos2, archivo, indent=4)  

pruebaInicial()
