# menus/menu_cursos.py
from modulos.cursos import GestorCurso

def submenu_curso(gestor_curso):
    """Submenú para la gestión de cursos"""
    while True:
        print("\n=== MENÚ CURSOS ===")
        print("1. Registrar curso")
        print("2. Mostrar todos los cursos")
        print("3. Buscar curso")
        print("4. Actualizar curso")
        print("5. Eliminar curso")
        print("6. Ver cupos disponibles")
        print("7. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                gestor_curso.registrar_curso()
            case "2":
                gestor_curso.mostrar_cursos()
            case "3":
                gestor_curso.buscar_curso()
            case "4":
                gestor_curso.actualizar_curso()
            case "5":
                gestor_curso.eliminar_curso()
            case "6":
                gestor_curso.ver_cupos_disponibles()
            case "7":
                print("Regresando al menú principal...")
                break
            case _:
                print("Opción inválida. Por favor, seleccione una opción válida.")