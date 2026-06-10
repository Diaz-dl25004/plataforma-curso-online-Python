# modelos/curso.py
class Curso:
    def __init__(self, id_curso, nombre, descripcion, creditos, cupo_maximo, inscritos = 0, tutor= "Por asignar"):
        self.id_curso = id_curso
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos
        self.cupo_maximo = cupo_maximo
        self.inscritos = inscritos 
        self.tutor = tutor
    
    def mostrar_info(self):
        """Muestra la información completa del curso"""
        print("\n" + "="*40)
        print(f"ID Curso: {self.id_curso}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Créditos: {self.creditos}")
        print(f"Cupo máximo: {self.cupo_maximo}")
        print(f"Cupos Disponibles: {self.cupo_maximo - self.inscritos}")
        print(f"Tutor asigndo: {self.tutor}")
        print("="*40)
    
    def actualizar_datos(self, nombre=None, descripcion=None, creditos=None, cupo_maximo=None):
        """Actualiza los datos del curso"""
        if nombre:
            self.nombre = nombre
        if descripcion:
            self.descripcion = descripcion
        if creditos:
            self.creditos = creditos
        if cupo_maximo:
            self.cupo_maximo = cupo_maximo
        print("Curso actualizado correctamente.")
    
    def hay_cupo(self):
        """Verifica si hay cupo disponible en el curso"""
        return self.inscritos < self.cupo_maximo
    
    def inscribir_estudiante(self):
        """Inscribe un estudiante al curso si hay cupo"""
        if self.hay_cupo():
            self.inscritos += 1
            return True
        return False
    
    def desinscribir_estudiante(self):
        """Desinscribe un estudiante del curso"""
        if self.inscritos > 0:
            self.inscritos -= 1
            return True
        return False
    
        #----METODOS PARA LA INTEGRACION DEL USO DE JSON----

     # Convierte la instancia de Curso a un diccionario para poder guardarlo en JSON
    def to_dict(self):
        return {
            "id_curso": self.id_curso,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "creditos": self.creditos,
            "cupo_maximo": self.cupo_maximo,
            "inscritos": self.inscritos,
            "tutor": self.tutor
        }
    
      #Crea una instancia de Curso a partir de un diccionario proveniente de un JSON
    @classmethod
    def from_dict(cls, datos):
        return cls(
            id_curso=datos["id_curso"],
            nombre=datos["nombre"],
            descripcion=datos["descripcion"],
            creditos=datos["creditos"],
            cupo_maximo=datos["cupo_maximo"],
            inscritos=datos.get("inscritos", 0), # Usa 0 si por alguna razón no existe el campo
            tutor=datos.get("tutor", "Por asignar")
        )
    

