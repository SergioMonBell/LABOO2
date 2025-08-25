class Persona():
 nombre = 'Dely'
 apellido = 'Lazo'
 genero = 'Femenino'
persona1 = Persona()
print(f"Antes: {persona1.nombre}")
persona1.nombre = 'María'
print(f"Despues: {persona1.nombre}")
print(persona1.genero)
print(f"{persona1.apellido} {persona1.nombre}")