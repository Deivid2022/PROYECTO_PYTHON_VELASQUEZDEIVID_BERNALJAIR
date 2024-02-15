
def clear_console():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def get_valid_input(options):
    while True:
        user_input = input("Seleccione una opción: ").strip()
        if user_input in options:
            return user_input
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

def menu_campers():
    print("Estás en el menú de Campers.")

def menu_inscripcionesCampers():
    
    clear_console()
    while True:
        print("Menu de Inscripciones de Campers:")
        print("1. Inscripciones")
        print("2. Actualizar Campers")
        print("3. Buscar")
        print("4. Mostrar Datos")
        print("5. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            print("Accediste a Inscripciones de Campers.")
            from inscripcionesCampers import inscripciones
        elif user_input == "2":
            print("Accediste a Actualizar Campers.")
            from inscripcionesCampers import actualizar_campers
        elif user_input == "3":
            print("Accediste a Buscar.")
            from inscripcionesCampers import buscar
        elif user_input == "4":
            print("Accediste a Mostrar Datos.")
            from inscripcionesCampers import mostrar_datos
        elif user_input == "5":
            print("Volviendo al menú coordinador.")
            break

def leer_trainers():
    print("Accediste a Leer Trainers.")

def añadir_trainers():
    print("Accediste a Añadir Trainers.")

def actualizar_trainers():
    print("Accediste a Actualizar Trainers.")

def eliminar_trainers():
    print("Accediste a Eliminar Trainers.")

def menu_trainers():
    
    clear_console()
    while True:
        print("1. Leer Trainers")
        print("2. Añadir Trainers")
        print("3. Actualizar Trainers")
        print("4. Eliminar Trainers")
        print("5. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            from Trainers import leer_trainer
        elif user_input == "2":
            from Trainers import Añadir_trainer
        elif user_input == "3":
            from Trainers import Actualizar_trainer
        elif user_input == "4":
            from Trainers import Eliminar_trainer
        elif user_input == "5":
            print("Volviendo al menú principal.")
            break

def menu_coordinadores():
    clear_console()
    while True:
        print("Rol de Coordinador:")
        print("1. Agregar Coordinadores")
        print("2. Agregar Trainers")
        print('3. Incripciones')
        print("4. Prueba Inicial")
        print("5. Distribución de Aulas")
        print("6. Módulo de Reportes")
        print("7. Notas")
        print("8. Rutas")
        print("9. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5", "6","7","8","9"])
        if user_input == "1":
            print("Accediste a Agregar Coordinadores.")
            from coordinadores import Coordinadores
        if user_input == "2":
            menu_inscripcionesCampers()
        if user_input == "3":
            menu_trainers()
        elif user_input == "4":
            print("Accediste a Prueba Inicial.")
            from pruebaInicialCampers import pruebaInicial
        elif user_input == "5":
            print("Accediste a Distribución de Aulas.")
            from distribucionAulas import distribucionAulas1
        elif user_input == "6":
            menu_reportes()
        elif user_input == "7":
            menu_notas()
        elif user_input == "8":
            menu_rutas()
        elif user_input == "9":
            print("Volviendo al menú principal.")
            break

def menu_reportes():
    
    clear_console()
    while True:
        print("Menu de Reportes:")
        print("1. Camper Estado Inscrito")
        print("2. Camper Estado Aprobado prueba inicial")
        print("3. Trainers")
        print("4. Bajo Rendimiento")
        print("5. Campers y Trainers asociados a una ruta")
        print('6. Campers que perdieron y aprobaron por modulos')
        print('7. Volver al menu coordinador')

        user_input = get_valid_input(["1", "2", "3", "4", "5","6","7"])
        if user_input == "1":
            print("Accediste a Camper Estado Inscrito.")
            from ModuloReportes import camperEstadoInscrito
        elif user_input == "2":
            print("Accediste a Camper Estado Aprobado.")
            from ModuloReportes import camperEstadoAprobado
        elif user_input == "3":
            print("Accediste a Trainers.")
            from ModuloReportes import Trainers
        elif user_input == "4":
            print("Accediste a Bajo Rendimiento.")
            from ModuloReportes import bajoRendimiento
        elif user_input == "5":
            print("Accediste a Campers y Trainers asociados a una ruta.")
            from ModuloReportes import CamperFuncion
        elif user_input == "6":
            print("Accediste a campers que perdieron y aprobaron por modulos")
            from ModuloReportes import CamperAprobadosYReprobados
        elif user_input == "7":
            print('Volviendo al menu coordinador')
            break

def menu_notas():
    clear_console()
    while True:
        print("Menu de Notas:")
        print("1. Actualizar Nota y Rendimiento")
        print("2. Volver al menú de Coordinadores")

        user_input = get_valid_input(["1", "2"])
        if user_input == "1":
            from notas2 import notas
        elif user_input == "2":
            print("Volviendo al menú de Coordinadores.")
            break

def actualizar_nota_y_rendimiento():
    print("Accediste a Actualizar Nota y Rendimiento.")

def menu_rutas():
    
    clear_console()
    while True:
        print("Menu de Rutas:")
        print("1. Configurar Ruta")
        print("2. Volver al menú de Coordinadores")

        user_input = get_valid_input(["1", "2"])
        if user_input == "1":
            from rutas import rutas1
        elif user_input == "2":
            print("Volviendo al menú de Coordinadores.")
            break

def configurar_ruta():
    print("Accediste a Configurar Ruta.")


def menu_principal():
    clear_console()
    while True:
        print('----------------------------------------')
        print("--  Bienvenido al sistema de gestión  --")
        print('----------------------------------------')
        print('')
        print("1. Rol Camper")
        print("2. Menú Trainer")
        print("3. Rol Coordinador")
        print("4. Salir")

        user_input = get_valid_input(["1", "2", "3", "4"])
        if user_input == "4":
            print("¡Hasta luego!")
            break
        elif user_input == "1":
            print('Ingresa la siguiente informacion para hacer la busqueda')
            import camper
        elif user_input == "2":
            menu_trainers()
        elif user_input == "3":
            menu_coordinadores()

if __name__ == "__main__":
    menu_principal()
