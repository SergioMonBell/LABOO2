class Coordenada:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def mostrar_coordenada(self):
        print(f"({self.coord_x},{self.coord_y})")


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


# Creación de instancias de Coordenada
vertice1 = Coordenada(1, 1)
vertice2 = Coordenada(10, 1)
vertice3 = Coordenada(10, 10)
vertice4 = Coordenada(1, 10)

# Creación de instancia de Cuadrado
cuadrado = Cuadrado(vertice1, vertice2, vertice3, vertice4)

# Llamada al método para mostrar los vértices
cuadrado.mostrar_vertices()