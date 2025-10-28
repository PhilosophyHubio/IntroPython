nombre = "Ana"
edad = 30
altura = 1.75
es_estudiante = True

print(f"Nombre: {nombre}, Tipo: {type(nombre)}")
print(f"Edad: {edad}, Tipo: {type(edad)}")
print(f"Altura: {altura}, Tipo: {type(altura)}")
print(f"Es estudiante: {es_estudiante}, Tipo: {type(es_estudiante)}")

# Conversión de float a int
precio_flotante = 19.99
precio_entero = int(precio_flotante)
print(f"\nDe float a int: {precio_entero}, Tipo: {type(precio_entero)}") # Resultado: 19

#Conversión de int a str
año = 2025
año_texto = str(año)
print(f"De int a str: '{año_texto}', Tipo: {type(año_texto)}")

#Conversión de str a float
cadena_numero = "123.45"
numero_float = float(cadena_numero)
print(f"De str a float: {numero_float}, Tipo: {type(numero_float)}")
