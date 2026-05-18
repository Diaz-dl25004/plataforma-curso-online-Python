# Creacion del menu principal de la plataforma
from menus.menu_estudiantes import submenu_estudiante

def menu_principal():
    
    while True:
        print("\n=== PLATAFORMA DE CURSOS ONLINE ===")
        print("\n=========== BIENVENIDOS ===========")
        print("1. Estudiante")
        print("2. Cursos")
        print("3. Incripción")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
               submenu_estudiante()
               
            case "2":
                 print("Pendiente agregar")

            case "3":
                 print("Pendiente agregar")

            case _:
                 print("Opción inválida.")


     


