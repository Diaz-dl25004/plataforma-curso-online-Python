# Creación de la clase Gestor de estudiantes
from modelos.estudiante import Estudiante
import json
import os


class GestorEstudiante:

    #Constructor que inicia abriendo un archivo json con los datos guardados
    def __init__(self):

        #BLOQUE NECESARIO PARA ADECUAR LA RUTA A LOS ARCHIVOS JSON AUNQUE SE EJECUTE EN OTRA PC
        # En este bloque mediante --file-- se obtiene la ruta completa, se escala hasta la ruta raiz 
        # y se guarda el base_dir
        base_dir = os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
        )   # Toma la ruta raíz, entra en la carpeta datos y apunta  estudiante.json para cargar los datos
        
        self.archivo = os.path.join(
        base_dir,
        "datos",
        "estudiantes.json"
        )
        self.estudiantes = self.cargar_datos()
    # ==================================================================
        #METODO PARA CARGAR LOS DATOS DESDE EL ARCHIVO JSON Y CONVERTIRLO A OBJETO
    def cargar_datos(self):
        if not os.path.exists(self.archivo):
            return []
        with open(self.archivo, "r", encoding = "utf-8") as archivo:
            datos = json.load(archivo) 
            return [
            Estudiante.from_dict(estudiante)
            for estudiante in datos
        ]
    
        # METODO QUE CONVIERTE LOS OBJETOS ESTUDIANTES EN ARCHIVO DE TEXTO PLANO JSON
    def guardar_datos(self):

        datos = [
            estudiante.to_dict()
            for estudiante in self.estudiantes
        ]

        with open(self.archivo, "w", encoding="utf-8") as archivo:

           json.dump(
               datos,
               archivo,
               indent=4,
               ensure_ascii=False
        )
    # =====================================================================
        #FUNCIÓN PARA REGISTRAR ESTUDIANTE
    def registrar_estudiante(self): 
        print("\n === REGISTRAR ESTUDIANTE ===")
        id_estudiante = input("Ingrese ID del estudiante: ")
        nombre = input("Ingrese nombre: ")
        correo = input("Ingrese correo: ")
        edad = int(input("Ingrese edad: "))

        # Validacion de ID repetido
        for estudiante in self.estudiantes:
            if estudiante.id_estudiante == id_estudiante:
                print("Error: Ya existe estudiante con ese ID")
                return

        # Creacion del un objeto tipo Estudiante
        nuevo_estudiante = Estudiante( id_estudiante,  nombre,  correo, edad)
    
        # Esto agrega un nuevo estudiante a la lista [] pero manda a llamar a la funcion guardar_datos.
        self.estudiantes.append(nuevo_estudiante)
        self.guardar_datos() # Con esto llamamos a la funcion que se encarga de convertir el objeto en texto plano y guardarlo en jason
        print("Estudiante regitrado con éxito")


        #FUNCION PARA MOSTRAR INFORMACIÓN DE ESTUDIANTE
    def mostrar_estudiante(self):
        print("\n=== LISTA DE ESTUDIANTES ====")

        if len(self.estudiantes) == 0: # Si no hay registros imprime un mensaje
            print("No hay estudiantes registrados")
            return
        
        for estudiante in self.estudiantes:
            estudiante.mostrar_info()


        #   FUNCION PARA BUSCAR ESTUDIANTE SEGUN ID
    def buscar_estudiante(self):
        print("\n=== BUSCAR ESTUDIANTE ===")
        id_buscar = input("Ingrese ID del estudiante: ")

        for estudiante in self.estudiantes:
            if estudiante.id_estudiante == id_buscar:
                print("\nEstudiante encontrado:")
                estudiante.mostrar_info()
                return
        print("Estudiante no encontrado")


        #FUNCION PARA ACTUALIZAR DATOS DEL ESTUDIANTE SEGUN ID
    def actualizar_estudiante(self):
        print("\n=== ACTUALIZAR ESTUDIANTE ===")
        id_buscar = input("Ingrese ID del estudiante: ")

        for estudiante in self.estudiantes:
            # Aseguramos la comparación transformando ambos a string por si acaso
            if str(estudiante.id_estudiante) == str(id_buscar):
                print("\n--- Ingrese nuevos datos (Presione ENTER para mantener el valor actual) ---")

                # 1. Campo Nombre (Opcional)
                nombre_input = input(f"Nuevo nombre ({estudiante.nombre}): ").strip()
                nombre_final = nombre_input if nombre_input else estudiante.nombre

                # 2. Campo Correo (Opcional)
                correo_input = input(f"Nuevo correo ({estudiante.correo}): ").strip()
                correo_final = correo_input if correo_input else estudiante.correo

                # 3. Campo Edad (Opcional con validación de enteros)
                edad_final = estudiante.edad  # Por defecto dejamos la actual
                edad_input = input(f"Nueva edad ({estudiante.edad}): ").strip()
                
                if edad_input:  # Si el usuario digitó algo, lo validamos
                    try:
                        edad_final = int(edad_input)
                    except ValueError:
                        print("Error: La edad debe ser un número entero. Se mantendrá la edad actual.")

                # Mandamos los datos finales recopilados al método del modelo
                estudiante.actualizar_datos(nombre_final, correo_final, edad_final)
                
                # Guardamos los cambios de inmediato en el JSON
                self.guardar_datos()
                print("\n✓ Datos del estudiante sincronizados con éxito.")
                return

        print("Estudiante no encontrado.")


        #FUNCION PARA ELIMINAR REGISTRO DE ESTUDIANTE
    def eliminar_estudiante(self):
        print("\n=== ELIMINAR ESTUDIANTE ===")
        id_buscar = input("Ingrese ID del estudiante: ")

        for estudiante in self.estudiantes:
            if estudiante.id_estudiante == id_buscar:

                self.estudiantes.remove(estudiante)
                self.guardar_datos() # Llamamos al metodo acceder al archivo json y poder borrar el registro del estudiante eliminado

                print("Estudiante eliminado correctamente.")
                return

        print("Estudiante no encontrado.")