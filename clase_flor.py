# clase_flor.py

class Flor:
    def __init__(self, color, tamano, aspecto):
        self.color = color
        self.tamano = tamano
        self.aspecto = aspecto

    def imprimir(self):
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamano}")
        print(f"Aspecto: {self.aspecto}")


# Ejemplo de uso
if __name__ == "__main__":
    mi_flor = Flor("Rojo", "Mediano", "Hermosa y fragante")
    mi_flor.imprimir()
