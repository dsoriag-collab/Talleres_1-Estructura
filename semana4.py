# Funciones

# Taller: 4 ejercicios paso a paso.

#_____1) Ejercicio 1 -- Función para calcular el IVA.
# Escribir una función calcular_iva(precio) que reciba
# un precio y retorne el IVA (15%).
# Usarla desde el programa principal.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# precio (input)


#---- Proceso:

# Crear una función llamada calcular_iva().

# La función recibe el precio como parámetro.

# Calcular el 15% del precio.

# Retornar el resultado usando return.

# Desde el programa principal,
# llamar a la función y guardar
# el resultado en la variable iva.


#---- Salida:

# Mostrar el valor del IVA
# con 2 decimales.



#-------- 2. BOSQUEJO A MANO ------------

# precio = 100


# Llamar a la función:

# calcular_iva(100)


# Dentro de la función:

# precio * 0.15

# 100 * 0.15 = 15


# return 15


# Entonces:

# iva = 15


# resultado:

# IVA de $100.0: $15.00



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.
#
# El problema se resuelve de forma secuencial.
#
# Primero se crea una función que recibe
# un precio.
#
# Después se calcula:
#
# precio * 0.15
#
# La función devuelve el resultado
# mediante return.
#
# Finalmente, el programa principal
# llama a la función y muestra el IVA.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def calcular_iva(precio):

    return precio * 0.15


precio = float(input("Precio: $"))

iva = calcular_iva(precio)

print(f"IVA de ${precio}: ${iva:.2f}")



#-------- 5. PRUEBA DE ESCRITORIO --------

# precio = 100


# instrucción                    precio       iva

# input                           100

# calcular_iva(precio)            100

# precio * 0.15                   100          15

# iva = calcular_iva(precio)      100          15


# pantalla:

# IVA de $100.0: $15.00

## Reto: define calcular_total(precio) que retorne precio + IVA usando la función anterior.

def calcular_iva(precio):
    return precio * 0.15

def calcular_total(precio):
    return precio + calcular_iva(precio)

precio = float(input("Precio: $"))
iva = calcular_iva(precio)
total = calcular_total(precio)
print(f"IVA de ${precio}: ${iva:.2f}")
print(f"Total a pagar: ${total:.2f}")

#____2) Ejercicio 2 -- Función es_primo(n)
# Escribir una función que reciba un número
# y retorne True si es primo, False si no.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# num (input)


#---- Proceso:

# Crear una función llamada es_primo(n).

# Si n es menor que 2,
# retornar False porque no es primo.

# Si n es 2 o mayor,
# probar posibles divisores desde 2.

# Si algún número divide exactamente a n,
# retornar False.

# Si después de revisar los posibles divisores
# no encontramos ninguno,
# retornar True.

# En el programa principal,
# usar la función para comprobar
# el número ingresado.

# Después recorrer los números del 2 al 30
# y usar nuevamente es_primo()
# para mostrar solamente los primos.


#---- Salida:

# Mostrar si el número ingresado
# es primo o no.

# Mostrar los números primos
# comprendidos entre 2 y 30.



#-------- 2. BOSQUEJO A MANO ------------

# Supongamos:

# num = 15


# Llamar:

# es_primo(15)


# Como:

# 15 < 2 → falso


# Probar posibles divisores:


# i = 2

# 15 % 2 = 1

# No divide exactamente.


# i = 3

# 15 % 3 = 0

# Encontramos un divisor.


# Entonces:

# return False


# resultado:

# 15 NO es primo


# Luego se recorren los números:

# 2, 3, 4, 5, ..., 30


# Para cada número se llama:

# es_primo(k)


# Si retorna True,
# se muestra ese número.


# resultado:

# 2 3 5 7 11 13 17 19 23 29



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existen procesos repetitivos.
#
# Dentro de es_primo(),
# se prueban posibles divisores de n.
#
# En cada repetición se verifica:
#
# n % i == 0
#
# Si la división es exacta,
# significa que n tiene otro divisor
# y por lo tanto no es primo.
#
# En ese momento se ejecuta:
#
# return False
#
# y la función termina inmediatamente.
#
#
# También existe otro proceso repetitivo
# en el programa principal.
#
# Se recorren los números del 2 al 30:
#
# for k in range(2, 31):
#
# y para cada número se llama
# nuevamente a es_primo(k).
#
# Si devuelve True,
# se muestra en pantalla.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def es_primo(n):

    if n < 2:
        return False

    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            return False

    return True


