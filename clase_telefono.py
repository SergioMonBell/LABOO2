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
        print("\n=== Información del Teléfono ===")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Número: {self.numero}")


def pedir_datos_telefono():
    """Solicita los datos del teléfono con validación."""
    marca = input("Ingrese la marca del teléfono: ").strip()
    modelo = input("Ingrese el modelo del teléfono: ").strip()

    while True:
        numero = input("Ingrese el número telefónico (ej: 555-1234): ").strip()
        if numero.replace("-", "").isdigit():
            break
        print("Error: El número debe contener solo dígitos y guiones.")

    return Telefono(marca, modelo, numero)


if __name__ == "__main__":
    telefono = pedir_datos_telefono()

    while True:
        print("\n=== Menú ===")
        print("1. Mostrar datos del teléfono")
        print("2. Llamar a un número")
        print("3. Salir")

        opcion = input("Seleccione una opción (1-3): ")

        try:
            if opcion == "1":
                telefono.mostrar_datos()
            elif opcion == "2":
                destino = input("Ingrese el número de destino: ").strip()
                if destino.replace("-", "").isdigit():
                    telefono.llamar(destino)
                else:
                    print("Error: El número de destino no es válido.")
            elif opcion == "3":
                print("Saliendo del programa...")
                break
            else:
                raise ValueError("Opción inválida. Debe ser 1, 2 o 3.")
        except ValueError as e:
            print(f"Error: {e}")