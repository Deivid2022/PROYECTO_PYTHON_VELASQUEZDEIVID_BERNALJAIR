def buscarCamper():
    import json
    with open ('aulas.json','r') as archivo:
        data = json.load(archivo)
    
    aula = input('Ingresa el aula donde perteneces: ').capitalize()
    grupo = input('Ingrese el grupo donde pertenece: ').upper()
    
    salos = data['aulas'][aula][grupo]
    id_camper = int(input('Ingresa tu numero de identidad: '))
    for salo in salos:
        if salo['identidad'] == id_camper:
            print(salo)

buscarCamper()