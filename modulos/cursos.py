import json
import os
from modelos.cursos import Curso

class GestorCurso:

    def __init__(self):
        # Lista que almacenará los diccionarios de cada curso
        # self.cursos = []
        # #BLOQUE NECESARIO PARA ADECUAR LA RUTA A LOS ARCHIVOS JSON AUNQUE SE EJECUTE EN OTRA PC
        base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
        )
        
        self.archivo = os.path.join(
        base_dir,
        "datos",
        "cursos.json"
        )
        self.cursos = self.cargar_datos()

    # == METODOS DE PERSISTENCIA JSON ==
    
    def cargar_datos(self):
        # 1. Validación de existencia
        if not os.path.exists(self.archivo):
            return []
            
        # 2. Lectura limpia (con try por seguridad si el JSON está vacío o dañado)
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo) 
                return [Curso.from_dict(curso) for curso in datos]
        except json.JSONDecodeError:
            print(" Archivo cursos.json vacío o dañado. Iniciando lista vacía.")
            return []

    def guardar_datos(self):
        # Primero preparar la lista de diccionarios
        datos = [curso.to_dict() for curso in self.cursos]

        # Abrir archivo y gurdar
        with open(self.archivo, "w", encoding="utf-8") as archivo:
           json.dump(datos, archivo, indent=4, ensure_ascii=False)

    # ================ FUNCIONES DEL GESTOR ===========================

    def registrar_curso(self):
        """Opción 1: Registrar curso"""
        print("\n--- REGISTRAR NUEVO CURSO ---")
        id_curso = input("Ingrese ID del curso: ")
        
        # VALIDACIÓN CLAVE: Verificar que el ID sea único en la lista
        for curso in self.cursos:
            if str(curso.id_curso) == str(id_curso):
                print(f" Error: Ya existe un curso registrado con el ID '{id_curso}'.")
                return # Cancelamos el registro para evitar duplicados
            
        nombre = input("Ingrese nombre del curso: ").strip()
        descripcion = input("Ingrese descripción del curso: ").strip()
        
        try:
            creditos = int(input("Ingrese los créditos del curso: "))
            cupos = int(input("Ingrese la cantidad de cupos disponibles: "))
        except ValueError:
            print("Entrada inválida. Se asignarán valores por defecto (3 créditos, 20 cupos).")
            creditos = 3
            cupos = 20
        
        print(" Seleccione un tutor para el curso ")
        # Localizamos la ruta de tutores.json en la carpeta datos donde estan guardados todos nuestros archivos.json
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        ruta_tutores = os.path.join(base_dir, "datos", "tutores.json")
        
        tutor_seleccionado = "Por asignar"
        
        if os.path.exists(ruta_tutores):
            try:
                with open(ruta_tutores, "r", encoding="utf-8") as f:
                    lista_tutores = json.load(f)
                
                # Desplegamos los tutores con su profesión
                for t in lista_tutores:
                    print(f"[{t['id_tutor']}] {t['nombre']} | Especialidad: {t['profesion']}")

                id_t = int(input("\nIngrese el número (ID) del tutor a asignar: "))
                
                # Buscamos la coincidencia del ID digitado
                for t in lista_tutores:
                    if t['id_tutor'] == id_t:
                        # Guardamos el nombre y título profesional directo en el curso
                        tutor_seleccionado = f"{t['nombre']} ({t['profesion']})"
                        break
                else:
                    print(" ID no encontrado en el catálogo. Se asignará 'Por asignar'.")
                    
            except (json.JSONDecodeError, ValueError):
                print(" Error de lectura o selección no válida. Se asignará 'Por asignar'.")
        else:
            print(" Nota: El archivo 'tutores.json' no existe todavía. Queda 'Por asignar'.")

        # Creamos la instancia de la clase Curso con todos sus parámetros nuevos
        nuevo_curso = Curso(
            id_curso=id_curso,
            nombre=nombre,
            descripcion=descripcion,
            creditos=creditos,
            cupo_maximo=cupos,
            inscritos=0,
            tutor=tutor_seleccionado
        )
        
        # Guardamos en la lista y sincronizamos con el archivo JSON
        self.cursos.append(nuevo_curso)
        self.guardar_datos()
        
        print(f"¡Curso '{nombre}' registrado con éxito con el tutor: {tutor_seleccionado}!")

    def mostrar_cursos(self):
        """Opción 2: Mostrar todos los cursos"""
        print("\n--- LISTADO DE CURSOS ACTIVOS ---")
        if not self.cursos:
            print("No hay cursos registrados en el sistema.")
            return

        # Utilizamos el método de impresión de la clase Curso
        for curso in self.cursos:
            curso.mostrar_info() # Llamada al metodo de la clase Curso

    def buscar_curso(self):
        """Opción 3: Buscar curso"""
        print("\n--- BUSCAR CURSO ---")
        if not self.cursos:
            print("No hay cursos en el sistema para buscar.")
            return

        busqueda = input("Ingrese el nombre del curso que busca: ").lower()
        encontrados = []

        for curso in self.cursos:
            if busqueda in curso.nombre.lower():
                encontrados.append(curso)

        if encontrados:
            print("\nCursos encontrados:")
            for curso in encontrados:
                print(f"- ID: {curso.id_curso} | {curso.nombre} | Cupos Máximos: {curso.cupo_maximo}")
        else:
            print("No se encontró ningún curso con ese nombre.")

    def actualizar_curso(self):
        """Opción 4: Actualizar curso"""
        print("\n--- ACTUALIZAR CURSO ---")
        if not self.cursos:
            print("No hay cursos registrados para actualizar.")
            return

        try:
            print("Seleccione el número del curso que desea actualizar:")
            for i, curso in enumerate(self.cursos, 1):
                print(f"{i}. {curso.nombre} (ID: {curso.id_curso})")

            indice = int(input("Número de la lista: ")) - 1

            if 0 <= indice < len(self.cursos):
                curso_seleccionado = self.cursos[indice]
                
                print(f"\nModificando curso: {curso_seleccionado.nombre}")
                nuevo_nombre = input("Nuevo Nombre (dejar vacío para mantener): ").strip() or None
                nueva_desc = input("Nueva Descripción (dejar vacío para mantener): ").strip() or None
                
                nuevo_credito_str = input("Nuevos Créditos (dejar vacío para mantener): ").strip()
                nuevos_creditos = int(nuevo_credito_str) if nuevo_credito_str else None
                
                nuevos_cupos_str = input("Nuevos Cupos Totales (dejar vacío para mantener): ").strip()
                nuevos_cupos = int(nuevos_cupos_str) if nuevos_cupos_str else None

                # Actualizamos usando el método interno del objeto Curso
                curso_seleccionado.actualizar_datos(
                    nombre=nuevo_nombre, 
                    descripcion=nueva_desc, 
                    creditos=nuevos_creditos, 
                    cupo_maximo=nuevos_cupos
                )
                
                # Guardamos los cambios en el JSON
                self.guardar_datos()
            else:
                print("Número de curso fuera de rango.")
        except ValueError:
            print("Error: Ingrese un número o dato válido.")

    def eliminar_curso(self):
        """Opción 5: Eliminar curso"""
        print("\n--- ELIMINAR CURSO ---")
        if not self.cursos:
            print("No hay cursos registrados para eliminar.")
            return

        try:
            print("Seleccione el número del curso que desea eliminar:")
            for i, curso in enumerate(self.cursos, 1):
                print(f"{i}. {curso.nombre}")

            indice = int(input("Número de curso: ")) - 1

            if 0 <= indice < len(self.cursos):
                eliminado = self.cursos.pop(indice)
                # Guardamos para actualizar el JSON eliminando el registro
                self.guardar_datos()
                print(f"¡Curso '{eliminado.nombre}' eliminado correctamente!")
            else:
                print("Número de curso no válido.")
        except ValueError:
            print("Error: Ingrese un número de índice válido.")

    def ver_cupos_disponibles(self):
        """Opción 6: Ver cupos disponibles"""
        print("\n--- CUPOS DISPONIBLES EN CURSOS ---")
        if not self.cursos:
            print("No hay cursos registrados.")
            return

        for curso in self.cursos:
            # Cálculo dinámico basado en los datos reales del objeto
            cupos_libres = curso.cupo_maximo - curso.inscritos
            print(f"- {curso.nombre}: {cupos_libres} lugares libres (Inscritos: {curso.inscritos}/{curso.cupo_maximo}).")