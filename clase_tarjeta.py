# clase_tarjeta.py

class Tarjeta:
    def __init__(self, id_tarjeta, saldo_inicial):
        """Constructor de la clase Tarjeta."""
        self.id = id_tarjeta
        self.saldo = saldo_inicial

    def muestra_saldo(self):
        """Muestra el saldo actual."""
        print(f" Saldo actual de la tarjeta {self.id}: {self.saldo:.2f} USD")

    def __str__(self):
        """Representación en texto de la tarjeta."""
        return f"Tarjeta(ID: {self.id}, Saldo: {self.saldo:.2f} USD)"


# Ejemplo de uso
if __name__ == "__main__":
    try:
        id_tarjeta = input("Ingrese el ID de la tarjeta: ")
        saldo_inicial = float(input("Ingrese el saldo inicial: "))
        
        tarjeta = Tarjeta(id_tarjeta, saldo_inicial)
        
        print("\n--- Información de la Tarjeta ---")
        print(tarjeta)  # Llama al método __str__
        
        tarjeta.muestra_saldo()
        
    except ValueError:
        print(" Error: El saldo debe ser un número.")
