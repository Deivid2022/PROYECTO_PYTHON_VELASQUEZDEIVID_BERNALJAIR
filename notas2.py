def menu():
    print('Modulos:')
    print('1. Fundamentos de programación')
    print('2. Programación Web')
    print('3. Programación formal')
    print('4. Bases de datos')
    print('5. Backend')


def notas():

    import json

    with open('aulas.json','r') as archivo:
        data = json.load(archivo)
    
    aula = input('Ingresa el aula de donde vas a colocar las notas: ').capitalize()
    grupo = input('Ingresa el grupo donde vas a asignar las notas: ').upper()
    estudiante = data['aulas'][aula][grupo]
    id_camper = int(input('Ingresa el numero de identidad del camper:'))
    
    for cursado in estudiante:
        if cursado['identidad'] == id_camper:
            ruta = cursado['ruta']
            print(f'El estudiante ', {cursado['nombre']}, ' se encuentra en la ruta ',ruta)
            menu()
            num = input('Ingrese la posicion del modulo al que va a agregar las notas: ')
            if num == '1':
                NotaT = int(input('Ingresa la nota teorica: '))
                NotaP = int(input('Ingresa la nota practica: '))
                NotaQ = int(input('Ingrsa el promedio de notas de los quizes y trabajos: '))
                Total = (NotaT*0.3)+(NotaP*0.6)+(NotaQ*0.1)
                if Total >= 60:
                    cursado['Fundamentos de programacion'] = 'Aprobado'
                    cursado['riesgo'] = 'Bajo'
                elif Total < 60:
                    cursado['Fundamentos de programacion'] = 'Reprobado'
                    cursado['riesgo'] = 'Alto'
            elif num == '2':
                NotaT = int(input('Ingresa la nota teorica: '))
                NotaP = int(input('Ingresa la nota practica: '))
                NotaQ = int(input('Ingrsa el promedio de notas de los quizes y trabajos: '))
                Total = (NotaT*0.3)+(NotaP*0.6)+(NotaQ*0.1)
                if Total >= 60:
                    cursado['Programacion Web'] = 'Aprobado'
                    cursado['riesgo'] = 'Bajo'
                elif Total < 60:
                    cursado['Programacion Web'] = 'Reprobado'
                    cursado['riesgo'] = 'Alto'
            elif num == '3':
                NotaT = int(input('Ingresa la nota teorica: '))
                NotaP = int(input('Ingresa la nota practica: '))
                NotaQ = int(input('Ingrsa el promedio de notas de los quizes y trabajos: '))
                Total = (NotaT*0.3)+(NotaP*0.6)+(NotaQ*0.1)
                if Total >= 60:
                    cursado['Programacion formal'] = 'Aprobado'
                    cursado['riesgo'] = 'Bajo'
                elif Total < 60:
                    cursado['Programacion formal'] = 'Reprobado'
                    cursado['riesgo'] = 'Alto'
            elif num == '4':
                NotaT = int(input('Ingresa la nota teorica: '))
                NotaP = int(input('Ingresa la nota practica: '))
                NotaQ = int(input('Ingrsa el promedio de notas de los quizes y trabajos: '))
                Total = (NotaT*0.3)+(NotaP*0.6)+(NotaQ*0.1)
                if Total >= 60:
                    cursado['Bases de datos'] = 'Aprobado'
                    cursado['riesgo'] = 'Bajo'
                elif Total < 60:
                    cursado['Bases de datos'] = 'Reprobados'
                    cursado['riesgo'] = 'Alto'
            elif num == '5':
                NotaT = int(input('Ingresa la nota teorica: '))
                NotaP = int(input('Ingresa la nota practica: '))
                NotaQ = int(input('Ingrsa el promedio de notas de los quizes y trabajos: '))
                Total = (NotaT*0.3)+(NotaP*0.6)+(NotaQ*0.1)
                if Total >= 60:
                    cursado['Backend'] = 'Aprobado'
                    cursado['riesgo'] = 'Bajo'
                elif Total < 60:
                    cursado['Backend'] = 'Reprobado'
                    cursado['riesgo'] = 'Alto'
    
    
    with open('aulas.json','w') as archivo:
        json.dump(data,archivo,indent=4)

notas()