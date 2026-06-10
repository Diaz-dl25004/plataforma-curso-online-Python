#Clase Inscripción

class Inscripcion:
    def __init__(self, id_inscripcion, id_estudiante, id_curso, tutor = "Por asignar"):
        self.id_inscripcion = id_inscripcion
        self.id_estudiante = id_estudiante
        self.id_curso = id_curso
        self.tutor = tutor
 
    def mostrar_info(self):
        print("\n--- INFORMACIÓN DE INSCRIPCIÓN ---")
        print(f"ID Inscripción : {self.id_inscripcion}")
        print(f"ID Estudiante  : {self.id_estudiante}")
        print(f"ID Curso       : {self.id_curso}")
        print(f"Tutor Asignado : {self.tutor}")

    #----METODOS PARA LA INTEGRACION DEL USO DE JSON----
    # Para guardar en formatos json
    def to_dict(self):
        """Convierte el objeto Inscripcion a un diccionario para guardarlo en JSON"""
        return {
            "id_inscripcion": self.id_inscripcion,
            "id_estudiante": self.id_estudiante,
            "id_curso": self.id_curso,
            "tutor": self.tutor
        }

    # Para extraer de formato Json y construirlo como objeto
    @classmethod
    def from_dict(cls, datos):
        """Crea una instancia de Inscripcion a partir de un diccionario del JSON"""
        return cls(
            id_inscripcion=datos["id_inscripcion"],
            id_estudiante=datos["id_estudiante"],
            id_curso=datos["id_curso"],
            tutor=datos.get("tutor", "Por asignar") # .get evita errores si el campo no existía antes
        )      