# modelos/curso.py
class Curso:
    def __init__(self, id_curso, nombre, descripcion, creditos, cupo_maximo):
        self.id_curso = id_curso
        self.nombre = nombre
        self.descripcion = descripcion
        self.creditos = creditos
        self.cupo_maximo = cupo_maximo
        self.inscritos = 0  # Contador de estudiantes inscritos
    
    def mostrar_info(self):
        """Muestra la información completa del curso"""
        print("\n" + "="*40)
        print(f"ID Curso: {self.id_curso}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")
        print(f"Créditos: {self.creditos}")
        print(f"Cupo máximo: {self.cupo_maximo}")
        print(f"Disponibles: {self.cupo_maximo - self.inscritos}")
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