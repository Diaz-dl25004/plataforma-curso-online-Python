# Lista para guardar los cursos (aquí guardaremos diccionarios con nombre y precio)
cursos = []

def gestion_cursos():
    while True:
        print("\n--- SISTEMA DE GESTION DE CURSOS EDUTEC ONLINE ---")
        print("1. Agregar Curso")
        print("2. Chequear los cursos activos")
        print("3. Editar un curso")
        print("4. Eliminar un curso")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Apartado para agregar cursos 
            nombre = input("Ingrese nombre del curso: ")
            precio = input("Ingrese precio del curso: ")
            # En Python solo hacemos .append y listo, no necesitamos contador 
            cursos.append({"nombre": nombre, "precio": precio})
            print("¡Curso Agregado con Éxito!")

        elif opcion == "2":
            # Apartado para checar cursos registrados 
            if not cursos:
                print("No hay cursos registrados.")
            else:
                print("\nListado de Cursos:")
                # enumerate da el número de orden automáticamente
                for i, curso in enumerate(cursos, 1):
                    print(f"{i}. {curso['nombre']} - ${curso['precio']}")

        elif opcion == "3":
            # Apartado para editar cursos 
            if not cursos:
                print("No hay nada que editar.")
                continue
                
            try:
                indice = int(input("Ingrese el número de curso a editar: ")) - 1
                if 0 <= indice < len(cursos):
                    cursos[indice]['nombre'] = input("Nuevo Nombre: ")
                    cursos[indice]['precio'] = input("Nuevo Precio: ")
                    print("¡Curso editado con éxito!")
                else:
                    print("Curso no encontrado.")
            except ValueError:
                print("Error: Por favor ingrese un número válido.")

        elif opcion == "4":
            # Apartado para eliminar cursos 
            if not cursos:
                print("No hay cursos para eliminar.")
                continue

            try:
                indice = int(input("Número de curso a eliminar: ")) - 1
                if 0 <= indice < len(cursos):
                    # .pop() elimina y reordena todo automáticamente
                    eliminado = cursos.pop(indice)
                    print(f"¡Curso '{eliminado['nombre']}' eliminado con éxito!")
                else:
                    print("Error: El curso no existe.")
            except ValueError:
                print("Error: Ingrese un número de índice válido.")

        elif opcion == "5":
            print("Saliendo del módulo de cursos...")
            break
        else:
            print("Opción incorrecta, intente de nuevo.")

# Para probarlo
if __name__ == "__main__":
    gestion_cursos()