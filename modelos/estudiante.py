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
     
          
   





