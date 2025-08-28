# clase_contador.py

class Contador:
    def __init__(self, valor=0):
        self.valor = valor

    def obtener(self):
        print(f"Valor del contador: {self.valor}")

    def reiniciar(self):
        self.valor = 0
        print("Contador reiniciado a 0.")

    def incrementar(self):
        self.valor += 1
        print(f"Contador incrementado a: {self.valor}")


def pedir_entero(mensaje):
    """Solicita al usuario un número entero válido."""
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: Debes ingresar un número entero.")


if __name__ == "__main__":
    print("=== Programa Contador ===")
    valor_inicial = pedir_entero("Ingrese el valor inicial del contador: ")
    contador = Contador(valor_inicial)

    while True:
        print("\nOpciones:")
        print("1. Mostrar valor del contador")
        print("2. Incrementar contador")
        print("3. Reiniciar contador")
        print("4. Salir")

        opcion = input("Seleccione una opción (1-4): ")

        try:
            if opcion == "1":
                contador.obtener()
            elif opcion == "2":
                contador.incrementar()
            elif opcion == "3":
                contador.reiniciar()
            elif opcion == "4":
                print("Saliendo del programa...")
                break
            else:
                raise ValueError("Opción no válida.")
        except ValueError as e:
            print(f"Error: {e}")