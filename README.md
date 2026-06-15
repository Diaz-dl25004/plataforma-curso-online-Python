# Plataforma de Cursos Online - Sistema de Gestión Académica

Proyecto final de la asignatura **Lógica de Programación**  
Ciclo I / 2026 – Ingeniería en Desarrollo de Software

---

## Descripción

Este proyecto es una aplicación de línea de comandos (CLI) desarrollada en **Python** que permite gestionar una plataforma de cursos online.  
El sistema administra **estudiantes**, **cursos** e **inscripciones**, almacenando toda la información en archivos **JSON** para garantizar la persistencia de los datos entre ejecuciones.

Incluye **pruebas unitarias** para verificar la integridad de los datos y las reglas de negocio (verificación de persistencia de información, inscripción exitosa, límite de cupos, etc.), cumpliendo con los requisitos de la tercera entrega del proyecto.

---

## Integrantes del equipo

| Integrante | Módulo asignado |
|---|---|
| José Adalberto Díaz Lue | Gestión de Estudiantes |
| Byron Antonio Fuentes Escobar | Gestión de Cursos |
| Paola Sugey Hércules Jirón | Gestión de Inscripciones |

---

## Requisitos previos

- **Python 3.10 o superior** instalado.
- **Git** (opcional, para clonar el repositorio).
- Editor de texto o IDE de su preferencia (VS Code, PyCharm, etc.).
- Los archivos JSON de datos se generan automáticamente en la carpeta `datos/` al ejecutar el programa por primera vez.

---

## Instalación y configuración

1. **Clonar el repositorio** desde GitHub:

```bash
git clone https://github.com/Diaz-dl25004/plataforma-curso-online-Python.git
cd plataforma-curso-online-Python
```

2. **Ejecutar** el programa desde la raíz del proyecto:

```bash
python main.py
```

Al ejecutarlo verá el siguiente menú en consola:

```
=== PLATAFORMA DE CURSOS ONLINE ===

=========== BIENVENIDOS ===========
1. Gestión de Estudiantes
2. Gestión de Cursos
3. Gestión de Inscripciones
4. Salir
```

**Ejemplo de uso:**

- Para registrar un estudiante: seleccione la opción `1`, luego `1`, e ingrese los datos solicitados.
- Para registrar un curso: seleccione la opción `2`, luego `1`, e ingrese los datos solicitados.
- Para inscribir un estudiante en un curso: seleccione la opción `3`, luego `1`, y siga las instrucciones en pantalla.
- Los datos se guardan automáticamente en archivos JSON dentro de la carpeta `datos/`.

---

## Estructura del Proyecto

```
plataforma-curso-online-Python/
├── datos/                     # Archivos JSON con datos persistentes
│   ├── cursos.json
│   ├── estudiantes.json
│   ├── inscripciones.json
│   └── tutores.json
├── menus/                     # Menús de la CLI
│   ├── menu_cursos.py
│   ├── menu_estudiantes.py
│   ├── menu_inscripciones.py
│   └── menu_principal.py
├── modelos/                   # Definición de las clases (objetos)
│   ├── curso.py
│   ├── estudiante.py
│   ├── inscripcion.py
│   └── instructor.py
├── modulos/                   # Gestores de cada entidad (lógica CRUD)
│   ├── cursos.py
│   ├── estudiantes.py
│   ├── inscripciones.py
│   └── instructores.py
├── test/                      # Pruebas unitarias
│   ├── __init__.py
│   ├── test_cursos.py
│   ├── test_estudiante.py
│   └── test_inscripciones.py
├── .gitignore                 # Archivos ignorados por Git
├── README.md                  # Documentación del proyecto
└── main.py                    # Punto de entrada de la aplicación
```

---

## Pruebas Unitarias

Las pruebas unitarias están implementadas con el módulo `unittest` de Python y se encuentran en la carpeta `test/`.

**Para ejecutar todas las pruebas:**

```bash
python -m unittest discover test
```

**Para ejecutar con detalle de cada prueba:**

```bash
python -m unittest discover test -v
```

Se espera que todas las pruebas pasen con `OK`.

---

### Pruebas por módulo

#### Módulo de Estudiantes — `test_estudiante.py`

Verifica la **integridad de datos** durante la conversión de objeto a diccionario y viceversa (`to_dict` / `from_dict`), asegurando que ningún atributo se pierda al guardar o cargar desde JSON.

| Prueba | Descripción |
|---|---|
| `test_conversion_completa` | Verifica que `id_estudiante`, `nombre`, `correo` y `edad` se mantienen intactos tras convertir el objeto a diccionario y reconstruirlo |

---

#### Módulo de Cursos — `test_cursos.py`

Verifica las reglas de negocio relacionadas con el manejo de cupos y la persistencia de datos del curso.

| Prueba | Descripción |
|---|---|
| `test_inscripcion_exitosa_y_limite_de_cupo` | Verifica que se permiten inscripciones mientras hay cupo y que se bloquean al alcanzar el máximo |
| `test_desinscribir_estudiante` | Verifica que los inscritos se reducen correctamente y que el contador no baja de cero |
| `test_conversion_json` | Valida que `to_dict` y `from_dict` mantienen todos los datos del curso intactos |

---

#### Módulo de Inscripciones — `test_inscripciones.py`

Verifica tanto la integridad de datos como la lógica de negocio del gestor de inscripciones. Usa archivos temporales para no modificar los datos reales y `unittest.mock` para simular entradas del usuario.

| Prueba | Descripción |
|---|---|
| `test_conversion_completa` | Verifica que `id_inscripcion`, `id_estudiante`, `id_curso` y `tutor` se mantienen intactos tras la conversión `to_dict` / `from_dict` |
| `test_inscribir_estudiante_exitoso` | Verifica que la inscripción se registra correctamente y que el cupo del curso disminuye |
| `test_inscribir_estudiante_duplicado` | Verifica que el sistema impide inscribir al mismo estudiante dos veces en el mismo curso |

---

## Funcionalidades implementadas

| Módulo | CRUD completo | Persistencia JSON | Pruebas unitarias |
|---|---|---|---|
| Estudiantes | ✅ Sí | ✅ Sí | ✅ Sí (`test_estudiante.py`) |
| Cursos | ✅ Sí | ✅ Sí | ✅ Sí (`test_cursos.py`) |
| Inscripciones | ✅ Sí | ✅ Sí | ✅ Sí (`test_inscripciones.py`) |

---

## Tecnologías utilizadas

- **Python 3.10+** — Lenguaje de programación.
- **JSON** — Persistencia de datos entre ejecuciones.
- **unittest** — Framework para pruebas unitarias.
- **unittest.mock** — Simulación de entradas del usuario en pruebas.
- **Git / GitHub** — Control de versiones y repositorio remoto.

---

## Licencia

Este proyecto fue desarrollado con fines educativos para la asignatura de Lógica de Programación.  
Queda prohibida su reproducción con fines comerciales sin autorización expresa de los autores.