num = int(input("Número: "))

if es_primo(num):
    print(f"{num} es primo")

else:
    print(f"{num} NO es primo")


print("Primos entre 2 y 30:")

for k in range(2, 31):

    if es_primo(k):
        print(k, end=" ")



#-------- 5. PRUEBA DE ESCRITORIO --------

# Supongamos:

# num = 15


# Dentro de es_primo(15):


# i      15 % i      ¿es 0?      resultado

# 2         1           No        continuar

# 3         0           Sí        return False


# pantalla:

# 15 NO es primo


# Después:

# k      es_primo(k)     ¿mostrar?

# 2         True            Sí

# 3         True            Sí

# 4         False           No

# 5         True            Sí

# 6         False           No

# 7         True            Sí

# ...

# 29        True            Sí

# 30        False           No


# pantalla:

# Primos entre 2 y 30:
# 2 3 5 7 11 13 17 19 23 29

## Reto: Escribe una función contar_primos(a, b) que cuente cuántos primos hay entre a y b.

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def contar_primos(a, b):
    contador = 0
    for k in range(a, b + 1):
        if es_primo(k):
            contador += 1
    return contador

num = int(input("Número: "))
if es_primo(num):
    print(f"{num} es primo")
else:
    print(f"{num} NO es primo")

print("Primos entre 2 y 30:")
for k in range(2, 31):
    if es_primo(k):
        print(k, end=" ")
print() 

a = int(input("Desde: "))
b = int(input("Hasta: "))
print(f"Hay {contar_primos(a, b)} primos entre {a} y {b}")

#_____3) Ejercicio 3 -- Suma de dígitos con función recursiva
# Escribir una función suma_digitos(n) que retorne
# la suma de los dígitos de un número.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# num (input)


#---- Proceso:

# Crear una función llamada suma_digitos(n).

# Convertir el número a positivo usando abs().

# Crear una variable suma que empiece en 0.

# Mientras el número sea mayor que 0:

# Obtener el último dígito usando n % 10.

# Sumar ese dígito a la variable suma.

# Eliminar el último dígito usando n // 10.

# Repetir hasta que n llegue a 0.

# Finalmente retornar la suma.


#---- Salida:

# Mostrar la suma de los dígitos
# del número ingresado.

# También mostrar la suma de los dígitos
# de 123, 4783 y 999.



#-------- 2. BOSQUEJO A MANO ------------

# num = 4783


# n = abs(4783)

# n = 4783

# suma = 0


# Primera repetición:

# último dígito:

# 4783 % 10 = 3

# suma = 0 + 3

# suma = 3

# n = 4783 // 10

# n = 478


# Segunda repetición:

# 478 % 10 = 8

# suma = 3 + 8

# suma = 11

# n = 478 // 10

# n = 47


# Tercera repetición:

# 47 % 10 = 7

# suma = 11 + 7

# suma = 18

# n = 47 // 10

# n = 4


# Cuarta repetición:

# 4 % 10 = 4

# suma = 18 + 4

# suma = 22

# n = 4 // 10

# n = 0


# Como n = 0,
# termina el while.


# resultado:

# Suma: 22



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este código sí existe un proceso repetitivo.
#
# En cada repetición se hacen dos operaciones:
#
# 1. Obtener el último dígito:
#
# n % 10
#
# 2. Eliminar el último dígito:
#
# n = n // 10
#
# El dígito obtenido se acumula:
#
# suma += n % 10
#
# Por ejemplo:
#
# 4783 → 478 → 47 → 4 → 0
#
# Este proceso se repite hasta que
# el número llega a 0.
#
# IMPORTANTE:
#
# Este código usa un ciclo while.
#
# Por lo tanto, técnicamente
# NO es una función recursiva.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def suma_digitos(n):

    n = abs(n)

    suma = 0

    while n > 0:

        suma += n % 10

        n = n // 10

    return suma


num = int(input("Número: "))

print(f"Suma: {suma_digitos(num)}")


for x in [123, 4783, 999]:

    print(f"{x} → {suma_digitos(x)}")



#-------- 5. PRUEBA DE ESCRITORIO --------

# num = 4783


# repetición    n antes    n % 10    suma    n después

