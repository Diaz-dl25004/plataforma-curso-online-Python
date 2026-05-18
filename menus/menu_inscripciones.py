# menus/menu_inscripciones.py
def submenu_inscripcion(gestor_estudiante, gestor_curso):
    from modulos.inscripciones import GestorInscripcion
    gestor_inscripcion = GestorInscripcion(gestor_estudiante, gestor_curso)
    
    while True:
        print("\n=== MENÚ INSCRIPCIONES ===")
        print("1. Inscribir estudiante en curso")
        print("2. Listar cursos por estudiante")
        print("3. Listar estudiantes por curso")
        print("4. Eliminar inscripción")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        match opcion:
            case "1":
                gestor_inscripcion.inscribir_estudiante()
            case "2":
                gestor_inscripcion.listar_cursos_por_estudiante()
            case "3":
                gestor_inscripcion.listar_estudiantes_por_curso()
            case "4":
                gestor_inscripcion.eliminar_inscripcion()  # ← Asegúrate que esta línea exista
            case "5":
                print("Regresando al menú principal...")
                break
            case _:
                print("Opción inválida.")