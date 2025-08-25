# clase_libro.py

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
        print(f"ISBN: {self.isbn}")
        print(f"Título: {self.titulo}")
        print(f"Editorial: {self.editorial}")
        print(f"Año de publicación: {self.anio}")
        print(f"Precio: ${self.precio}")
        estado = "Prestado" if self.prestado else "Disponible"
        print(f"Estado: {estado}")


# Ejemplo de uso
if __name__ == "__main__":
    libro1 = Libro("978-3-16-148410-0", "Python Básico", "Editorial ABC", 2023, 29.99)
    
    libro1.mostrar_datos()
    print()
    
    libro1.prestar()
    libro1.mostrar_datos()
    print()
    
    libro1.devolver()
    libro1.mostrar_datos()