# inicio         4783                  0

#     1          4783         3        3        478

#     2           478         8       11         47

#     3            47         7       18          4

#     4             4         4       22          0


# return:

# 22


# Para los valores de la lista:

# 123:

# 1 + 2 + 3 = 6


# 4783:

# 4 + 7 + 8 + 3 = 22


# 999:

# 9 + 9 + 9 = 27


# pantalla:

# Suma: 22
# 123 → 6
# 4783 → 22
# 999 → 27

## Reto: Escribe es_narcisista(n): retorna True si el número es igual a la suma de sus dígitos 
##       elevados al número de dígitos. Ej.: 153 = 1³+5³+3³.

def es_narcisista(n):
    if n < 0:
        return False
    digitos = str(n)          
    potencia = len(digitos)   
    suma = 0
    for d in digitos:
        suma += int(d) ** potencia
    return suma == n

num = int(input("Número: "))
if es_narcisista(num):
    print(f"{num} es narcisista")
else:
    print(f"{num} NO es narcisista")

print("Pruebas:")
for x in [153, 370, 371, 407, 123, 1634]:
    print(f"{x} → {es_narcisista(x)}")

#____4) Ejercicio 4 -- Menú modular con funciones.
# Rediseñar el menú de saludar/despedir del módulo 3,
# pero esta vez con cada opción como función separada.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# opcion (input)

# nombre (input)


#---- Proceso:

# Crear una función saludar().

# Pedir un nombre dentro de la función
# y mostrar un saludo.


# Crear una función despedir().

# Pedir un nombre dentro de la función
# y mostrar una despedida.


# Crear una función mostrar_menu().

# Mostrar las opciones disponibles:
#
# 1. Saludar
# 2. Despedir
# 3. Salir


# Crear un ciclo que muestre el menú
# repetidamente.

# Según la opción ingresada:

# Si es "1", llamar a saludar().

# Si es "2", llamar a despedir().

# Si es "3", mostrar "Adiós"
# y terminar el ciclo.

# Si se ingresa otra opción,
# mostrar "Opción inválida".


#---- Salida:

# Mostrar el menú.

# Mostrar un saludo o una despedida.

# Mostrar un mensaje de salida.

# Mostrar un mensaje si la opción es inválida.



#-------- 2. BOSQUEJO A MANO ------------

# Se muestra:

# --- MENÚ ---
# 1. Saludar
# 2. Despedir
# 3. Salir


# Primer intento:

# opcion = "1"


# Se llama:

# saludar()


# nombre = "Dennis"


# mostrar:

# ¡Hola, Dennis!


# Después el ciclo vuelve
# a mostrar el menú.


# Segundo intento:

# opcion = "2"


# Se llama:

# despedir()


# nombre = "Dennis"


# mostrar:

# ¡Adiós, Dennis!


# El menú vuelve a aparecer.


# Tercer intento:

# opcion = "3"


# mostrar:

# Adiós


# break


# Se termina el programa.



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# El menú debe aparecer varias veces
# hasta que el usuario decida salir.
#
# En cada repetición se hace:
#
# 1. Mostrar el menú.
#
# 2. Pedir una opción.
#
# 3. Ejecutar la función correspondiente.
#
# 4. Volver al menú.
#
# Este proceso se repite con:
#
# while True:
#
# hasta que el usuario elige la opción "3".
#
# En ese momento se utiliza:
#
# break
#
# para terminar el ciclo.
#
#
# Además, cada acción está separada
# en una función:
#
# saludar()
#
# despedir()
#
# mostrar_menu()
#
# Esto hace que el programa sea modular
# y más fácil de organizar.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def saludar():

    nombre = input("Nombre: ")

    print(f"¡Hola, {nombre}!")


def despedir():

    nombre = input("Nombre: ")

    print(f"¡Adiós, {nombre}!")


def mostrar_menu():

    print("\n--- MENÚ ---")

    print("1. Saludar")

    print("2. Despedir")

    print("3. Salir")


while True:

    mostrar_menu()

    opcion = input("Opción: ")

    if opcion == "1":

        saludar()

    elif opcion == "2":

        despedir()

    elif opcion == "3":

        print("Adiós")

        break

    else:

        print("Opción inválida")



#-------- 5. PRUEBA DE ESCRITORIO --------

# Primera repetición:

# opcion = "1"

# función llamada = saludar()

