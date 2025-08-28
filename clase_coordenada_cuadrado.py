class Coordenada:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def mostrar_coordenada(self):
        print(f"({self.coord_x}, {self.coord_y})")


class Cuadrado:
    def __init__(self, vertice1, vertice2, vertice3, vertice4):
        self.vertice1 = vertice1
        self.vertice2 = vertice2
        self.vertice3 = vertice3
        self.vertice4 = vertice4

    def mostrar_vertices(self):
        print("El cuadrado está compuesto por los siguientes vértices:")
        self.vertice1.mostrar_coordenada()
        self.vertice2.mostrar_coordenada()
        self.vertice3.mostrar_coordenada()
        self.vertice4.mostrar_coordenada()


def pedir_coordenada(nombre_vertice):
    """Solicita al usuario una coordenada (x, y) válida."""
    while True:
        try:
            x = float(input(f"Ingrese la coordenada X de {nombre_vertice}: "))
            y = float(input(f"Ingrese la coordenada Y de {nombre_vertice}: "))
            return Coordenada(x, y)
        except ValueError:
            print("Error: Debe ingresar un número válido para la coordenada.")


if __name__ == "__main__":
    print("=== Creación de un Cuadrado ===")

    v1 = pedir_coordenada("Vértice 1")
    v2 = pedir_coordenada("Vértice 2")
    v3 = pedir_coordenada("Vértice 3")
    v4 = pedir_coordenada("Vértice 4")

    cuadrado = Cuadrado(v1, v2, v3, v4)
    cuadrado.mostrar_vertices()