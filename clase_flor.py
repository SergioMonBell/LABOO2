# clase_flor.py

class Flor:
    def __init__(self, color, tamano, aspecto):
        self.color = color
        self.tamano = tamano
        self.aspecto = aspecto

    def imprimir(self):
        print("\n--- Datos de la Flor ---")
        print(f"Color: {self.color}")
        print(f"Tamaño: {self.tamano}")
        print(f"Aspecto: {self.aspecto}")


def pedir_dato(mensaje):
    """Pide un dato al usuario y valida que no esté vacío."""
    while True:
        try:
            valor = input(mensaje).strip()
            if not valor:
                raise ValueError("El campo no puede estar vacío.")
            return valor
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    try:
        color = pedir_dato("Ingrese el color de la flor: ")
        tamano = pedir_dato("Ingrese el tamaño de la flor: ")
        aspecto = pedir_dato("Ingrese el aspecto de la flor: ")

        mi_flor = Flor(color, tamano, aspecto)
        mi_flor.imprimir()

    except KeyboardInterrupt:
        print("\nEjecución interrumpida por el usuario.")