# nombre = Dennis

# salida:

# ¡Hola, Dennis!


# Segunda repetición:

# opcion = "2"

# función llamada = despedir()

# nombre = Dennis

# salida:

# ¡Adiós, Dennis!


# Tercera repetición:

# opcion = "4"

# No coincide con ninguna opción válida.

# salida:

# Opción inválida


# Cuarta repetición:

# opcion = "3"

# salida:

# Adiós

# break


# pantalla:

# --- MENÚ ---
# 1. Saludar
# 2. Despedir
# 3. Salir
# Opción: 1
# Nombre: Dennis
# ¡Hola, Dennis!

# --- MENÚ ---
# 1. Saludar
# 2. Despedir
# 3. Salir
# Opción: 2
# Nombre: Dennis
# ¡Adiós, Dennis!

# --- MENÚ ---
# 1. Saludar
# 2. Despedir
# 3. Salir
# Opción: 4
# Opción inválida

# --- MENÚ ---
# 1. Saludar
# 2. Despedir
# 3. Salir
# Opción: 3
# Adiós

## Reto: Añade una función calcular() que pida dos números y muestre suma, resta, 
##       multiplicación y división. Nueva opción del menú.

# Ejercicios propuestos

#____1) P1 -- Función área de rectángulo.
# Función area_rectangulo(base, altura)
# que retorne el área.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# base

# altura


#---- Proceso:

# Crear una función llamada area_rectangulo().

# La función recibe dos parámetros:

# base

# altura

# Multiplicar la base por la altura.

# Retornar el resultado usando return.


#---- Salida:

# Mostrar el área del rectángulo.



#-------- 2. BOSQUEJO A MANO ------------

# Primera llamada:

# area_rectangulo(5, 5)


# base = 5

# altura = 5


# Calcular área:

# area = 5 * 5

# area = 25


# return 25


# resultado:

# 25


# Segunda llamada:

# area_rectangulo(3, 2)


# base = 3

# altura = 2


# Calcular área:

# area = 3 * 2

# area = 6


# return 6


# resultado:

# 6



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.
#
# El problema se resuelve de forma secuencial.
#
# La función recibe dos valores:
#
# base y altura.
#
# Después realiza la multiplicación:
#
# base * altura
#
# Finalmente devuelve el resultado
# utilizando return.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def area_rectangulo(base, altura):

    return base * altura


print(area_rectangulo(5, 5))

print(area_rectangulo(3, 2))



#-------- 5. PRUEBA DE ESCRITORIO --------

# Primera llamada:


# base    altura    base * altura    retorno

#  5        5            25            25


# Segunda llamada:


# base    altura    base * altura    retorno

#  3        2             6             6


# pantalla:

# 25

# 6

#_____2) P2 -- Función máximo de tres
# Función maximo(a, b, c) que retorne
# el mayor de tres números.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# a

# b

# c


#---- Proceso:

# Crear una función llamada maximo().

# La función recibe tres números.

# Usar max() para comparar los tres valores.

# Retornar el número mayor.


#---- Salida:

# Mostrar el mayor de los tres números.



#-------- 2. BOSQUEJO A MANO ------------

# Llamada:

# maximo(4, 10, 1)


# a = 4

# b = 10

# c = 1


# Comparar:

# max(4, 10, 1)


# El mayor es:

# 10


# return 10


# resultado:

# 10



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.
#
# El problema se resuelve de forma secuencial.
#
# La función recibe tres valores:
#
# a, b y c
#
# Después utiliza:
#
# max(a, b, c)
#
# para encontrar directamente
# el número mayor.
#
# Finalmente devuelve ese valor
# utilizando return.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def maximo(a, b, c):

    return max(a, b, c)


print(maximo(4, 10, 1))



#-------- 5. PRUEBA DE ESCRITORIO --------

# a    b    c    max(a, b, c)    retorno

# 4   10    1         10            10


# pantalla:

# 10         

#____3) P3 -- Función es_bisiesto (año)
# Un año es bisiesto si es divisible entre 4 y no entre 100,
# O si es divisible entre 400.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# anio


#---- Proceso:

# Crear una función llamada es_bisiesto().

# Verificar primero si el año
# es divisible entre 400.

# Si lo es,
# retornar True.

# Si no,
# verificar si es divisible entre 100.

# Si lo es,
# retornar False.

