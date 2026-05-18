# menu_principal.py
from menus.menu_estudiantes import submenu_estudiante
from menus.menu_cursos import submenu_curso
from menus.menu_inscripciones import submenu_inscripcion
from modulos.estudiantes import GestorEstudiante
from modulos.cursos import GestorCurso

def menu_principal():
    gestor_estudiante = GestorEstudiante()
    gestor_curso = GestorCurso()
    
    while True:
        print("\n=== PLATAFORMA DE CURSOS ONLINE ===")
        print("\n=========== BIENVENIDOS ===========")
        print("1. Gestión de Estudiantes")
        print("2. Gestión de Cursos")
        print("3. Gestión de Inscripciones")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                submenu_estudiante(gestor_estudiante)
            case "2":
                submenu_curso(gestor_curso)
            case "3":
                submenu_inscripcion(gestor_estudiante, gestor_curso)
            case "4":
                print("¡Hasta luego!")
                break
            case _:
                print("Opción inválida. Por favor, seleccione 1-4.")