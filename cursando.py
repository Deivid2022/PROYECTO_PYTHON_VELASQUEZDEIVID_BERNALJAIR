import json

def notas():
    with open('aulas.json','r') as archivo:
        data_aulas = json.load(archivo)
    with open('cursando.json','r') as archivo:
        data_notas = json.load(archivo)
    
    estudiantes = []

    for grupo in data_aulas['aulas']:
        for grupo_estudiantes in data_aulas['aulas'][grupo].values():
            estudiantes.extend(grupo_estudiantes)

    # Guardar la información de los estudiantes en cursando.json
    data_notas['cursando'] = estudiantes
    with open('cursando.json', 'w') as archivo:
        json.dump(data_notas, archivo, indent=4)

# Llamar a la función para mostrar y guardar la información de los estudiantes
notas()