# Después verificar si es divisible entre 4.

# Si lo es,
# retornar True.

# Si no cumple ninguna condición,
# retornar False.


#---- Salida:

# Mostrar True si el año es bisiesto.

# Mostrar False si el año no es bisiesto.



#-------- 2. BOSQUEJO A MANO ------------

# Primer año:

# anio = 2024


# 2024 % 400 = 24

# No es divisible entre 400.


# 2024 % 100 = 24

# No es divisible entre 100.


# 2024 % 4 = 0

# Sí es divisible entre 4.


# return True


# resultado:

# 2024: True



# Segundo año:

# anio = 1900


# 1900 % 400 = 300

# No es divisible entre 400.


# 1900 % 100 = 0

# Sí es divisible entre 100.


# return False


# resultado:

# 1900: False



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo
# en el programa principal.
#
# Se recorren varios años:
#
# 2024, 2023, 2000 y 1900.
#
# Para cada año se repite:
#
# 1. Enviar el año a es_bisiesto().
#
# 2. Comprobar sus divisibilidades.
#
# 3. Mostrar True o False.
#
#
# Dentro de la función no hay un ciclo.
#
# La decisión se realiza mediante condiciones.
#
# La regla general es:
#
# divisible entre 400
#
# O
#
# divisible entre 4
# y no divisible entre 100.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def es_bisiesto(anio):

    if anio % 400 == 0:
        return True

    if anio % 100 == 0:
        return False

    if anio % 4 == 0:
        return True

    return False


def es_bisiesto_corta(anio):

    return anio % 400 == 0 or (anio % 4 == 0 and anio % 100 != 0)


for y in [2024, 2023, 2000, 1900]:

    print(f"{y}: {es_bisiesto(y)}")



#-------- 5. PRUEBA DE ESCRITORIO --------

# año     %400     %100     %4     resultado

# 2024     24       24      0        True

# 2023     23       23      3        False

# 2000      0        0      0        True

# 1900    300        0      0        False


# pantalla:

# 2024: True

# 2023: False

# 2000: True

# 1900: False

#_____4) P4 -- Función factorial y combinatoria.
# Función factorial(n) y luego
# combinatoria(n, k) = n! / (k! · (n-k)!).


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# n

# k


#---- Proceso:

# Crear una función factorial(n).

# Empezar con fact = 1.

# Recorrer los números desde 2 hasta n.

# Multiplicar fact por cada valor de i.

# Retornar el factorial obtenido.


# Crear una función combinatoria(n, k).

# Calcular:

# factorial(n)

# factorial(k)

# factorial(n - k)

# Aplicar la fórmula de combinatoria:

# n! / (k! * (n-k)!)

# Retornar el resultado.


#---- Salida:

# Mostrar el factorial de un número.

# Mostrar el resultado de la combinatoria.



#-------- 2. BOSQUEJO A MANO ------------

# Primera llamada:

# factorial(5)


# fact = 1


# i = 2

# fact = 1 * 2

# fact = 2


# i = 3

# fact = 2 * 3

# fact = 6


# i = 4

# fact = 6 * 4

# fact = 24


# i = 5

# fact = 24 * 5

# fact = 120


# return 120


# resultado:

# 120



# Segunda llamada:

# combinatoria(5, 2)


# Aplicar la fórmula:

# factorial(5) // (factorial(2) * factorial(5 - 2))


# factorial(5) = 120

# factorial(2) = 2

# factorial(3) = 6


# combinatoria:

# 120 // (2 * 6)

# 120 // 12

# 10


# return 10


# resultado:

# 10



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo
# dentro de la función factorial().
#
# Para calcular el factorial,
# se multiplica el resultado acumulado
# por cada número desde 2 hasta n.
#
# El patrón que se repite es:
#
# fact *= i
#
# Por ejemplo:
#
# 1 * 2 * 3 * 4 * 5
#
# Este proceso se realiza con un ciclo for.
#
#
# La función combinatoria() no necesita
# un ciclo propio.
#
# Reutiliza la función factorial()
# varias veces para aplicar la fórmula.



#-------- 4. ESCRIBIR EL CÓDIGO --------

def factorial(n):

    fact = 1

    for i in range(2, n + 1):

        fact *= i

    return fact


def combinatoria(n, k):

    return factorial(n) // (factorial(k) * factorial(n - k))


