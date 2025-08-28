class Persona:
    def __init__(self, nombre="Dely", apellido="Lazo", genero="Femenino"):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero

    def mostrar(self):
        print(f"Nombre completo: {self.apellido} {self.nombre}")
        print(f"Género: {self.genero}")


def pedir_datos_persona():
    """Solicita los datos de la persona con validación."""
    while True:
        nombre = input("Ingrese el nombre: ").strip()
        if nombre:
            break
        print("Error: El nombre no puede estar vacío.")

    while True:
        apellido = input("Ingrese el apellido: ").strip()
        if apellido:
            break
        print("Error: El apellido no puede estar vacío.")

    while True:
        genero = input("Ingrese el género (Masculino/Femenino): ").strip().capitalize()
        if genero in ["Masculino", "Femenino"]:
            break
        print("Error: El género debe ser 'Masculino' o 'Femenino'.")

    return Persona(nombre, apellido, genero)


if __name__ == "__main__":
    persona1 = pedir_datos_persona()

    print(f"\nAntes: {persona1.nombre}")
    persona1.nombre = input("Ingrese un nuevo nombre para la persona: ").strip()
    print(f"Después: {persona1.nombre}")

    persona1.mostrar()