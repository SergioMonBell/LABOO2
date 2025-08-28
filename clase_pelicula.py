# clase_pelicula.py

class Pelicula:
    def __init__(self, titulo, duracion, categoria):
        self.titulo = titulo
        self.duracion = duracion  # en minutos
        self.categoria = categoria

    def __str__(self):
        return f"Título: {self.titulo} | Categoría: {self.categoria}"


class Cartelera:
    def __init__(self):
        self.peliculas = []

    def agregar(self, pelicula):
        if isinstance(pelicula, Pelicula):
            self.peliculas.append(pelicula)
            print(f"La película '{pelicula.titulo}' ha sido agregada a la cartelera.")
        else:
            print("Error: Solo se pueden agregar objetos de tipo Pelicula.")

    def imprimir(self):
        if not self.peliculas:
            print("La cartelera está vacía.")
        else:
            print("\n=== Cartelera de Películas ===")
            for p in self.peliculas:
                print(f"Título: {p.titulo} | Duración: {p.duracion} min | Categoría: {p.categoria}")


def pedir_datos_pelicula():
    """Solicita los datos de una película con validación."""
    titulo = input("Ingrese el título de la película: ").strip()
    while True:
        try:
            duracion = int(input("Ingrese la duración en minutos: "))
            if duracion <= 0:
                raise ValueError("La duración debe ser un número positivo.")
            break
        except ValueError as e:
            print(f"Error: {e}")
    categoria = input("Ingrese la categoría de la película: ").strip()
    return Pelicula(titulo, duracion, categoria)


if __name__ == "__main__":
    cartelera = Cartelera()

    while True:
        print("\n=== Menú ===")
        print("1. Agregar película")
        print("2. Mostrar cartelera")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        if opcion == "1":
            nueva_pelicula = pedir_datos_pelicula()
            cartelera.agregar(nueva_pelicula)
        elif opcion == "2":
            cartelera.imprimir()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Error: Opción inválida.")