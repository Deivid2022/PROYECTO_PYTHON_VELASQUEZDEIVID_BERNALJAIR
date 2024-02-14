def camperEstadoInscrito():
    import json
    
    with open('InscritosCampers.json','r') as archivo:
        data = json.load(archivo)
        inscritos = data['datos']['Inscripcion']
        print('Campers en estado de inscripcion')
        for i in inscritos:
            print(i)
        
#camperEstadoInscrito()

def camperEstadoAprobado():
    import json
    with open('aprobadosYreprobados.json','r') as archivo:
        data = json.load(archivo)
        aprobados = data['inscritos']['aprobados']
        print('Campers que aprobaron el examen Inicial')
        for i in aprobados:
            print(i)

#camperEstadoAprobado()

def Trainers():
    import json
    
    with open('Trainers.json','r') as archivo:
        data = json.load(archivo)
        trainers = data['Trainers']
        print('Entrenadores que se encuentran en Campusland')
        for i in trainers:
            print(i)

#Trainers()

def bajoRendimiento():
    import json 
    
    with open('aulas.json','r') as archivo:
        data = json.load(archivo)
    aulap1 = data['aulas']['Aula1']['P1']
    aulap2 = data['aulas']['Aula1']['P2']
    aulap3 = data['aulas']['Aula1']['P3']
    aulap4 = data['aulas']['Aula1']['P4']
    aulam1 = data['aulas']['Aula2']['M1']
    aulam2 = data['aulas']['Aula2']['M2']
    aulam3 = data['aulas']['Aula2']['M3']
    aulam4 = data['aulas']['Aula2']['M4']
    aulaj1 = data['aulas']['Aula3']['J1']
    aulaj2 = data['aulas']['Aula3']['J2']
    aulaj3 = data['aulas']['Aula3']['J3']
    aulaj4 = data['aulas']['Aula3']['J4']
    
    for aula in aulap1:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulap2:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulap3:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulap4:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulam1:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulam2:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulam3:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulam4:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulaj1:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulaj2:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulaj3:
        if aula['riesgo'] == 'Alto':
            print(aula)
    for aula in aulaj4:
        if aula['riesgo'] == 'Alto':
            print(aula)

#bajoRendimiento()

def CamperFuncion():
    import json
    with open('aulas.json','r') as archivo:
        data =  json.load(archivo)
    with open('Trainers.json','r') as archivo:
        data_trainer = json.load(archivo)
        
    trainer = data_trainer['Trainers']
        
    aulap1 = data['aulas']['Aula1']['P1']
    aulap2 = data['aulas']['Aula1']['P2']
    aulap3 = data['aulas']['Aula1']['P3']
    aulap4 = data['aulas']['Aula1']['P4']
    aulam1 = data['aulas']['Aula2']['M1']
    aulam2 = data['aulas']['Aula2']['M2']
    aulam3 = data['aulas']['Aula2']['M3']
    aulam4 = data['aulas']['Aula2']['M4']
    aulaj1 = data['aulas']['Aula3']['J1']
    aulaj2 = data['aulas']['Aula3']['J2']
    aulaj3 = data['aulas']['Aula3']['J3']
    aulaj4 = data['aulas']['Aula3']['J4']
    
    
    for aula in aulap1:
        if aula['trainer'] == trainer['nombre']:
            print(aula) 

CamperFuncion()