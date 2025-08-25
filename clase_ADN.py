# clase_adn.py

class DNA:
    def __init__(self, secuencia):
        self.secuencia = secuencia.upper()  # Convertir a mayúsculas para consistencia

    def contar_bases(self):
        """Cuenta la cantidad de cada base nitrogenada."""
        bases = {"A": 0, "C": 0, "G": 0, "T": 0}
        for base in self.secuencia:
            if base in bases:
                bases[base] += 1
        return bases

    def fusionar(self, otra_secuencia):
        """Fusiona la secuencia actual con otra."""
        if isinstance(otra_secuencia, DNA):
            self.secuencia += otra_secuencia.secuencia
        else:
            raise ValueError("El argumento debe ser un objeto DNA")

    def composicion_porcentual(self):
        """Calcula el porcentaje de cada base en la secuencia."""
        total = len(self.secuencia)
        if total == 0:
            return {"A": 0, "C": 0, "G": 0, "T": 0}
        conteo = self.contar_bases()
        porcentaje = {base: (conteo[base] / total) * 100 for base in conteo}
        return porcentaje

    def similitud(self, otra_secuencia):
        """Calcula la similitud con otra secuencia como porcentaje de coincidencia."""
        if not isinstance(otra_secuencia, DNA):
            raise ValueError("El argumento debe ser un objeto DNA")
        longitud_min = min(len(self.secuencia), len(otra_secuencia.secuencia))
        if longitud_min == 0:
            return 0.0
        coincidencias = sum(1 for i in range(longitud_min) if self.secuencia[i] == otra_secuencia.secuencia[i])
        return (coincidencias / longitud_min) * 100

    def imprimir(self):
        """Muestra información completa de la secuencia."""
        print(f"Secuencia: {self.secuencia}")
        print(f"Conteo de bases: {self.contar_bases()}")
        print(f"Composición porcentual: {self.composicion_porcentual()}")


# Ejemplo de uso
if __name__ == "__main__":
    adn1 = DNA("ATGCGTA")
    adn2 = DNA("ATGCCGA")

    print("ADN 1:")
    adn1.imprimir()
    print("\nADN 2:")
    adn2.imprimir()

    print("\nSimilitud entre ADN 1 y ADN 2:")
    print(f"{adn1.similitud(adn2):.2f}%")

    print("\nFusionando ADN 1 y ADN 2...")
    adn1.fusionar(adn2)
    adn1.imprimir()
