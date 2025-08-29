# clase_alumno.py

import re

class Alumno:
    contador_alumnos = 1  # Controla el autoincremento del código

    def __init__(self, nombre, apellidos, codigo_alumno=None, notas=None):
        self.nombre = self.validar_nombre(nombre)
        self.apellidos = self.validar_apellidos(apellidos)
        self.codigo_alumno = self.validar_codigo(codigo_alumno)
        self.notas = self.validar_notas(notas if notas else [])

    def validar_nombre(self, nombre):
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        return nombre.strip().capitalize()

    def validar_apellidos(self, apellidos):
        if not apellidos or not apellidos.strip():
            raise ValueError("El apellido no puede estar vacío.")
        return apellidos.strip().capitalize()

    def validar_codigo(self, codigo):
        if not codigo:
            codigo = f"A{Alumno.contador_alumnos:04d}"
            Alumno.contador_alumnos += 1
            return codigo

        if not re.match(r"^A\d{4}$", codigo):
            raise ValueError("El código debe tener el formato 'A0001'.")
        return codigo.upper()

    def validar_notas(self, notas):
        notas_validadas = []
        for i in range(4):
            try:
                nota = int(notas[i]) if i < len(notas) and notas[i] != "" else 0
                if nota < 0 or nota > 20:
                    raise ValueError
            except ValueError:
                raise ValueError(f"La nota {i+1} debe ser un número entero entre 0 y 20.")
            notas_validadas.append(nota)
        return notas_validadas

    def informacion(self):
        print(f"Código de alumno: {self.codigo_alumno}")
        print(f"Apellido del alumno: {self.apellidos}")
        print(f"Nombre del alumno: {self.nombre}")

    def promedio(self):
        for i, nota in enumerate(self.notas, 1):
            print(f"Nota_{i}: {nota}")
        promedio_final = sum(self.notas) / 4
        print(f"Promedio final: {promedio_final:.2f}")


if __name__ == "__main__":
    while True:
        try:
            nombre = input("Ingrese el nombre del alumno: ")
            apellidos = input("Ingrese los apellidos del alumno: ")
            codigo = input("Ingrese el código del alumno (o deje vacío para autogenerar): ")

            notas = []
            for i in range(1, 5):
                valor = input(f"Ingrese la nota {i} (0-20, o vacío para 0): ").strip()
                notas.append(valor if valor != "" else 0)

            alumno = Alumno(nombre, apellidos, codigo, notas)
            print("\n=== Información del Alumno ===")
            alumno.informacion()
            print("\n=== Notas y Promedio ===")
            alumno.promedio()
            break

        except ValueError as e:
            print(f"Error: {e}. Intente nuevamente.\n")
