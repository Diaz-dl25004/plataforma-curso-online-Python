# Archivo: test/test_inscripciones.py
# Pruebas unitarias para el módulo de inscripciones

import unittest
import sys
import os
import tempfile
from unittest.mock import patch

# Ajuste de ruta para importar módulos del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modelos.inscripcion import Inscripcion
from modulos.inscripciones import GestorInscripcion
from modulos.estudiantes import GestorEstudiante
from modulos.cursos import GestorCurso
from modelos.estudiante import Estudiante
from modelos.cursos import Curso


class TestInscripcion(unittest.TestCase):
    """Prueba 1: Integridad de datos en la clase Inscripcion (to_dict / from_dict)"""

    def test_conversion_completa(self):
        inscripcion_original = Inscripcion(
            id_inscripcion=5,
            id_estudiante="E001",
            id_curso="C001",
            tutor="Ing. Walter Ernesto Andrade Mejía"
        )

        diccionario = inscripcion_original.to_dict()
        inscripcion_recuperada = Inscripcion.from_dict(diccionario)

        self.assertEqual(inscripcion_original.id_inscripcion,
                         inscripcion_recuperada.id_inscripcion)
        self.assertEqual(inscripcion_original.id_estudiante,
                         inscripcion_recuperada.id_estudiante)
        self.assertEqual(inscripcion_original.id_curso,
                         inscripcion_recuperada.id_curso)
        self.assertEqual(inscripcion_original.tutor,
                         inscripcion_recuperada.tutor)


class TestGestorInscripcion(unittest.TestCase):
    """Prueba 2: Funcionalidad del gestor de inscripciones"""

    def setUp(self):
        # Crear gestores de estudiantes y cursos sin datos reales
        self.gestor_estudiante = GestorEstudiante()
        self.gestor_curso = GestorCurso()

        # Limpiar listas
        self.gestor_estudiante.estudiantes = []
        self.gestor_curso.cursos = []

        # Agregar estudiantes de prueba
        est1 = Estudiante("E001", "Juan Pérez", "juan@test.com", 22)
        est2 = Estudiante("E002", "Ana Gómez", "ana@test.com", 24)
        self.gestor_estudiante.estudiantes.extend([est1, est2])

        # Agregar cursos de prueba
        curso1 = Curso("C001", "Python Básico", "Introducción",
                       3, 25, 0, "Ing. Tutor1")
        curso2 = Curso("C002", "Java Avanzado", "POO",
                       4, 20, 0, "Ing. Tutor2")
        self.gestor_curso.cursos.extend([curso1, curso2])

        # Crear gestor de inscripciones
        self.gestor_inscripcion = GestorInscripcion(self.gestor_estudiante,
                                                   self.gestor_curso)

        # 🔥 CORRECCIÓN IMPORTANTE:
        # Vaciar la lista de inscripciones que se cargaron del JSON real
        self.gestor_inscripcion.inscripciones = []
        self.gestor_inscripcion.contador_id = 1

        # (Opcional) Usar archivo temporal para no modificar el original
        self.temp_archivo = tempfile.NamedTemporaryFile(
            mode='w+', encoding='utf-8', delete=False)
        self.temp_archivo.write('[]')
        self.temp_archivo.close()
        self.gestor_inscripcion.archivo = self.temp_archivo.name

    def tearDown(self):
        if os.path.exists(self.temp_archivo.name):
            os.unlink(self.temp_archivo.name)

    def test_inscribir_estudiante_exitoso(self):
        # Simular entrada del usuario
        with patch('builtins.input', side_effect=['E001', '1']):
            self.gestor_inscripcion.inscribir_estudiante()

        # Verificar que solo hay UNA inscripción
        self.assertEqual(len(self.gestor_inscripcion.inscripciones), 1)

        # Verificar datos de la inscripción
        insc = self.gestor_inscripcion.inscripciones[0]
        self.assertEqual(insc.id_estudiante, "E001")
        self.assertEqual(insc.id_curso, "C001")

        # Verificar que el curso aumentó sus inscritos
        curso = self.gestor_curso.cursos[0]
        self.assertEqual(curso.inscritos, 1)


if __name__ == "__main__":
    unittest.main()