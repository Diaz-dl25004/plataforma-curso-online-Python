#Clase Inscripción

class Inscripcion:
    def __init__(self, id_inscripcion, id_estudiante, id_curso):
        self.id_inscripcion = id_inscripcion
        self.id_estudiante = id_estudiante
        self.id_curso = id_curso
 
    def mostrar_info(self):
        print("\n--- INFORMACIÓN DE INSCRIPCIÓN ---")
        print(f"ID Inscripción : {self.id_inscripcion}")
        print(f"ID Estudiante  : {self.id_estudiante}")
        print(f"ID Curso       : {self.id_curso}")

          