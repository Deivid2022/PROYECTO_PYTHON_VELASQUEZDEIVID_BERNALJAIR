def menu():
    print('Modulos:')
    print('1. Fundamentos de programación')
    print('2. Programación Web')
    print('3. Programación formal')
    print('4. Bases de datos')
    print('5. Backend')


def notas():

    import json

    with open('cursando.json','r') as archivo:
        data = json.load(archivo)
    cursandos = data['cursando']

    id_camper = int(input('Ingresa el numero de identidad del camper:'))
    
    for cursado in cursandos:
        if cursado['identidad'] == id_camper:
            ruta = cursado['ruta']
            print(f'El estudiante ', {cursado['nombre']}, ' se encuentra en la ruta ',ruta)
            menu()
            num = input('Ingrese la posicion del modulo al que va a agregar las notas: ')
            if num == '1':
                NotaT = int(input('Ingresa la nota teorica: '))
                NotaP = int(input('Ingresa la nota practica: '))
                NotaQ = int(input('Ingrsa la suma total de los quizes y trabajos: '))
                Total = (NotaT*0.3)+(NotaP*0.6)+(NotaQ*0.6)
                cursado['Fundamentos de programacion'] = Total
    
    
    with open('cursando.json','w') as archivo:
        json.dump(data,archivo,indent=4)

notas()