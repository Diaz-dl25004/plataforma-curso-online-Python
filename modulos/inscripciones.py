# Creacion de la clase Gestor de Inscripciones
from modelos.inscripcion import Inscripcion

class GestorInscripcion:

    def __init__(self, gestor_estudiante, gestor_curso):
        self.inscripciones = []  # Lista en memoria de inscripciones
        self.gestor_estudiante = gestor_estudiante  # Referencia al gestor de estudiantes
        self.gestor_curso = gestor_curso            # Referencia al gestor de cursos
        self.contador_id = 1                        # Para generar IDs únicos automáticamente

    # FUNCIÓN PARA INSCRIBIR ESTUDIANTE EN CURSO
    def inscribir_estudiante(self):
        print("\n=== INSCRIBIR ESTUDIANTE EN CURSO ===")

        if len(self.gestor_estudiante.estudiantes) == 0:
            print("Error: No hay estudiantes registrados.")
            return

        if len(self.gestor_curso.cursos) == 0:
            print("Error: No hay cursos registrados.")
            return

        # Mostrar estudiantes disponibles
        print("\n--- Estudiantes disponibles ---")
        for estudiante in self.gestor_estudiante.estudiantes:
            estudiante.mostrar_info()

        id_estudiante = input("\nIngrese ID del estudiante: ")

        # Validar que el estudiante exista
        estudiante_encontrado = None
        for estudiante in self.gestor_estudiante.estudiantes:
            if estudiante.id_estudiante == id_estudiante:
                estudiante_encontrado = estudiante
                break

        if estudiante_encontrado is None:
            print("Error: Estudiante no encontrado.")
            return

        # Mostrar cursos disponibles
        print("\n--- Cursos disponibles ---")
        for curso in self.gestor_curso.cursos:
            curso.mostrar_info()

        id_curso = input("\nIngrese ID del curso: ")

        # Validar que el curso exista
        curso_encontrado = None
        for curso in self.gestor_curso.cursos:
            if curso.id_curso == id_curso:
                curso_encontrado = curso
                break

        if curso_encontrado is None:
            print("Error: Curso no encontrado.")
            return

        # Validar que no esté ya inscrito
        for inscripcion in self.inscripciones:
            if inscripcion.id_estudiante == id_estudiante and inscripcion.id_curso == id_curso:
                print("Error: El estudiante ya está inscrito en ese curso.")
                return

        # Crear y guardar la inscripción
        nueva_inscripcion = Inscripcion(self.contador_id, id_estudiante, id_curso)
        self.inscripciones.append(nueva_inscripcion)
        self.contador_id += 1
        print(f"Inscripción exitosa: {estudiante_encontrado.nombre} → {curso_encontrado.nombre}")

    # FUNCIÓN PARA LISTAR CURSOS DE UN ESTUDIANTE
    def listar_cursos_por_estudiante(self):
        print("\n=== CURSOS POR ESTUDIANTE ===")

        if len(self.gestor_estudiante.estudiantes) == 0:
            print("No hay estudiantes registrados.")
            return

        print("\n--- Estudiantes disponibles ---")
        for estudiante in self.gestor_estudiante.estudiantes:
            estudiante.mostrar_info()

        id_estudiante = input("\nIngrese ID del estudiante: ")

        # Validar que el estudiante exista
        estudiante_encontrado = None
        for estudiante in self.gestor_estudiante.estudiantes:
            if estudiante.id_estudiante == id_estudiante:
                estudiante_encontrado = estudiante
                break

        if estudiante_encontrado is None:
            print("Error: Estudiante no encontrado.")
            return

        print(f"\nCursos de {estudiante_encontrado.nombre}:")
        encontrado = False

        for inscripcion in self.inscripciones:
            if inscripcion.id_estudiante == id_estudiante:
                for curso in self.gestor_curso.cursos:
                    if curso.id_curso == inscripcion.id_curso:
                        curso.mostrar_info()
                        encontrado = True

        if not encontrado:
            print("No está inscrito en ningún curso.")

    # FUNCIÓN PARA LISTAR ESTUDIANTES DE UN CURSO
    def listar_estudiantes_por_curso(self):
        print("\n=== ESTUDIANTES POR CURSO ===")

        if len(self.gestor_curso.cursos) == 0:
            print("No hay cursos registrados.")
            return

        print("\n--- Cursos disponibles ---")
        for curso in self.gestor_curso.cursos:
            curso.mostrar_info()

        id_curso = input("\nIngrese ID del curso: ")

        # Validar que el curso exista
        curso_encontrado = None
        for curso in self.gestor_curso.cursos:
            if curso.id_curso == id_curso:
                curso_encontrado = curso
                break

        if curso_encontrado is None:
            print("Error: Curso no encontrado.")
            return

        print(f"\nEstudiantes en {curso_encontrado.nombre}:")
        encontrado = False

        for inscripcion in self.inscripciones:
            if inscripcion.id_curso == id_curso:
                for estudiante in self.gestor_estudiante.estudiantes:
                    if estudiante.id_estudiante == inscripcion.id_estudiante:
                        estudiante.mostrar_info()
                        encontrado = True

        if not encontrado:
            print("No hay estudiantes inscritos en este curso.")

    # FUNCIÓN PARA ELIMINAR UNA INSCRIPCIÓN (Versión simplificada)
    def eliminar_inscripcion(self):  # ← AHORA SÍ, dentro de la clase con indentación correcta
        print("\n=== ELIMINAR INSCRIPCIÓN ===")
        
        if len(self.inscripciones) == 0:
            print("No hay inscripciones registradas.")
            return
        
        # Mostrar inscripciones de forma más clara
        print("\n--- Inscripciones actuales ---")
        
        for inscripcion in self.inscripciones:
            print(f"ID: {inscripcion.id_inscripcion} | Estudiante: {inscripcion.id_estudiante} | Curso: {inscripcion.id_curso}")
        
        try:
            id_inscripcion = int(input("\nIngrese ID de la inscripción a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número")
            return
        
        # Buscar y eliminar
        for i, inscripcion in enumerate(self.inscripciones):
            if inscripcion.id_inscripcion == id_inscripcion:
                # Mostrar qué se está eliminando
                print(f"Eliminando inscripción - Estudiante: {inscripcion.id_estudiante}, Curso: {inscripcion.id_curso}")
                del self.inscripciones[i]
                print("✓ Inscripción eliminada correctamente.")
                return
        
        print(f"✗ Inscripción con ID {id_inscripcion} no encontrada.")
        print(f"IDs válidos: {[inscripcion.id_inscripcion for inscripcion in self.inscripciones]}")