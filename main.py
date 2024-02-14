
def menuInicial():
    print('''
          -----------------------
          Bienvenido a Campusland
          -----------------------''')
    print('')
    print('Elige el rol que quieras ejecutar')
    print('')
    print('1. Coordinador')
    print('2. Trainer')
    print('3. Camper')


def menuCoordinador():
    print('Que deseas hacer?')
    print('1. Inscribir Camper')
    print('2. Prueba Inicial del Camper')
    print('3. Registrar Trainer')
    print('4. Modulo de matriculas')
    print('5. Evaluar el rendimiento de los campers')
    
def menuTrainer():
    print('Que deseas hacer?')
    print('1. Ingresar notas de camper')
    print('2. observar riesgo del camper por modulo')
    print('3. Observar salones asignados')    

def menuCamper():
    print('Para observar tu rendimiento ingresa tu numero de identidad')
    num = int(input(''))
    print('Elige el modulo del que deseas ver tu rendimiento')
    print('1. Fundamentos de programación')
    print('2. Programación Web')
    print('3. Programación formal')
    print('4. Bases de datos')

menuInicial()
menuCoordinador()