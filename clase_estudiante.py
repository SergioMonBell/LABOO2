import datetime

class Estudiante:
    def __init__(self, nombre, fecha_nacimiento_str, escuela, universidad):
        try:
            self.nombre = nombre
            self.fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()
            self.escuela = escuela
            self.universidad = universidad
        except ValueError:
            raise ValueError("La fecha de nacimiento debe tener el formato dd/mm/yyyy y ser válida.")

    def imprimir(self):
        print("==============INFORMACION==============")
        print(f"Nombre: {self.nombre}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento.strftime('%d/%m/%Y')}")
        print(f"Escuela: {self.escuela}")
        print(f"Universidad: {self.universidad}")


def pedir_datos_estudiante():
    """Solicita los datos de un estudiante con validación."""
    nombre = input("Ingrese el nombre: ").strip()
    while True:
        fecha_nacimiento_str = input("Ingrese la fecha de nacimiento (dd/mm/yyyy): ").strip()
        try:
            datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y")  # Validación de fecha
            break
        except ValueError:
            print("Error: Formato de fecha inválido. Use dd/mm/yyyy.")
    escuela = input("Ingrese la escuela: ").strip()
    universidad = input("Ingrese la universidad: ").strip()
    return Estudiante(nombre, fecha_nacimiento_str, escuela, universidad)


if __name__ == "__main__":
    estudiante = pedir_datos_estudiante()
    estudiante.imprimir()