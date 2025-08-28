# clase_producto.py

class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    # Getters
    def get_codigo(self):
        return self.codigo

    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    # Setters
    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precio(self, precio):
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = precio

    # Método para calcular total
    def calcular_total(self, unidades):
        if unidades < 0:
            raise ValueError("Las unidades no pueden ser negativas.")
        total = self.precio * unidades
        return total


if __name__ == "__main__":
    # Entrada de datos del producto
    codigo = input("Ingrese el código del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()

    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio < 0:
                raise ValueError("El precio no puede ser negativo.")
            break
        except ValueError as e:
            print(f"Error: {e}")

    producto = Producto(codigo, nombre, precio)

    # Calcular el total
    while True:
        try:
            unidades = int(input("Ingrese la cantidad de unidades: "))
            if unidades < 0:
                raise ValueError("Las unidades no pueden ser negativas.")
            total = producto.calcular_total(unidades)
            print(f"El precio total por {unidades} unidades de '{producto.get_nombre()}' es: ${total:.2f}")
            break
        except ValueError as e:
            print(f"Error: {e}")
