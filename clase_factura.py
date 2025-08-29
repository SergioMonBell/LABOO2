# clase_factura.py

import datetime

class Factura:
    IGV = 0.18  # Impuesto del 18%

    def __init__(self):
        self.numero = None
        self.fecha_emision = None
        self.nombre_cliente = None
        self.producto = None
        self.precio_unitario = None
        self.cantidad = None
        self.precio_bruto = 0
        self.monto_impuesto = 0
        self.precio_neto = 0
        self.estado = True

    def ingresar(self):
        try:
            self.numero = input("Ingrese el número de documento: ").strip()
            if not self.numero:
                raise ValueError("El número de documento no puede estar vacío.")

            fecha_str = input("Ingrese la fecha de emisión (dd/mm/aaaa): ").strip()
            try:
                self.fecha_emision = datetime.datetime.strptime(fecha_str, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("Formato de fecha inválido. Use dd/mm/aaaa.")

            self.nombre_cliente = input("Ingrese el nombre del cliente: ").strip()
            if not self.nombre_cliente:
                raise ValueError("El nombre del cliente no puede estar vacío.")

            self.producto = input("Ingrese el nombre del producto: ").strip()
            if not self.producto:
                raise ValueError("El nombre del producto no puede estar vacío.")

            try:
                self.precio_unitario = float(input("Ingrese el precio unitario: "))
                if self.precio_unitario <= 0:
                    raise ValueError
            except ValueError:
                raise ValueError("El precio unitario debe ser un número positivo.")

            try:
                self.cantidad = int(input("Ingrese la cantidad: "))
                if self.cantidad <= 0:
                    raise ValueError
            except ValueError:
                raise ValueError("La cantidad debe ser un número entero positivo.")

            print("Datos ingresados correctamente.")

        except ValueError as e:
            print(f"Error: {e}")

    def calcular(self):
        if self.precio_unitario is None or self.cantidad is None:
            print("Primero debe ingresar los datos de la factura.")
            return
        self.precio_bruto = self.precio_unitario * self.cantidad
        self.monto_impuesto = self.precio_bruto * Factura.IGV
        self.precio_neto = self.precio_bruto + self.monto_impuesto
        print("Cálculos realizados correctamente.")

    def anular(self):
        self.estado = False
        print("Factura anulada correctamente.")

    def imprimir(self):
        if self.numero is None:
            print("No hay datos de factura para mostrar.")
            return
        print("\n===== FACTURA =====")
        print(f"Número: {self.numero}")
        print(f"Fecha de emisión: {self.fecha_emision.strftime('%d/%m/%Y')}")
        print(f"Cliente: {self.nombre_cliente}")
        print(f"Producto: {self.producto}")
        print(f"Precio Unitario: {self.precio_unitario:.2f}")
        print(f"Cantidad: {self.cantidad}")
        print(f"Precio Bruto: {self.precio_bruto:.2f}")
        print(f"Monto IGV (18%): {self.monto_impuesto:.2f}")
        print(f"Precio Neto: {self.precio_neto:.2f}")
        print(f"Estado: {'Activo' if self.estado else 'Anulado'}")
        print("===================\n")


def menu():
    factura = Factura()

    while True:
        print("=== MENÚ FACTURA ===")
        print("1. Ingresar")
        print("2. Calcular")
        print("3. Anular")
        print("4. Imprimir")
        print("5. Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            factura.ingresar()
        elif opcion == "2":
            factura.calcular()
        elif opcion == "3":
            factura.anular()
        elif opcion == "4":
            factura.imprimir()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
