# Creacion de la clase estudiante

class Estudiante: # Se definen los atributos de la clase 
     def __init__(self, id_estudiante, nombre, correo, edad):
          self.id_estudiante = id_estudiante
          self.nombre = nombre
          self.correo = correo
          self.edad = edad

     def mostrar_info(self): # funcion para mostrar la informacion del estudiante
          print("\n--- INIFORMACIÓN DEL ESTUDIANTE ---")
          print(f"ID: {self.id_estudiante}")
          print(f"Nombre: {self.nombre}")
          print(f"Correo: {self.correo}")
          print(f"Edad: {self.edad}")

     def actualizar_datos(self, nombre, correo, edad): # funcion para actualizar datos del estudiante
          self.nombre = nombre
          self.correo = correo
          self.edad = edad
     
     #-----METODOS PARA LA INTEGRACION DEL USO DE JSON----
     
     def to_dict(self): #Esta funcion convierte un objeto Estudiante en un dicionario que Json puede guardar
          return{
               "id_estudiante": self.id_estudiante,
               "nombre": self.nombre,
               "correo": self.correo,
               "edad": self.edad
          }   
     
     @classmethod 
     def from_dict(cls, datos):  # Esta funcion toma el diccionario guardado en json y lo transforma en un objeto
          return cls(
              datos["id_estudiante"],
              datos["nombre"],
              datos["correo"],
              datos["edad"]
    )  
   
     




