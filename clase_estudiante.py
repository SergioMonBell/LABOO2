import datetime

class Estudiante:
    nombre = ""
    fecha_nacimiento = ""
    escuela = ""
    universidad = ""

    def __init__(self, nombre, fecha_nacimiento_str, escuela, universidad):
        self.nombre = nombre
        self.fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento_str, "%d/%m/%Y").date()
        self.escuela = escuela
        self.universidad = universidad

    def imprimir(self):
        print("==============INFORMACION==============")
        print(f"Nombre: {self.nombre}")
        print(f"Fecha de nacimiento: {self.fecha_nacimiento.strftime('%d/%m/%Y')}")
        print(f"Escuela: {self.escuela}")
        print(f"Universidad: {self.universidad}")

# Crear instancia y mostrar información
leandro = Estudiante("Leandro", "01/01/2008", "Sistemas", "UCSM")
leandro.imprimir()
