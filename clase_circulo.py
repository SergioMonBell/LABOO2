# clase_circulo.py
import math

class Circulo:
    def __init__(self, radio):
        if not isinstance(radio, (int, float)):
            raise ValueError("El radio debe ser un número.")
        if radio <= 0:
            raise ValueError("El radio debe ser un número positivo.")
        self.radio = radio
        self.PI = math.pi  # Constante PI

    def calculo_area(self):
        """Calcula y devuelve el área del círculo."""
        return self.PI * (self.radio ** 2)


if __name__ == "__main__":
    while True:
        try:
            radio_usuario = float(input("Ingrese el radio del círculo: "))
            circulo = Circulo(radio_usuario)
            print(f"El área del círculo es: {circulo.calculo_area():.2f}")
            break
        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.")
