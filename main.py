
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
    while True:
        print("\nMenu de Inscripciones de Campers:")
        print("1. Inscripciones")
        print("2. Actualizar Campers")
        print("3. Buscar")
        print("4. Mostrar Datos")
        print("5. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            print("Accediste a Inscripciones de Campers.")

        elif user_input == "2":
            print("Accediste a Actualizar Campers.")
        elif user_input == "3":
            print("Accediste a Buscar.")
        elif user_input == "4":
            print("Accediste a Mostrar Datos.")
        elif user_input == "5":
            print("Volviendo al menú principal.")
            break

def menu_trainers():
    print("Estás en el menú de Trainers.")

def menu_coordinadores():
    while True:
        print("\nMenu de Coordinadores:")
        print("1. Agregar Coordinadores")
        print("2. Prueba Inicial")
        print("3. Distribución de Aulas")
        print("4. Módulo de Reportes")
        print("5. Volver al menú principal")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            print("Accediste a Agregar Coordinadores.")
        elif user_input == "2":
            print("Accediste a Prueba Inicial.")
        elif user_input == "3":
            print("Accediste a Distribución de Aulas.")
        elif user_input == "4":
            menu_reportes()
        elif user_input == "5":
            print("Volviendo al menú principal.")
            break

def menu_reportes():
    while True:
        print("\nMenu de Reportes:")
        print("1. Camper Estado Inscrito")
        print("2. Camper Estado Aprobado")
        print("3. Trainers")
        print("4. Bajo Rendimiento")
        print("5. Volver al menú de Coordinadores")

        user_input = get_valid_input(["1", "2", "3", "4", "5"])
        if user_input == "1":
            print("Accediste a Camper Estado Inscrito.")
        elif user_input == "2":
            print("Accediste a Camper Estado Aprobado.")
        elif user_input == "3":
            print("Accediste a Trainers.")
        elif user_input == "4":
            print("Accediste a Bajo Rendimiento.")
        elif user_input == "5":
            print("Volviendo al menú de Coordinadores.")
            break

def menu_principal():
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
