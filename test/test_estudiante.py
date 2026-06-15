# Creación de una prueba unitaria para verificar la persistencia de la informaión
# Consiste en verificar que durante el proceso de convertir un un objeto Estudiante a diccionario 
# y luego de diccionario reconstruirlo a objeto, este no pierda información.
import unittest
from modelos.estudiante import Estudiante

class TestEstudiante(unittest.TestCase):
    def test_conversion_completa(self):
        # El contructor de Estudiante inicia con estos parámetros __init__(self, id_estudiante, nombre, correo, edad):
        estudiante_original = Estudiante("HP0032", "Katherine Alejandra", "ale@gmail.com", 25)  
        
        # Se guarrda en diccionario lo que el metodo to_dict() entrega. De objeto a diccionario
        diccionario = estudiante_original.to_dict()
        # estudiante_recuperado guarda el objeto reconstruido a  partir del diccionario
        estudiante_recuperado = Estudiante.from_dict(diccionario)

        # Se procede a hacer las comparaciones para verificar la integridad de los datos
        # Prueba de las funciones to_dict y from_dict
        
        # id = id
        self.assertEqual(
            estudiante_original.id_estudiante,
            estudiante_recuperado.id_estudiante
        )
        
        # nombre = nombre
        self.assertEqual(
            estudiante_original.nombre,
            estudiante_recuperado.nombre
        )
        
        # correo = correo
        self.assertEqual(
            estudiante_original.correo,
            estudiante_recuperado.correo
        )
        
        #edad = edad
        self.assertEqual(
            estudiante_original.edad,
            estudiante_recuperado.edad
        )

# ejecución desde la terminal
if __name__ == "__main__":
    unittest.main()




