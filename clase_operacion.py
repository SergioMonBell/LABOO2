# clase_operacion.py

class Operacion:
    def __init__(self, num1, num2):
        if num1 < 0 or num2 < 0:
            raise ValueError("Los números deben ser naturales (mayores o iguales a 0).")
        self.num1 = num1
        self.num2 = num2

    def sumar(self):
        resultado = self.num1 + self.num2
        print(f"{self.num1} + {self.num2} = {resultado}")

    def restar(self):
        resultado = self.num1 - self.num2
        print(f"{self.num1} - {self.num2} = {resultado}")

    def multiplicar(self):
        resultado = self.num1 * self.num2
        print(f"{self.num1} × {self.num2} = {resultado}")

    def division(self):
        if self.num2 == 0:
            print("Error: No se puede dividir entre cero.")
        else:
            resultado = self.num1 / self.num2
            print(f"{self.num1} ÷ {self.num2} = {resultado}")


def pedir_numero(mensaje):
    """Pide un número natural con validación."""
    while True:
        try:
            num = int(input(mensaje))
            if num < 0:
                raise ValueError("Debe ser un número natural (≥ 0).")
            return num
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    print("=== Calculadora de Operaciones ===")
    n1 = pedir_numero("Ingrese el primer número: ")
    n2 = pedir_numero("Ingrese el segundo número: ")

    operacion = Operacion(n1, n2)

    print("\nResultados:")
    operacion.sumar()
    operacion.restar()
    operacion.multiplicar()
    operacion.division()