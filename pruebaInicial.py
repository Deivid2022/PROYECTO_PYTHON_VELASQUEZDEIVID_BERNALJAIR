def pruebaInicial():
    import json 
    
    with open('Inscritos.json','r') as archivo:
        datos = json.load(archivo)
    inscritos = datos['datos']['Inscripcion']
    id_camper = int(input('Ingresa el id del camper: '))
    for inscrito in inscritos:
        if inscrito['id'] == id_camper:
            