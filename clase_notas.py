# clase_nota_alumno.py

class NotaAlumno:
    def __init__(self, nombre, apellidos, estudios, calificacion):
        self.nombre = nombre                # Atributo público
        self.apellidos = apellidos          # Atributo público
        self.estudios = estudios            # Atributo público
        self.__calificacion = calificacion  # Atributo privado

    # Getter para obtener la calificación
    def get_calificacion(self):
        return self.__calificacion

    # Setter para modificar la calificación con validación
    def set_calificacion(self, nueva_calificacion):
        try:
            nueva_calificacion = float(nueva_calificacion)
            if 0 <= nueva_calificacion <= 10:
                self.__calificacion = nueva_calificacion
                print(" Calificación actualizada correctamente.")
            else:
                print(" Error: La calificación debe estar entre 0 y 10.")
        except ValueError:
            print(" Error: Debes ingresar un número válido.")

# Ejemplo de uso
if __name__ == "__main__":
    # Se pide la información al usuario
    nombre = input("Ingrese el nombre: ")
    apellidos = input("Ingrese los apellidos: ")
    estudios = input("Ingrese los estudios: ")

    while True:
        try:
            calificacion = float(input("Ingrese la calificación (0 a 10): "))
            if 0 <= calificacion <= 10:
                break
            else:
                print(" Debe estar entre 0 y 10.")
        except ValueError:
            print(" Ingrese un número válido.")

    alumno = NotaAlumno(nombre, apellidos, estudios, calificacion)

    print("\n--- Datos del Alumno ---")
    print(f"Nombre: {alumno.nombre}")
    print(f"Apellidos: {alumno.apellidos}")
    print(f"Estudios: {alumno.estudios}")
    print(f"Calificación: {alumno.get_calificacion()}")

    # Probar setter
    nueva = input("\nIngrese nueva calificación: ")
    alumno.set_calificacion(nueva)
    print(f"Calificación actual: {alumno.get_calificacion()}")