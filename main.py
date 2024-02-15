import os
import inscripcionesCampers
import coordinadores
import distribucionAulas
import ModuloReportes
import notas
import notas2
import pruebaInicialCampers
import rutas
import Trainers

def clear_console():
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
            inscripcionesCampers.inscripciones()
        elif user_input == "2":
            print("Accediste a Actualizar Campers.")
            inscripcionesCampers.actualizar_campers()
        elif user_input == "3":
            print("Accediste a Buscar.")
            inscripcionesCampers.buscar()
        elif user_input == "4":
            print("Accediste a Mostrar Datos.")
            inscripcionesCampers.mostrar_datos()
        elif user_input == "5":
            print("Volviendo al menú principal.")
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
        print("Menu de Trainers:")
        print("1. Leer Trainers")
        print("2. Añadir Trainers")
        print("3. Actualizar Trainers")
        print("4. Eliminar Trainers")
        print("5. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            Trainers.leer_trainer()
        elif user_input == "2":
            Trainers.Añadir_trainer()
        elif user_input == "3":
            Trainers.Actualizar_trainer()
        elif user_input == "4":
            Trainers.Eliminar_trainer()
        elif user_input == "5":
            print("Volviendo al menú principal.")
            break

def menu_coordinadores():
    clear_console()
    while True:
        print("Menu de Coordinadores:")
        print("1. Agregar Coordinadores")
        print("2. Prueba Inicial")
        print("3. Distribución de Aulas")
        print("4. Módulo de Reportes")
        print("5. Notas")
        print("6. Rutas")
        print("7. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5", "6"])
        if user_input == "1":
            print("Accediste a Agregar Coordinadores.")
            coordinadores.Coordinadores()
        elif user_input == "2":
            print("Accediste a Prueba Inicial.")
            pruebaInicialCampers.pruebaInicial()
        elif user_input == "3":
            print("Accediste a Distribución de Aulas.")
            distribucionAulas.distribucionAulas()
        elif user_input == "4":
            menu_reportes()
        elif user_input == "5":
            menu_notas()
        elif user_input == "6":
            menu_rutas()
        elif user_input == "7":
            print("Volviendo al menú principal.")
            break

def menu_reportes():
    clear_console()
    while True:
        print("Menu de Reportes:")
        print("1. Camper Estado Inscrito")
        print("2. Camper Estado Aprobado")
        print("3. Trainers")
        print("4. Bajo Rendimiento")
        print("5. Camper Función")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            print("Accediste a Camper Estado Inscrito.")
            ModuloReportes.camperEstadoInscrito()
        elif user_input == "2":
            print("Accediste a Camper Estado Aprobado.")
            ModuloReportes.camperEstadoAprobado()
        elif user_input == "3":
            print("Accediste a Trainers.")
            ModuloReportes.Trainers()
        elif user_input == "4":
            print("Accediste a Bajo Rendimiento.")
            ModuloReportes.bajoRendimiento()
        elif user_input == "5":
            print("Accediste a Camper Función.")
            ModuloReportes.CamperFuncion()

def menu_notas():
    clear_console()
    while True:
        print("Menu de Notas:")
        print("1. Actualizar Nota y Rendimiento")
        print("2. Volver al menú de Coordinadores")

        user_input = get_valid_input(["1", "2", "3", "4", "5", "6"])
        if user_input == "1":
            notas.actualizar_notas_y_rendimiento()
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
            rutas.rutas()
        elif user_input == "2":
            print("Volviendo al menú de Coordinadores.")
            break

def configurar_ruta():
    print("Accediste a Configurar Ruta.")


def menu_principal():
    clear_console()
    while True:
        print("Bienvenido al sistema de gestión:")
        print("1. Inscripciones de Campers")
        print("2. Menu Trainers")
        print("3. Menu Coordinadores")
        print("4. Salir")

        user_input = get_valid_input(["1", "2", "3", "4"])
        if user_input == "4":
            print("¡Hasta luego!")
            break
        elif user_input == "1":
            menu_inscripcionesCampers()
        elif user_input == "2":
            menu_trainers()
        elif user_input == "3":
            menu_coordinadores()

if __name__ == "__main__":
    menu_principal()
