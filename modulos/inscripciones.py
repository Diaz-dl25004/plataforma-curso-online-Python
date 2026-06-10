# Creacion de la clase Gestor de Inscripciones
from modelos.inscripcion import Inscripcion
import os
import json

class GestorInscripcion:
    # Constructor
    def __init__(self, gestor_estudiante, gestor_curso):
        self.inscripciones = []  # Lista en memoria de inscripciones
        self.gestor_estudiante = gestor_estudiante  # Referencia al gestor de estudiantes
        self.gestor_curso = gestor_curso            # Referencia al gestor de cursos
        self.contador_id = 1                        # Para generar IDs únicos automáticamente

    #BLOQUE NECESARIO PARA ADECUAR LA RUTA A LOS ARCHIVOS JSON AUNQUE SE EJECUTE EN OTRA PC
        # En este bloque mediante --file-- se obtiene la ruta completa, se escala hasta la ruta raiz 
        # y se guarda el base_dir
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.archivo = os.path.join(base_dir, "datos", "inscripciones.json")
        self.archivo_tutores = os.path.join(base_dir, "datos", "tutores.json")
        self.cargar_datos()  

    # =========================================================================
    #METODO PARA CARGAR LOS DATOS DESDE EL ARCHIVO JSON Y CONVERTIRLO A OBJETO
    def cargar_datos(self):
        """Lee el archivo JSON de inscripciones y restaura la lista de objetos en memoria"""
        if not os.path.exists(self.archivo):
            return

        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                datos_json = json.load(f)
                # Usamos el método de clase from_dict que recién agregamos
                self.inscripciones = [Inscripcion.from_dict(item) for item in datos_json]
                
                # Sincronizamos el contador de IDs automáticos
                if self.inscripciones:
                    self.contador_id = max(ins.id_inscripcion for ins in self.inscripciones) + 1
        except (json.JSONDecodeError, KeyError):
            self.inscripciones = []
            self.contador_id = 1

     # METODO QUE CONVIERTE LOS OBJETOS ESTUDIANTES EN ARCHIVO DE TEXTO PLANO JSON
    def guardar_datos(self):
        """Convierte los objetos Inscripcion a diccionarios y los escribe en el JSON"""
        datos = [inscripcion.to_dict() for inscripcion in self.inscripciones]
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4, ensure_ascii=False)

    # METODO QUE ASIGNA A UN TUTOR AUTOMATICAMENTE A UNA INSCRIPCION DEPENDIENDO DEL CURSO
    def obtener_tutor_por_curso(self, id_curso):
        """Busca automáticamente en tutores.json quién imparte el curso según su ID"""
        if not os.path.exists(self.archivo_tutores):
            return "Asignado por Administración"
        
        try:
            with open(self.archivo_tutores, "r", encoding="utf-8") as f:
                tutores = json.load(f)
                for t in tutores:
                    if str(t["id_curso"]) == str(id_curso):
                        return t["tutor"]
        except Exception:
            pass
        return "Tutor por asignar"

    # ===========================================================================

    # FUNCIÓN PARA INSCRIBIR ESTUDIANTE EN CURSO
    def inscribir_estudiante(self):
        print("\n=== INSCRIBIR ESTUDIANTE EN CURSO ===")

        if len(self.gestor_estudiante.estudiantes) == 0:
            print("Error: No hay estudiantes registrados.")
            return

        if len(self.gestor_curso.cursos) == 0:
            print("Error: No hay cursos registrados.")
            return

        # Mostrar estudiantes disponibles (estudiante es un objeto)
        print("\n--- Estudiantes disponibles ---")
        for estudiante in self.gestor_estudiante.estudiantes:
            estudiante.mostrar_info()

        id_estudiante = input("\nIngrese ID del estudiante: ")

        # Validar que el estudiante exista
        estudiante_encontrado = None
        for estudiante in self.gestor_estudiante.estudiantes:
            if str(estudiante.id_estudiante) == str(id_estudiante):
                estudiante_encontrado = estudiante
                break

        if estudiante_encontrado is None:
            print("Error: Estudiante no encontrado.")
            return

        # Mostrar cursos disponibles (son objetos)
        print("\n--- Cursos disponibles ---")
        for i, curso in enumerate(self.gestor_curso.cursos, 1):
            cupos_libres = curso.cupo_maximo - curso.inscritos
            print(
                f"[{i}] Curso: {curso.nombre} | Créditos: {curso.creditos} | Cupos libres: {cupos_libres}"
            )

        # Pedimos el número/índice del curso para hacerlo más fácil y rápido
        try:
            opcion_curso = (
                int(input("\nSeleccione el número del curso a inscribir: ")) - 1
            )
            if 0 <= opcion_curso < len(self.gestor_curso.cursos):
                curso_encontrado = self.gestor_curso.cursos[opcion_curso]
            else:
                curso_encontrado = None
        except ValueError:
            print("Error: Debe ingresar un número válido.")
            return

        if curso_encontrado is None:
            print("Error: Selección de curso no válida.")
            return

        # Validar si quedan cupos disponibles en el curso
        cupos_libres = curso_encontrado.cupo_maximo - curso_encontrado.inscritos
        if cupos_libres <= 0:
            print(f"Error: Ya no quedan cupos disponibles para el curso '{curso_encontrado.nombre}'.")
            return

        # Validar que no esté ya inscrito usando el ID unico del curso
        for inscripcion in self.inscripciones:
            if (
                str(inscripcion.id_estudiante) == str(id_estudiante)
                and str(inscripcion.id_curso) == str(curso_encontrado.id_curso)
            ):
                print("Error: El estudiante ya está inscrito en ese curso específico.")
                return
        
        # Jalamos el tutor que el curso y trae asignado desde su creacion
        # Usamos getattr por seguridad por si algún curso viejo en el JSON no tiene el atributo.
        tutor_asignado = getattr(curso_encontrado, 'tutor', "Por asignar")
        
        # Crear el objeto Inscripcion incluyendo el tutor directo de la materia
        nueva_inscripcion = Inscripcion(
            self.contador_id, id_estudiante, curso_encontrado.id_curso, tutor_asignado
        )
        self.inscripciones.append(nueva_inscripcion)
        self.contador_id += 1

        # Aumentamos los inscritos en el curso y guardamos AMBOS archivos JSON
        curso_encontrado.inscritos += 1
        self.gestor_curso.guardar_datos()  # Actualiza cursos.json
        self.guardar_datos()              # Actualiza inscripciones.json

        print(f"¡Inscripción exitosa!: {estudiante_encontrado.nombre} → {curso_encontrado.nombre}")
        print(f"Tutor asignado a cargo: {tutor_asignado}")
        
        
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
            if str(estudiante.id_estudiante) == str(id_estudiante):
                estudiante_encontrado = estudiante
                break

        if estudiante_encontrado is None:
            print("Error: Estudiante no encontrado.")
            return

        print(f"\nCursos de {estudiante_encontrado.nombre}:")
        encontrado = False

        for inscripcion in self.inscripciones:
            if str(inscripcion.id_estudiante) == str(id_estudiante):
                for curso in self.gestor_curso.cursos:
                    if str(curso.id_curso) == str(inscripcion.id_curso):
                        print(f"• ID: {curso.id_curso} | Curso: {curso.nombre} | Tutor: {inscripcion.tutor}")
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
            print(f"ID: {curso.id_curso} | {curso.nombre}")

        id_curso = input("\nIngrese ID del curso para ver los alumnos: ")

        # Validar que el curso exista
        curso_encontrado = None
        for curso in self.gestor_curso.cursos:
            if str(curso.id_curso) == str(id_curso):
                curso_encontrado = curso
                break

        if curso_encontrado is None:
            print("Error: Curso no encontrado.")
            return

        print(f"\nEstudiantes en {curso_encontrado.nombre}:")
        encontrado = False

        for inscripcion in self.inscripciones:
            if str(inscripcion.id_curso) == str(id_curso):
                for estudiante in self.gestor_estudiante.estudiantes:
                    if str(estudiante.id_estudiante) == str(inscripcion.id_estudiante):
                        print(f"• ID: {estudiante.id_estudiante} | Nombre: {estudiante.nombre}")
                        encontrado = True

        if not encontrado:
            print("No hay estudiantes inscritos en este curso.")

    # FUNCIÓN PARA ELIMINAR UNA INSCRIPCIÓN (Versión simplificada)
    def eliminar_inscripcion(self):
        print("\n=== ELIMINAR INSCRIPCIÓN ===")
        
        if len(self.inscripciones) == 0:
            print("No hay inscripciones registradas.")
            return
            print("\n--- Inscripciones actuales ---")

        for inscripcion in self.inscripciones:
            # Buscamos el nombre del curso rápido para darle contexto visual al usuario
            nombre_c = "Curso Desconocido"
            for c in self.gestor_curso.cursos:
                if str(c.id_curso) == str(inscripcion.id_curso):
                    nombre_c = c.nombre
                    break
            print(f"ID Inscripción: {inscripcion.id_inscripcion} | Estudiante ID: {inscripcion.id_estudiante} | {nombre_c}")
        
        try:
            id_inscripcion = int(input("\nIngrese ID de la inscripción a eliminar: "))
        except ValueError:
            print("Error: El ID debe ser un número entero.")
            return  
        for i, inscripcion in enumerate(self.inscripciones):
            if inscripcion.id_inscripcion == id_inscripcion:
                # Devolvemos el cupo restando 1 a los inscritos en el curso original
                for curso in self.gestor_curso.cursos:
                    if str(curso.id_curso) == str(inscripcion.id_curso):
                        if curso.inscritos > 0:
                            curso.inscritos -= 1
                            self.gestor_curso.guardar_datos() # Sincroniza cursos.json
                        break
                
                print(f"Cancelando inscripción ID {inscripcion.id_inscripcion}...")
                del self.inscripciones[i]
                self.guardar_datos() # Sincroniza inscripciones.json automáticamente
                print(" Inscripción eliminada correctamente y cupo liberado.")
                return 
        print(f"✗ Inscripción con ID {id_inscripcion} no encontrada.")

        