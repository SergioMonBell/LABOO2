# clase_telefono.py

class Telefono:
    def __init__(self, marca, modelo, numero):
        self.marca = marca
        self.modelo = modelo
        self.numero = numero

    def llamar(self, destino):
        """Simula una llamada telefónica al número destino."""
        print(f"Llamando desde {self.numero} a {destino}...")

    def mostrar_datos(self):
        """Muestra los datos completos del teléfono."""
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Número: {self.numero}")


# Ejemplo de uso
if __name__ == "__main__":
    mi_telefono = Telefono("Samsung", "Galaxy S21", "555-1234")
    
    mi_telefono.mostrar_datos()
    print()
    
    mi_telefono.llamar("555-5678")
