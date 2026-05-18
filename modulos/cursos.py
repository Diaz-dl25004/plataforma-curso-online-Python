# modulos/cursos.py
from modelos.cursos import Curso

class GestorCurso:
    def __init__(self):
        self.cursos = []  # Base de datos temporal para cursos
    
    def registrar_curso(self):
        """Registra un nuevo curso en el sistema"""
        print("\n=== REGISTRAR CURSO ===")
        
        id_curso = input("Ingrese ID del curso: ")
        
        # Validar ID único
        for curso in self.cursos:
            if curso.id_curso == id_curso:
                print("Error: Ya existe un curso con ese ID")
                return
        
        nombre = input("Ingrese nombre del curso: ")
        descripcion = input("Ingrese descripción: ")
        
        # Validar créditos
        try:
            creditos = int(input("Ingrese número de créditos: "))
            if creditos <= 0:
                print("Error: Los créditos deben ser mayores a 0")
                return
        except ValueError:
            print("Error: Ingrese un número válido para créditos")
            return
        
        # Validar cupo máximo
        try:
            cupo_maximo = int(input("Ingrese cupo máximo del curso: "))
            if cupo_maximo <= 0:
                print("Error: El cupo máximo debe ser mayor a 0")
                return
        except ValueError:
            print("Error: Ingrese un número válido para el cupo")
            return
        
        nuevo_curso = Curso(id_curso, nombre, descripcion, creditos, cupo_maximo)
        self.cursos.append(nuevo_curso)
        print("¡Curso registrado con éxito!")
    
    def mostrar_cursos(self):
        """Muestra todos los cursos registrados"""
        print("\n=== LISTA DE CURSOS ===")
        
        if len(self.cursos) == 0:
            print("No hay cursos registrados")
            return
        
        for curso in self.cursos:
            curso.mostrar_info()
    
    def buscar_curso(self):
        """Busca un curso por su ID"""
        print("\n=== BUSCAR CURSO ===")
        id_buscar = input("Ingrese ID del curso: ")
        
        for curso in self.cursos:
            if curso.id_curso == id_buscar:
                print("\nCurso encontrado:")
                curso.mostrar_info()
                return
        print("Curso no encontrado.")
    
    def actualizar_curso(self):
        """Actualiza los datos de un curso existente"""
        print("\n=== ACTUALIZAR CURSO ===")
        id_buscar = input("Ingrese ID del curso a actualizar: ")
        
        for curso in self.cursos:
            if curso.id_curso == id_buscar:
                print("\nDeje en blanco si no desea modificar el campo")
                
                nombre = input(f"Nuevo nombre ({curso.nombre}): ")
                descripcion = input(f"Nueva descripción ({curso.descripcion}): ")
                
                creditos_input = input(f"Nuevos créditos ({curso.creditos}): ")
                creditos = int(creditos_input) if creditos_input else None
                
                cupo_input = input(f"Nuevo cupo máximo ({curso.cupo_maximo}): ")
                cupo_maximo = int(cupo_input) if cupo_input else None
                
                curso.actualizar_datos(
                    nombre=nombre if nombre else None,
                    descripcion=descripcion if descripcion else None,
                    creditos=creditos,
                    cupo_maximo=cupo_maximo
                )
                return
        print("Curso no encontrado.")
    
    def eliminar_curso(self):
        """Elimina un curso del sistema"""
        print("\n=== ELIMINAR CURSO ===")
        id_buscar = input("Ingrese ID del curso a eliminar: ")
        
        for curso in self.cursos:
            if curso.id_curso == id_buscar:
                # Verificar si hay estudiantes inscritos
                if curso.inscritos > 0:
                    print(f"No se puede eliminar el curso. Tiene {curso.inscritos} estudiante(s) inscrito(s).")
                    return
                
                self.cursos.remove(curso)
                print("Curso eliminado correctamente.")
                return
        print("Curso no encontrado.")
    
    def ver_cupos_disponibles(self):
        """Muestra los cupos disponibles de todos los cursos"""
        print("\n=== CUPOS DISPONIBLES POR CURSO ===")
        
        if len(self.cursos) == 0:
            print("No hay cursos registrados")
            return
        
        for curso in self.cursos:
            disponibles = curso.cupo_maximo - curso.inscritos
            print(f"Curso: {curso.nombre} (ID: {curso.id_curso})")
            print(f"  Cupos disponibles: {disponibles}/{curso.cupo_maximo}")
            print("-" * 30)