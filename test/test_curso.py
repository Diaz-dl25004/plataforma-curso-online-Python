import unittest
from modelos.cursos import Curso  

class TestCurso(unittest.TestCase):

    def setUp(self): #método especial que actua como preparador
        """Este método se ejecuta antes de CADA test. Ideal para preparar objetos limpios."""
        self.curso_prueba = Curso(
            id_curso="MAT101",
            nombre="Matemática Básica",
            descripcion="Curso de álgebra elemental",
            creditos=4,
            cupo_maximo=2,  # Ponemos un cupo bajo (2) para probar fácilmente el límite
            inscritos=0,
            tutor="Ing. Carlos Pérez"
        )

    #===================================================================================
    #================== COMPROBACIÓN DEL LÍMITE DE CUPOS ===============================
    def test_inscripcion_exitosa_y_limite_de_cupo(self):
        """Verifica que se puedan inscribir estudiantes y que respete el cupo máximo"""
        # 1. Primera inscripción (Debe permitirlo porque hay 2 cupos)
        resultado_1 = self.curso_prueba.inscribir_estudiante()
        self.assertTrue(resultado_1)
        self.assertEqual(self.curso_prueba.inscritos, 1)

        # 2. Segunda inscripción (Debe permitirlo, llegamos al límite)
        resultado_2 = self.curso_prueba.inscribir_estudiante()
        self.assertTrue(resultado_2)
        self.assertEqual(self.curso_prueba.inscritos, 2)
        self.assertFalse(self.curso_prueba.hay_cupo()) # Ya no debería haber cupo

        # 3. Tercera inscripción (Debe fallar porque el cupo máximo es 2)
        resultado_3 = self.curso_prueba.inscribir_estudiante()
        self.assertFalse(resultado_3)
        self.assertEqual(self.curso_prueba.inscritos, 2) # El contador no debió subir

    #==================================================================================
    #=================== COMPROBACIÓN PARA RESDUCCIÓN DE INSCRITOS ===================
    def test_desinscribir_estudiante(self):
        """Verifica que se reduzcan los inscritos correctamente y no baje de cero"""
        # Forzamos 1 inscrito para la prueba
        self.curso_prueba.inscritos = 1

        # Desinscripción válida
        resultado = self.curso_prueba.desinscribir_estudiante()
        self.assertTrue(resultado)
        self.assertEqual(self.curso_prueba.inscritos, 0)

        # Intentar desinscribir cuando ya está en 0 (No debe bajar a números negativos)
        resultado_negativo = self.curso_prueba.desinscribir_estudiante()
        self.assertFalse(resultado_negativo)
        self.assertEqual(self.curso_prueba.inscritos, 0)

    #=================================================================================
    #===== COMPROBACIÓN DE INTEGRIDAD DE DATOS-SERIALIZACIÓN Y DESERIALIZACIÓN =======
    def test_conversion_json(self):
        """Valida que to_dict y from_dict mantengan los datos intactos"""
        diccionario = self.curso_prueba.to_dict()
        curso_recuperado = Curso.from_dict(diccionario)

        self.assertEqual(self.curso_prueba.id_curso, curso_recuperado.id_curso)
        self.assertEqual(self.curso_prueba.nombre, curso_recuperado.nombre)
        self.assertEqual(self.curso_prueba.cupo_maximo, curso_recuperado.cupo_maximo)
        self.assertEqual(self.curso_prueba.tutor, curso_recuperado.tutor)
 
 # Ejecucion desde l terminal
if __name__ == "__main__":
    unittest.main()



