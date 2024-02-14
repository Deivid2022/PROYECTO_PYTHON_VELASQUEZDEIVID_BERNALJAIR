import json

def cargar_inscritos():
    with open('inscritosCampers.json', 'r', encoding='utf8') as file:
        data = json.load(file)
    return data['datos']['Inscripcion']

def actualizar_notas_y_rendimiento(identidad):
    with open('notas.json', 'r', encoding='utf8') as file:
        notas = json.load(file)

    campers = notas['Notas']['Cursando']

    for camper in campers:
        if camper['identidad'] == identidad:
            while True:
                materia = seleccionar_materia()
                if materia is None:
                    return
                if materia not in camper:
                    camper[materia] = {}

                prueba_teorica = obtener_nota('prueba teórica', materia)
                prueba_practica = obtener_nota('prueba práctica', materia)
                promedio_quiz = obtener_promedio('quiz', materia)
                promedio_trabajos = obtener_promedio('trabajo', materia)

                total_talleres = (promedio_quiz + promedio_trabajos) / 2 * 0.1
                nota_final = prueba_practica + prueba_teorica + total_talleres

                rendimiento = {
                    f'Nota_final_{materia}': nota_final,
                    f'Rendimiento_{materia}': 'Riesgo Bajo' if nota_final >= 60 else 'Riesgo Alto'
                }

                camper[materia].update(rendimiento)

                print(f'Nota final de {materia}: {nota_final}')
                print(f'Rendimiento de {materia}: {"Riesgo Bajo" if nota_final >= 60 else "Riesgo Alto"}')
                print("Volviendo al menú principal...")
                return

def seleccionar_materia():
    materias = ['Fundamentos de Programación', 'Programación Web', 'Programación Formal', 'Bases de Datos', 'Backend']
    print('Seleccione la materia (\'fin\' para terminar):')
    for i, materia in enumerate(materias, start=1):
        print(f'{i}. {materia}')
    opcion = input('-> ')
    if opcion.lower() == 'fin':
        return None
    try:
        indice = int(opcion)
        if 1 <= indice <= len(materias):
            return materias[indice - 1]
        else:
            print('Opción inválida.')
            return seleccionar_materia()
    except ValueError:
        print('Opción inválida.')
        return seleccionar_materia()

def obtener_nota(tipo, materia):
    while True:
        try:
            nota = int(input(f'Digite nota de la {tipo} de 0 a 100 de {materia}: '))
            if 0 <= nota <= 100:
                return nota * 0.3 if tipo == 'prueba teórica' else nota * 0.6
            else:
                print('La nota debe estar entre 0 a 100.')
        except ValueError:
            print('Debe ingresar un número.')

def obtener_promedio(tipo, materia):
    while True:
        try:
            cantidad = int(input(f'Digite la cantidad de {tipo} realizados en {materia}: '))
            notas = [int(input(f'Digite nota del {tipo} #{i + 1} de 0 a 100: ')) for i in range(cantidad)]
            promedio = sum(notas) / cantidad
            if all(0 <= nota <= 100 for nota in notas):
                return promedio
            else:
                print('Las notas deben estar en el rango de 0 a 100.')
        except ValueError:
            print('Debe ingresar números.')

def mostrar_notas():
    with open('notas.json', 'r', encoding='utf8') as file:
        notas = json.load(file)

    campers = notas['Notas']['Cursando']

    print('Mostrando todas las notas guardadas:')
    for camper in campers:
        print(f"Notas para el estudiante con identidad: {camper['identidad']}")
        for materia, notas_materia in camper.items():
            if materia != 'identidad':
                print(f'{materia}:')
                for nota, valor in notas_materia.items():
                    print(f'{nota}: {valor}')
                print('')

# Mostrar menú principal
while True:
    print("\nMenú:")
    print("1. Actualizar notas y rendimiento")
    print("2. Mostrar notas guardadas")
    print("3. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == '1':
        identidad_estudiante = int(input('Digite la identidad del estudiante: '))
        inscritos = cargar_inscritos()
        datos_persona = None
        for persona in inscritos:
            if persona['identidad'] == identidad_estudiante:
                datos_persona = persona
                break

        if datos_persona:
            actualizar_notas_y_rendimiento(identidad_estudiante)
        else:
            print('La identidad ingresada no se encuentra en la lista de inscritos.')
    
    elif opcion == '2':
        mostrar_notas()
    
    elif opcion == '3':
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
