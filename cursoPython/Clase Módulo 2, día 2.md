# **Condicionales y Ciclos en Python**

**Objetivo:**
Que el alumno sea capaz de tomar decisiones y repetir instrucciones controlando el flujo de ejecución de sus programas.
Al finalizar la clase, comprenderá cómo usar estructuras condicionales y bucles para resolver problemas comunes en programación.

---

## **Bloque 1: Operadores Relacionales y Lógicos (30 minutos)**

**0:00 – 0:10 | Introducción a los operadores relacionales**

Los **operadores relacionales** comparan dos valores y devuelven un resultado booleano:
`True` (verdadero) o `False` (falso).

| Operador | Significado       | Ejemplo  | Resultado |
| -------- | ----------------- | -------- | --------- |
| `==`     | Igual a           | `5 == 5` | `True`    |
| `!=`     | Diferente de      | `5 != 3` | `True`    |
| `>`      | Mayor que         | `8 > 6`  | `True`    |
| `<`      | Menor que         | `2 < 1`  | `False`   |
| `>=`     | Mayor o igual que | `5 >= 5` | `True`    |
| `<=`     | Menor o igual que | `4 <= 6` | `True`    |

**💻 Ejemplo práctico:**

```python
a = 10
b = 5

print("¿a es mayor que b?", a > b)
print("¿a es igual a b?", a == b)
print("¿a es diferente de b?", a != b)
```

---

**0:10 – 0:30 | Operadores lógicos**

Permiten combinar varias condiciones en una sola instrucción.
Los principales son:

| Operador | Descripción                               | Ejemplo               | Resultado |
| -------- | ----------------------------------------- | --------------------- | --------- |
| `and`    | Verdadero si ambas condiciones lo son     | `(5 > 2) and (3 < 4)` | `True`    |
| `or`     | Verdadero si al menos una condición lo es | `(5 < 2) or (3 < 4)`  | `True`    |
| `not`    | Invierte el valor lógico                  | `not(5 > 2)`          | `False`   |

**💻 Ejercicio 2:**

```python
x = 7
print((x > 5) and (x < 10))
print((x < 5) or (x == 7))
print(not(x == 7))
```

---

## **Bloque 2: Sentencias Condicionales (30 minutos)**

**0:30 – 0:45 | Estructura básica: if, elif, else**

Las sentencias condicionales permiten que el programa tome decisiones.

**💻 Ejercicio 3:**

```python
calificacion = int(input("Ingresa tu calificación: "))

if calificacion >= 90:
    print("Excelente 😃")
elif calificacion >= 70:
    print("Aprobado 👍")
else:
    print("Reprobado 😢")
```

---

**0:45 – 1:00 | Ejercicio práctico**

El usuario ingresa su edad y el programa determina si puede entrar a una fiesta.

**💻 Código:**

```python
edad = int(input("Ingresa tu edad: "))

if edad < 18:
    print("No puedes entrar")
elif edad <= 40:
    print("Bienvenido")
else:
    print("Solo con invitación especial")
```

---

## **Bloque 3: Ciclos for y while (30 minutos)**

**1:00 – 1:15 | Ciclo for**

Se usa cuando se conoce la cantidad de repeticiones.

**💻 Ejemplo:**

```python
for i in range(5):
    print("Iteración número:", i)
```

---

**1:15 – 1:25 | Ciclo while**

Se usa cuando no se sabe cuántas veces se repetirá el bloque.

**💻 Ejemplo:**

```python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

---

**1:25 – 1:35 | Uso de range()**

La función `range(inicio, fin, paso)` genera una secuencia de números.

**💻 Ejercicio 4:**

```python
for i in range(2, 11, 2):
    print(i)
```

---

## **Bloque 4: Control del flujo en ciclos (20 minutos)**

**1:35 – 1:45 | break**

Interrumpe un ciclo antes de que termine.

**💻 Ejercicio 5:**

```python
for i in range(10):
    if i == 5:
        break
    print(i)
print("Ciclo detenido en i =", i)
```

---

**1:45 – 1:55 | continue**

Salta la iteración actual y continúa con la siguiente.

**💻 Ejercicio 6:**

```python
for i in range(10):
    if i == 5:
        continue
    print(i)
```

---

## **Bloque 5: Ejercicio Integrador (15 minutos)**

**1:55 – 2:10 | Validación de contraseña**

El usuario tiene tres intentos para ingresar la contraseña correcta.

**💻 Código:**

```python
contraseña = "python123"
intentos = 3

while intentos > 0:
    ingreso = input("Introduce la contraseña: ")
    if ingreso == contraseña:
        print("✅ Acceso concedido")
        break
    else:
        intentos -= 1
        print(f"❌ Contraseña incorrecta. Intentos restantes: {intentos}")

if intentos == 0:
    print("🔒 Acceso bloqueado")
```

---

## **TAREA MÓDULO 2: Programa de Cajero Automático**

Desarrolla un programa que simule un cajero automático simple.

**Requisitos:**

1. Pedir un **PIN de 4 dígitos** con **3 intentos**.
2. Mostrar un **menú** con las opciones:

   * Consultar saldo
   * Depositar dinero
   * Retirar dinero
   * Salir

**💻 Código sugerido:**

```python
pin_correcto = "1234"
intentos = 3
saldo = 1000

while intentos > 0:
    pin = input("Introduce tu PIN de 4 dígitos: ")
    if pin == pin_correcto:
        print("\n✅ Acceso concedido\n")
        while True:
            print("Menú principal:")
            print("1. Consultar saldo")
            print("2. Depositar dinero")
            print("3. Retirar dinero")
            print("4. Salir")

            opcion = input("Elige una opción: ")

            if opcion == "1":
                print(f"Tu saldo actual es: ${saldo}\n")

            elif opcion == "2":
                deposito = float(input("Cantidad a depositar: $"))
                saldo += deposito
                print(f"Depósito exitoso. Saldo actual: ${saldo}\n")

            elif opcion == "3":
                retiro = float(input("Cantidad a retirar: $"))
                if retiro > saldo:
                    print("❌ Fondos insuficientes.\n")
                else:
                    saldo -= retiro
                    print(f"Retiro exitoso. Saldo actual: ${saldo}\n")

            elif opcion == "4":
                print("👋 Gracias por usar el cajero.")
                break
            else:
                print("⚠️ Opción inválida, intenta nuevamente.\n")
        break
    else:
        intentos -= 1
        print(f"❌ PIN incorrecto. Intentos restantes: {intentos}\n")

if intentos == 0:
    print("🔒 Cuenta bloqueada")
```



