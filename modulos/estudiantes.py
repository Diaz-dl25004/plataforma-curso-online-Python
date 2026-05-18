# Creación de la clase Gestor de estudiantes
from modelos.estudiante import Estudiante

class GestorEstudiante:

    def __init__(self):
        self.estudiantes = [] # Esta lista sirve como base de datos temporal para guardar los objetos de tipo estudiante


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
           
        # Esto agrega a la lista estudiantes[], un nuevo estudiante
        self.estudiantes.append(nuevo_estudiante)
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
                print("\nEstudiante enconctrado:")
                estudiante.mostrar_info()
                return
        print("Estudiante encontrado")


        #FUNCION PARA ACTUALIZAR DATOS DEL ESTUDIANTE SEGUN ID
    def actualizar_estudiante(self):
        print("\n=== ACTUALIZAR ESTUDIANTE ===")
        id_buscar = input("Ingrese ID del estudiante: ")

        for estudiante in self.estudiantes:
            if estudiante.id_estudiante == id_buscar:

                print("\nIngrese nuevos datos:")

                nombre = input("Nuevo nombre: ")
                correo = input("Nuevo correo: ")
                edad = int(input("Nueva edad: "))

                estudiante.actualizar_datos(nombre, correo, edad)
                print("Estudiante actualizado correctamente.")
                return
        print("Estudiante no encontrado.")


        #FUNCION PARA ELIMINAR REGISTRO DE ESTUDIANTE
    def eliminar_estudiante(self):
        print("\n=== ELIMINAR ESTUDIANTE ===")
        id_buscar = input("Ingrese ID del estudiante: ")

        for estudiante in self.estudiantes:
            if estudiante.id_estudiante == id_buscar:

                self.estudiantes.remove(estudiante)

                print("Estudiante eliminado correctamente.")
                return

        print("Estudiante no encontrado.")










