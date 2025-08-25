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


# Ejemplo de uso
if __name__ == "__main__":
    contador = Contador()
    contador.obtener()       # Muestra 0
    contador.incrementar()   # Incrementa a 1
    contador.incrementar()   # Incrementa a 2
    contador.reiniciar()     # Reinicia a 0
