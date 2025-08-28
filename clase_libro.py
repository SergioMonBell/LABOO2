class Libro:
    def __init__(self, isbn, titulo, editorial, anio, precio):
        self.isbn = isbn
        self.titulo = titulo
        self.editorial = editorial
        self.anio = anio
        self.precio = precio
        self.prestado = False  # Indica si el libro está prestado o no

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        if self.prestado:
            self.prestado = False
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' no estaba prestado.")

    def mostrar_datos(self):
        print("\n===== Información del libro =====")
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Editorial: {self.editorial}")
        print(f"Año de publicación: {self.anio}")
        print(f"Precio: ${self.precio:.2f}")
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"Estado: {estado}")


def pedir_datos_libro():
    """Solicita los datos del libro con validación."""
    isbn = input("Ingrese el ISBN: ").strip()
    titulo = input("Ingrese el título: ").strip()
    editorial = input("Ingrese la editorial: ").strip()

    while True:
        try:
            anio = int(input("Ingrese el año de publicación: "))
            if anio <= 0:
                raise ValueError("El año debe ser un número positivo.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    return Libro(isbn, titulo, editorial, anio, precio)


if __name__ == "__main__":
    libro = pedir_datos_libro()

    while True:
        print("\n=== Menú de opciones ===")
        print("1. Mostrar datos del libro")
        print("2. Prestar libro")
        print("3. Devolver libro")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        try:
            if opcion == "1":
                libro.mostrar_datos()
            elif opcion == "2":
                libro.prestar()
            elif opcion == "3":
                libro.devolver()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                raise ValueError("Opción inválida. Elija un número del 1 al 4.")
        except ValueError as e:
            print(f"Error: {e}")