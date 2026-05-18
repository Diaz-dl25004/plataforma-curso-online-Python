#Creacion del menu Gestion de Estudiantes
from modulos.estudiantes import GestorEstudiante

def submenu_estudiante(): # Defino la función y servirá para poder llamarla desde el menú principal
     gestor = GestorEstudiante()

     while True:
        print("\n=== MENÚ ESTUDIANTES ===")
        print("1. Registrar estudiante")
        print("2. Mostrar estudiantes")
        print("3. Buscar estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Volver")

        opcion = input("Seleccione una opción: ")

        match opcion:

            case "1":
                gestor.registrar_estudiante()

            case "2":
                gestor.mostrar_estudiante()

            case "3":
                gestor.buscar_estudiante()

            case "4":
                gestor.actualizar_estudiante()

            case "5":
                gestor.eliminar_estudiante()

            case "6":
                print("Regresando al menú principal")
                break

            case _:
                print("Opción inválida.")








