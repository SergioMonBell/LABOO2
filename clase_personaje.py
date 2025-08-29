# clase_personaje.py

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = self.validar_nombre(nombre)
        self.fuerza = self.validar_atributo(fuerza, "Fuerza")
        self.inteligencia = self.validar_atributo(inteligencia, "Inteligencia")
        self.defensa = self.validar_atributo(defensa, "Defensa")
        self.vida = self.validar_atributo(vida, "Vida")

    def validar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return nombre.strip().capitalize()

    def validar_atributo(self, valor, nombre_atributo):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError(f"{nombre_atributo} debe ser un número positivo.")
        return valor

    def mostrar_atributos(self):
        print("\n=== ATRIBUTOS DEL PERSONAJE ===")
        print(f"Nombre: {self.nombre}")
        print(f"Fuerza: {self.fuerza}")
        print(f"Inteligencia: {self.inteligencia}")
        print(f"Defensa: {self.defensa}")
        print(f"Vida: {self.vida}")
        print("===============================")

    def subir_nivel(self, fuerza_extra=1, inteligencia_extra=1, defensa_extra=1, vida_extra=10):
        self.fuerza += fuerza_extra
        self.inteligencia += inteligencia_extra
        self.defensa += defensa_extra
        self.vida += vida_extra
        print(f"\n¡{self.nombre} ha subido de nivel!")
        self.mostrar_atributos()

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(f"\n {self.nombre} ha muerto.")


if __name__ == "__main__":
    try:
        nombre = input("Ingrese el nombre del personaje: ")
        fuerza = int(input("Ingrese la fuerza: "))
        inteligencia = int(input("Ingrese la inteligencia: "))
        defensa = int(input("Ingrese la defensa: "))
        vida = int(input("Ingrese la vida: "))

        personaje = Personaje(nombre, fuerza, inteligencia, defensa, vida)

        personaje.mostrar_atributos()

        # Subir de nivel
        opcion = input("\n¿Desea subir de nivel? (s/n): ").lower()
        if opcion == "s":
            personaje.subir_nivel()

        # Simular muerte
        opcion = input("\n¿Desea matar al personaje? (s/n): ").lower()
        if opcion == "s":
            personaje.morir()

        # Verificar si está vivo
        if personaje.esta_vivo():
            print(f"\n {personaje.nombre} sigue vivo.")
        else:
            print(f"\n {personaje.nombre} está muerto.")

    except ValueError as e:
        print(f"Error: {e}")
