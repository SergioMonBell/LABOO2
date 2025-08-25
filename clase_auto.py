# clase_auto.py

class Auto:
    def __init__(self, marca, modelo, anio, color):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color

    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")


# Crear objeto taxi
if __name__ == "__main__":
    taxi = Auto("Toyota", "Corolla", 2020, "Amarillo")
    taxi.imprimir()
