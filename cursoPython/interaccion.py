nombre_usuario = input("Por favor, ingresa tu nombre: ")
print(f"¿Bienvenido/a a la clase de Python, {nombre_usuario}!")

#La edad que se introduce es inicialmente unstr, por eso se usa int()
edad_str = input("Ahora, ingresa tu edad: ")
edad_num = int(edad_str) 

edad_futura = edad_num + 5
print(f"En 5 años tendrás {edad_futura} años.")
