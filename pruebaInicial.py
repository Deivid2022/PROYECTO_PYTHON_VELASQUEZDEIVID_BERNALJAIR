def pruebaInicial():
    import json 
    
    with open('Inscritos.json','r') as archivo:
        datos = json.load(archivo)
    with open('aprobados.json','r') as archivo:
        datos2 = json.load(archivo)
    while len(datos2['aprobados']['P1']) <= 33:
        inscritos = datos['datos']['Inscripcion']
        id_camper = int(input('Ingresa el id del camper: '))
        aprobados = {}
        estado = 'Aprobado'
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
        
        datos2['aprobados']['P1'].append(aprobados)
        with open('aprobados.json','w') as archivo:
            json.dump(datos2,archivo,indent=4)

pruebaInicial()