print(factorial(5))

print(combinatoria(5, 2))



#-------- 5. PRUEBA DE ESCRITORIO --------

# Para factorial(5):


# i        fact antes        fact después

# inicio        1

# 2             1                 2

# 3             2                 6

# 4             6                24

# 5            24               120


# return:

# 120



# Para combinatoria(5, 2):


# factorial(5) = 120

# factorial(2) = 2

# factorial(5 - 2) = factorial(3) = 6


# cálculo:

# 120 // (2 * 6)

# 120 // 12

# 10


# return:

# 10


# pantalla:

# 120

# 10

#_____5) P5 -- Calculadora modular
# Programa que use funciones separadas para cada operación
# (sumar, restar, multiplicar, dividir) y un menú que llame
# a la correcta.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# op (input)

# a (input)

# b (input)


#---- Proceso:

# Crear una función para sumar.

# Crear una función para restar.

# Crear una función para multiplicar.

# Crear una función para dividir.

# En dividir(),
# verificar si b es 0.

# Si b es 0,
# retornar None.

# Si b no es 0,
# realizar la división.

# Mostrar un menú dentro de un ciclo.

# Según la opción ingresada,
# llamar a la función correspondiente.

# Si la opción es 5,
# terminar el ciclo.

# Si la opción no es válida,
# mostrar un mensaje de error.


#---- Salida:

# Mostrar el resultado de la operación.

# Mostrar un mensaje si se intenta
# dividir entre 0.

# Mostrar un mensaje si la opción
# ingresada no es válida.



#-------- 2. BOSQUEJO A MANO ------------

# Primera opción:

# op = "1"


# a = 8

# b = 3


# Se llama:

# sumar(8, 3)


# 8 + 3 = 11


# r = 11


# resultado:

# Resultado: 11



# Segunda opción:

# op = "4"


# a = 10

# b = 0


# Se llama:

# dividir(10, 0)


# Como:

# b == 0


# return None


# Entonces:

# r = None


# mostrar:

# No se puede dividir entre 0


# continue


# El ciclo vuelve al menú.



# Tercera opción:

# op = "5"


# break


# Se termina el programa.



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# El menú se muestra varias veces.
#
# En cada repetición se hace:
#
# 1. Mostrar las opciones.
#
# 2. Leer la opción.
#
# 3. Pedir los números.
#
# 4. Ejecutar la operación elegida.
#
# 5. Mostrar el resultado.
#
# El proceso continúa hasta que
# el usuario elige la opción "5".
#
# Por eso se utiliza:
#
# while True:
#
# y se termina con:
#
# break
#
#
# Cada operación está separada
# en una función diferente:
#
# sumar()
#
# restar()
#
# multiplicar()
#
# dividir()



#-------- 4. ESCRIBIR EL CÓDIGO --------

def sumar(a, b):

    return a + b


def restar(a, b):

    return a - b


def multiplicar(a, b):

    return a * b


def dividir(a, b):

    if b == 0:
        return None

    return a / b


while True:

    print("\n1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir")

    op = input("Opción: ")

    if op == "5":
        break

    a = float(input("a: "))

    b = float(input("b: "))

    if op == "1":

        r = sumar(a, b)

    elif op == "2":

        r = restar(a, b)

    elif op == "3":

        r = multiplicar(a, b)

    elif op == "4":

        r = dividir(a, b)

        if r is None:

            print("No se puede dividir entre 0")

            continue

    else:

        print("Opción inválida")

        continue

    print(f"Resultado: {r}")



#-------- 5. PRUEBA DE ESCRITORIO --------

# Primera repetición:


# op = "1"

# a = 8

# b = 3


# operación:

# sumar(8, 3)


# r = 11


# salida:

# Resultado: 11



# Segunda repetición:


# op = "4"

# a = 10

# b = 0


# operación:

# dividir(10, 0)


# r = None


# como r is None:

# mostrar:

# No se puede dividir entre 0


# continue



# Tercera repetición:


# op = "5"


# break


# termina el ciclo


# pantalla:

# 1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir
# Opción: 1
# a: 8
# b: 3
# Resultado: 11.0

# 1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir
# Opción: 4
# a: 10
# b: 0
# No se puede dividir entre 0

# 1.Sumar 2.Restar 3.Multiplicar 4.Dividir 5.Salir
# Opción: 5