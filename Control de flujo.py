# Control de flujo

## Taller: 6 ejercicios paso a paso

#_______1) Ejercicio 1 -- Contar del 1 al N
# Leer un número N y mostrar los números del 1 al N.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# n (input)

#---- Proceso:
# Crear un ciclo que empiece en 1.
# Repetir el ciclo hasta llegar al número N.
# Mostrar el valor de i en cada repetición.

#---- Salida:
# Mostrar todos los números desde 1 hasta N.

#-------- 2. BOSQUEJO A MANO ------------
# n = 5

# El ciclo empieza en 1:
# i = 1
# mostrar 1

# siguiente valor:
# i = 2
# mostrar 2

# siguiente valor:
# i = 3
# mostrar 3

# siguiente valor:
# i = 4
# mostrar 4

# siguiente valor:
# i = 5
# mostrar 5

# resultado:
# 1
# 2
# 3
# 4
# 5

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Se debe mostrar un número y después avanzar
# al siguiente número.
# Este proceso se repite desde 1 hasta N.
# Por eso se utiliza un ciclo for.
# range(1, n + 1) empieza en 1
# y termina en N.
# Se usa n + 1 porque el último valor de range()
# no se incluye.

#-------- 4. ESCRIBIR EL CÓDIGO --------
n = int(input("N: "))

for i in range(1, n + 1):
    print(i)

#-------- 5. PRUEBA DE ESCRITORIO --------
# n = 5

# repetición        i        salida

#     1             1           1
#     2             2           2
#     3             3           3
#     4             4           4
#     5             5           5

# pantalla:
# 1
# 2
# 3
# 4
# 5

## Reto: Cámbialo para que muestre del N al 1 (hacia atrás). Pista: range(n, 0, -1).

n = int(input("N: "))

for i in range(n, 0, -1):
    print(i)

#_____2) Ejercicio 2 -- Suma de los primeros N naturales
# Leer N y calcular la suma de 1 + 2 + 3 + ... + N.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# cantidad_num_naturales (input)

#---- Proceso:
# Crear una variable suma con valor inicial de 0.
# Recorrer los números naturales desde 1 hasta N.
# En cada repetición, agregar el valor de i
# a la variable suma.
# Continuar hasta llegar al número N.

#---- Salida:
# Mostrar la suma total de los primeros N números naturales.

#-------- 2. BOSQUEJO A MANO ------------
# cantidad_num_naturales = 5
# suma = 0

# Primera repetición:
# i = 1
# suma = 0 + 1
# suma = 1

# Segunda repetición:
# i = 2
# suma = 1 + 2
# suma = 3

# Tercera repetición:
# i = 3
# suma = 3 + 3
# suma = 6

# Cuarta repetición:
# i = 4
# suma = 6 + 4
# suma = 10

# Quinta repetición:

# i = 5
# suma = 10 + 5
# suma = 15

# resultado:
# Suma: 15

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# En cada repetición se toma el valor de i
# y se suma al resultado acumulado.
# El proceso que se repite es:
# suma = suma + i
# Después, i avanza al siguiente número.
# Este patrón continúa desde 1 hasta N,
# por eso se utiliza un ciclo for.

#-------- 4. ESCRIBIR EL CÓDIGO --------
cantidad_num_naturales = int(input("Ingrese la cantidad de números naturales a sumar: "))

suma = 0

for i in range(1, cantidad_num_naturales + 1):
    suma = suma + i

print(f"Suma: {suma}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# cantidad_num_naturales = 5

# repetición        i        suma

# inicio                      0
#     1             1         1
#     2             2         3
#     3             3         6
#     4             4        10
#     5             5        15

# pantalla:
# Suma: 15

## Reto: Adaptarlo para calcular la suma de los pares del 2 al 100. Pista: range(2, 101, 2).

suma_pares = 0

for i in range (2, 101, 2):
    suma_pares = suma_pares + i

print(f"La suma de los pares del 2 al 100 es: {suma_pares}")

#____3) Ejercicio 3 -- Factorial de N
# Leer N y calcular el factorial
# (N! = 1 × 2 × 3 × ... × N).
# Ejemplo: 5! = 120.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# factorial_n (input)

#---- Proceso:
# Crear una variable factorial con valor inicial de 1.
# Recorrer los números desde 1 hasta N.
# En cada repetición, multiplicar factorial
# por el valor actual de i.
# Guardar el resultado acumulado
# en la variable factorial.

#---- Salida:
# Mostrar el factorial del número ingresado.

#-------- 2. BOSQUEJO A MANO ------------
# factorial_n = 5
# factorial = 1

# Primera repetición:
# i = 1
# factorial = 1 * 1
# factorial = 1

# Segunda repetición:
# i = 2
# factorial = 1 * 2
# factorial = 2

# Tercera repetición:
# i = 3
# factorial = 2 * 3
# factorial = 6

# Cuarta repetición:
# i = 4
# factorial = 6 * 4
# factorial = 24

# Quinta repetición:
# i = 5
# factorial = 24 * 5
# factorial = 120

# resultado:
# Factorial de 5: 120

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# En cada repetición se toma el valor de i
# y se multiplica por el resultado acumulado.
# El proceso que se repite es:
# factorial = factorial * i
# Después, i avanza al siguiente número.
# Este patrón continúa desde 1 hasta N,
# por eso se utiliza un ciclo for.


#-------- 4. ESCRIBIR EL CÓDIGO --------
factorial_n = int(input("Ingrese un número para calcular su factorial: "))

factorial = 1

for i in range(1, factorial_n + 1):
    factorial = factorial * i

print(f"Factorial de {factorial_n}: {factorial}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# factorial_n = 5

# repetición        i        factorial
# inicio                      1
#     1             1         1
#     2             2         2
#     3             3         6
#     4             4        24
#     5             5       120

# pantalla:
# Factorial de 5: 120

## Reto: ¿Qué pasa con N muy grande (100!)? Python maneja enteros infinitos, 
#        pruébalo. En JS con enteros normales explotaría.

factorial_n100 = 100
factorialreto = 1

for i in range (1, factorial_n100+1):
    factorialreto = factorialreto * i

print(f"Factorial de 100: {factorialreto}") ##El resultado es inmenso lmao.

#_____4) Ejercicio 4 -- Cuántos aprobaron
# Leer las notas de N estudiantes (una por una)
# y contar cuántos aprobaron (nota ≥ 70).

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:

# n (input)

# nota (input)

#---- Proceso:
# Crear una variable aprobados que empiece en 0.
# Repetir el ingreso de notas N veces.
# En cada repetición, leer la nota de un estudiante.
# Si la nota es mayor o igual a 70,
# aumentar el contador de aprobados en 1.

#---- Salida:
# Mostrar cuántos estudiantes aprobaron
# de la cantidad total de estudiantes.

#-------- 2. BOSQUEJO A MANO ------------
# n = 4
# aprobados = 0

# Primer estudiante:
# nota = 80
# 80 >= 70
# aprobados = 0 + 1
# aprobados = 1

# Segundo estudiante:
# nota = 65
# 65 >= 70 → falso
# aprobados = 1

# Tercer estudiante:
# nota = 90
# 90 >= 70
# aprobados = 1 + 1
# aprobados = 2

# Cuarto estudiante:
# nota = 70
# 70 >= 70
# aprobados = 2 + 1
# aprobados = 3

# resultado:
# Aprobados: 3 de 4

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Para cada estudiante se repite el mismo proceso:
# 1. Pedir una nota.
# 2. Comparar si la nota es mayor o igual a 70.
# 3. Si aprobó, aumentar el contador en 1.
# El proceso se repite N veces,
# por eso se utiliza un ciclo for.
# El patrón principal es:
# if nota >= 70:
#     aprobados += 1

#-------- 4. ESCRIBIR EL CÓDIGO --------
n = int(input("¿Cuántos estudiantes? "))

aprobados = 0

for i in range(n):
    nota = float(input(f"Nota {i + 1}: "))

    if nota >= 70:
        aprobados += 1

print(f"Aprobados: {aprobados} de {n}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# n = 4

# repetición    nota    nota >= 70    aprobados
# inicio                                  0
#     1         80          Sí            1
#     2         65          No            1
#     3         90          Sí            2
#     4         70          Sí            3

# pantalla:
# Aprobados: 3 de 4

## Reto: Añade un contador para reprobados y muestra el porcentaje de aprobación.

n = int(input("¿Cuántos estudiantes? "))
aprobadosreto = 0
reprobadosreto = 0                      

for i in range(n):
    notareto = float(input(f"Nota {i+1}: "))
    if notareto >= 7:                   
        aprobadosreto += 1
    else:
        reprobadosreto += 1

porcentaje = aprobadosreto / n * 100         

print(f"-- Notas --\n"
      f"Aprobados: {aprobadosreto}\n"
      f"Reprobados: {reprobadosreto}\n"
      f"Porcentaje de aprobados: {porcentaje}%")

#_____5) Ejercicio 5 -- La nota más alta (patrón campeón)
# Leer las notas de N estudiantes
# y mostrar la nota más alta.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# n (input)
# nota (input)

#---- Proceso:
# Crear una variable maxima con un valor inicial
# muy pequeño.
# Leer las notas de los estudiantes una por una.
# Comparar cada nota con la nota máxima guardada.
# Si la nueva nota es mayor que maxima,
# actualizar maxima con esa nota.
# Repetir el proceso N veces.

#---- Salida:
# Mostrar la nota más alta encontrada.

#-------- 2. BOSQUEJO A MANO ------------
# n = 4

# maxima = -infinito

# Primera nota:
# nota = 75
# 75 > maxima
# maxima = 75

# Segunda nota:
# nota = 82
# 82 > 75
# maxima = 82

# Tercera nota:
# nota = 68
# 68 > 82 → falso
# maxima = 82

# Cuarta nota:
# nota = 90
# 90 > 82
# maxima = 90

# resultado:
# Máxima: 90

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Para cada nota se repite el mismo proceso:
# 1. Leer una nota.
# 2. Compararla con la nota máxima actual.
# 3. Si la nueva nota es mayor,
#    reemplazar la máxima.
# El patrón principal es:
# if nota > maxima:
#     maxima = nota
# Este patrón se conoce como "patrón campeón",
# porque siempre se conserva el valor más alto
# encontrado hasta el momento.

#-------- 4. ESCRIBIR EL CÓDIGO --------
n = int(input("¿Cuántas notas? "))

maxima = float("-inf")

for i in range(n):
    nota = float(input(f"Nota {i + 1}: "))

    if nota > maxima:
        maxima = nota

print(f"Máxima: {maxima}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# n = 4

# repetición    nota    nota > maxima    maxima

# inicio                               -infinito
#     1         75          Sí            75
#     2         82          Sí            82
#     3         68          No            82
#     4         90          Sí            90


# pantalla:
# Máxima: 90

## Reto: Adaptarlo para encontrar la menor nota. Cambio: float("inf") y if nota < minima:.

numreto = int(input("¿Cuántas notas? "))
minimareto = float("inf")              # valor imposible: nada será menor

for i in range(numreto):
    notareto = float(input(f"Nota {i+1}: "))
    if notareto < minimareto:               # ¿es mayor que el récord?
        minimareto = notareto               # sí → actualizamos

print(f"Mínima: {minimareto}")

#____6) Ejercicio 6 -- ¿Es primo?
# Leer un número y determinar si es primo
# (solo divisible entre 1 y él mismo).

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# n (input)

#---- Proceso:
# Crear una variable es_primo con valor True.
# Si n es menor que 2,
# indicar que no es primo.
# Si n es 2 o mayor,
# probar posibles divisores desde 2.
# Revisar si alguno divide exactamente al número.
# Si encontramos un divisor,
# cambiar es_primo a False
# y detener el ciclo con break.

#---- Salida:
# Mostrar si el número es primo.
# O mostrar que el número NO es primo.

#-------- 2. BOSQUEJO A MANO ------------
# n = 15
# es_primo = True

# Como:
# 15 >= 2
# entramos al ciclo.

# Probar divisor:
# i = 2
# 15 % 2 = 1
# No divide exactamente.
# es_primo sigue siendo True.

# Siguiente divisor:
# i = 3
# 15 % 3 = 0
# Encontramos un divisor exacto.

# Entonces:
# es_primo = False
# break

# Se detiene el ciclo.

# resultado:
# 15 NO es primo

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Se prueban varios números como posibles
# divisores de n.
# En cada repetición se realiza:
# n % i
# Si el residuo es 0:
# n % i == 0
# significa que encontramos un divisor.
# Entonces:
# es_primo = False
# y usamos break para detener el ciclo,
# porque ya sabemos que el número no es primo.
# La variable es_primo funciona como una BANDERA.
# Empieza en True porque inicialmente
# asumimos que el número sí es primo.
# Si encontramos un divisor,
# la bandera cambia a False.
# Solo se buscan divisores hasta la raíz
# cuadrada de n porque no es necesario
# comprobar todos los números hasta n.

#-------- 4. ESCRIBIR EL CÓDIGO --------
n = int(input("Número: "))

es_primo = True

if n < 2:
    es_primo = False

else:
    for i in range(2, int(n ** 0.5) + 1):

        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"{n} es primo")

else:
    print(f"{n} NO es primo")

#-------- 5. PRUEBA DE ESCRITORIO --------
# n = 15

# paso       i       n % i       es_primo
# inicio                            True
# n < 2                            False
#   1        2         1            True
#   2        3         0            False

# break → termina el ciclo

# pantalla:
# 15 NO es primo

## Reto: Genera una lista de todos los primos entre 2 y 100.

print(f"Números primos entre 2 y 100:")
for n in range (2, 101):
    es_primo = True
    for i in range (2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        print(n)

# Ejercicios propuestos

#____1) P1 -- Tabla de multiplicar
# Lee un número N y muestra su tabla de multiplicar
# del 1 al 12.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# numerotabla (input)

#---- Proceso:
# Recorrer los números desde 1 hasta 12.
# En cada repetición, multiplicar numerotabla
# por el valor actual de i.
# Mostrar la multiplicación y su resultado.

#---- Salida:
# Mostrar la tabla de multiplicar del número ingresado
# desde 1 hasta 12.

#-------- 2. BOSQUEJO A MANO ------------
# numerotabla = 5

# Primera repetición:
# i = 1
# 5 * 1 = 5

# mostrar:
# 5 x 1 = 5

# Segunda repetición:
# i = 2
# 5 * 2 = 10

# mostrar:
# 5 x 2 = 10

# Tercera repetición:
# i = 3
# 5 * 3 = 15

# mostrar:
# 5 x 3 = 15

# El mismo proceso continúa
# hasta llegar a i = 12.

# Última repetición:
# i = 12
# 5 * 12 = 60

# mostrar:
# 5 x 12 = 60

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# En cada repetición se toma el mismo número
# y se multiplica por un valor diferente de i.
# El patrón que se repite es:
# numerotabla * i
# El valor de i aumenta desde 1 hasta 12.
# Por eso se utiliza un ciclo for
# con range(1, 13).
# Se usa 13 porque el último valor de range()
# no se incluye.

#-------- 4. ESCRIBIR EL CÓDIGO --------
numerotabla = int(input("Ingrese un número: "))

for i in range(1, 13):
    print(f"{numerotabla} x {i} = {numerotabla * i}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# numerotabla = 5

# repetición        i        numerotabla * i        salida
#     1             1               5               5 x 1 = 5
#     2             2              10               5 x 2 = 10
#     3             3              15               5 x 3 = 15
#     4             4              20               5 x 4 = 20
#     5             5              25               5 x 5 = 25
#     6             6              30               5 x 6 = 30
#     7             7              35               5 x 7 = 35
#     8             8              40               5 x 8 = 40
#     9             9              45               5 x 9 = 45
#    10            10              50               5 x 10 = 50
#    11            11              55               5 x 11 = 55
#    12            12              60               5 x 12 = 60

# pantalla:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# 5 x 4 = 20
# 5 x 5 = 25
# 5 x 6 = 30
# 5 x 7 = 35
# 5 x 8 = 40
# 5 x 9 = 45
# 5 x 10 = 50
# 5 x 11 = 55
# 5 x 12 = 60

#_____2) P2 -- Contar dígitos de un número
# Lee un número y cuenta cuántos dígitos tiene
# sin convertirlo a string.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# num (input)

#---- Proceso:
# Convertir el número a positivo usando abs()
# para que funcione también con números negativos.
# Crear una variable digitos que empiece en 0.
# Si el número es 0,
# indicar que tiene 1 dígito.
# Si el número es distinto de 0,
# dividirlo entre 10 repetidamente.
# Cada vez que se divide entre 10,
# aumentar el contador de dígitos en 1.
# Repetir hasta que el número llegue a 0.

#---- Salida:
# Mostrar cuántos dígitos tiene el número.

#-------- 2. BOSQUEJO A MANO ------------
# num = 4827
# n = abs(4827)
# n = 4827
# digitos = 0

# Primera repetición:
# digitos = 0 + 1
# digitos = 1
# n = 4827 // 10
# n = 482

# Segunda repetición:
# digitos = 1 + 1
# digitos = 2
# n = 482 // 10
# n = 48

# Tercera repetición:
# digitos = 2 + 1
# digitos = 3
# n = 48 // 10
# n = 4

# Cuarta repetición:
# digitos = 3 + 1
# digitos = 4
# n = 4 // 10
# n = 0

# Como n ya es 0,
# termina el ciclo.

# resultado:
# 4 dígitos

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# En cada repetición se hacen dos cosas:
# 1. Aumentar el contador de dígitos.
# digitos += 1
# 2. Eliminar el último dígito del número
#    usando división entera entre 10.
# n = n // 10
# Por ejemplo:
# 4827 → 482 → 48 → 4 → 0
# Este proceso se repite mientras n sea mayor que 0,
# por eso se utiliza un ciclo while.

#-------- 4. ESCRIBIR EL CÓDIGO --------
num = int(input("Número: "))

n = abs(num)

digitos = 0

if n == 0:
    digitos = 1

else:
    while n > 0:
        digitos += 1
        n = n // 10

print(f"{digitos} dígitos")

#-------- 5. PRUEBA DE ESCRITORIO --------
# num = 4827
# n = 4827
# digitos = 0

# repetición        n antes        digitos        n después
#     1               4827             1              482
#     2                482             2               48
#     3                 48             3                4
#     4                  4             4                0


# Cuando n = 0, termina el while.

# pantalla:
# 4 dígitos

#_____3) Suma de pares e impares
# Lee N números y muestra la suma de los pares
# y la suma de los impares por separado.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# n (input)
# x (input)

#---- Proceso:
# Crear una variable suma_pares que empiece en 0.
# Crear una variable suma_impares que empiece en 0.
# Leer N números uno por uno.
# Verificar si cada número es par o impar.

# Si el número es par,
# sumarlo en suma_pares.

# Si el número es impar,
# sumarlo en suma_impares.

#---- Salida:
# Mostrar la suma de los números pares.
# Mostrar la suma de los números impares.

#-------- 2. BOSQUEJO A MANO ------------
# n = 5
# suma_pares = 0
# suma_impares = 0

# Primer número:
# x = 4
# 4 % 2 = 0
# Es par.

# suma_pares = 0 + 4
# suma_pares = 4

# Segundo número:
# x = 7
# 7 % 2 = 1
# Es impar.

# suma_impares = 0 + 7
# suma_impares = 7

# Tercer número:
# x = 2
# 2 % 2 = 0
# Es par.

# suma_pares = 4 + 2
# suma_pares = 6

# Cuarto número:
# x = 9
# 9 % 2 = 1
# Es impar.
# suma_impares = 7 + 9
# suma_impares = 16

# Quinto número:
# x = 6
# 6 % 2 = 0
# Es par.

# suma_pares = 6 + 6
# suma_pares = 12

# resultado:
# Suma pares: 12
# Suma impares: 16

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Para cada número se repite el mismo proceso:
# 1. Leer un número.
# 2. Verificar si es par o impar usando:
# x % 2
# 3. Si el residuo es 0,
#    sumar el número en suma_pares.
# 4. Si el residuo no es 0,
#    sumar el número en suma_impares.
# Este proceso se repite N veces,
# por eso se utiliza un ciclo for.

#-------- 4. ESCRIBIR EL CÓDIGO --------
n = int(input("¿Cuántos números? "))

suma_pares = 0
suma_impares = 0

for i in range(n):

    x = int(input(f"Número {i + 1}: "))

    if x % 2 == 0:
        suma_pares += x

    else:
        suma_impares += x

print(f"Suma pares: {suma_pares}")
print(f"Suma impares: {suma_impares}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# n = 5

# repetición    x    x % 2    suma_pares    suma_impares
# inicio                            0              0
#     1         4       0           4              0
#     2         7       1           4              7
#     3         2       0           6              7
#     4         9       1           6             16
#     5         6       0          12             16


# pantalla:
# Suma pares: 12
# Suma impares: 16

#______4) P4 -- Validar entrada (bucle con centinela)
# Pide una edad y valida que esté entre 0 y 120.
# Si el usuario ingresa algo inválido, vuelve a pedirla.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# edad (input)

#---- Proceso:
# Pedir una edad dentro de un ciclo.
# Verificar si la edad está entre 0 y 120.
# Si la edad es válida,
# salir del ciclo usando break.
# Si la edad no es válida,
# mostrar un mensaje de error
# y volver a pedirla.

#---- Salida:
# Mostrar la edad válida ingresada.

#-------- 2. BOSQUEJO A MANO ------------
# Primer intento:
# edad = 150

# Verificar:
# 0 <= 150 <= 120

# Falso

# Entonces:

# mostrar:
# Inválida, intenta de nuevo

# Segundo intento:
# edad = -5

# Verificar:
# 0 <= -5 <= 120

# Falso

# Entonces:

# mostrar:
# Inválida, intenta de nuevo

# Tercer intento:
# edad = 25

# Verificar:
# 0 <= 25 <= 120

# Verdadero

# Entonces:
# break

# Se sale del ciclo.

# resultado:
# Edad válida: 25

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# El proceso que se repite es:
# 1. Pedir una edad.
# 2. Verificar si está entre 0 y 120.
# 3. Si es inválida,
#    volver a pedirla.
# Este proceso continúa hasta que
# el usuario ingresa una edad válida.
# Por eso se utiliza:
# while True:
# El ciclo se mantiene activo indefinidamente
# hasta que se cumple la condición:
# 0 <= edad <= 120
# Cuando se cumple, se utiliza break
# para salir del ciclo.

#-------- 4. ESCRIBIR EL CÓDIGO --------
while True:

    edad = int(input("Edad (0-120): "))

    if 0 <= edad <= 120:
        break

    print("Inválida, intenta de nuevo")

print(f"Edad válida: {edad}")


#-------- 5. PRUEBA DE ESCRITORIO --------
# intento    edad    0 <= edad <= 120    acción
#    1       150          Falso          mostrar error
#    2       -5           Falso          mostrar error
#    3        25          Verdadero      break

# pantalla:
# Edad (0-120): 150
# Inválida, intenta de nuevo
# Edad (0-120): -5
# Inválida, intenta de nuevo
# Edad (0-120): 25
# Edad válida: 25

#_______5) P5 -- Adivina el número
# Genera un número secreto entre 1 y 100.
# El usuario intenta adivinar.
# En cada intento le dices si es «mayor» o «menor».
# Cuenta cuántos intentos usó.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# intento (input)

#---- Proceso:
# Generar un número secreto aleatorio
# entre 1 y 100.
# Crear una variable intentos que empiece en 0.
# Pedir al usuario un número.
# Aumentar el contador de intentos en 1.
# Comparar el número ingresado
# con el número secreto.
# Si son iguales,
# mostrar que acertó y terminar el ciclo.
# Si el intento es menor que el secreto,
# indicar que el número secreto es mayor.
# Si el intento es mayor que el secreto,
# indicar que el número secreto es menor.

#---- Salida:
# Mostrar pistas indicando si el número
# secreto es mayor o menor.
# Mostrar cuántos intentos necesitó
# cuando adivine correctamente.

#-------- 2. BOSQUEJO A MANO ------------
# Supongamos que:

# secreto = 60

# intentos = 0

# Primer intento:
# intento = 40
# intentos = 0 + 1
# intentos = 1

# 40 == 60 → falso

# 40 < 60 → verdadero

# mostrar:
# Es mayor


# Segundo intento:
# intento = 75
# intentos = 1 + 1
# intentos = 2

# 75 == 60 → falso

# 75 < 60 → falso

# Entonces:

# mostrar:
# Es menor


# Tercer intento:
# intento = 60
# intentos = 2 + 1
# intentos = 3

# 60 == 60 → verdadero

# mostrar:
# ¡Correcto en 3 intentos!

# break

# Se termina el ciclo.

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# En cada repetición se hacen los mismos pasos:
# 1. Pedir un número al usuario.
# 2. Aumentar el contador de intentos.
# 3. Comparar el intento con el número secreto.
# Si el intento es incorrecto,
# se proporciona una pista y se vuelve a intentar.
# El proceso continúa hasta que:
# intento == secreto
# Cuando esto ocurre,
# se utiliza break para terminar el ciclo.
# También se utiliza un contador:
# intentos += 1
# para saber cuántas veces intentó
# adivinar el usuario.

#-------- 4. ESCRIBIR EL CÓDIGO --------
import random

secreto = random.randint(1, 100)

intentos = 0

while True:

    intento = int(input("Adivina (1-100): "))

    intentos += 1

    if intento == secreto:
        print(f"¡Correcto en {intentos} intentos!")
        break

    elif intento < secreto:
        print("Es mayor")

    else:
        print("Es menor")

#-------- 5. PRUEBA DE ESCRITORIO --------
# Supongamos:
# secreto = 60

# intento    intentos    comparación        salida
#   40          1        40 < 60            Es mayor
#   75          2        75 > 60            Es menor
#   60          3        60 == 60           Correcto


# pantalla:
# Adivina (1-100): 40
# Es mayor
# Adivina (1-100): 75
# Es menor
# Adivina (1-100): 60
# ¡Correcto en 3 intentos!

#______6) P6 -- Serie de Fibonacci
# Muestra los primeros N números de Fibonacci.
# La serie:
# 0, 1, 1, 2, 3, 5, 8, 13, 21...
# Cada número es la suma de los dos anteriores.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# n (input)

#---- Proceso:
# Crear dos variables iniciales:
# a = 0
# b = 1

# Repetir el proceso N veces.

# En cada repetición,
# mostrar el valor actual de a.

# Después actualizar los valores:
# a toma el valor de b.
# b toma la suma de a + b.

# De esta forma se genera
# el siguiente número de Fibonacci.

#---- Salida:
# Mostrar los primeros N números
# de la serie de Fibonacci.

#-------- 2. BOSQUEJO A MANO ------------
# n = 6

# a = 0
# b = 1

# Primera repetición:
# mostrar a:
# 0

# actualizar:

# a = 1
# b = 0 + 1

# a = 1
# b = 1

# Segunda repetición:
# mostrar a:
# 1

# actualizar:

# a = 1
# b = 1 + 1

# a = 1
# b = 2

# Tercera repetición:
# mostrar a:
# 1

# actualizar:

# a = 2
# b = 1 + 2

# a = 2
# b = 3

# Cuarta repetición:
# mostrar a:
# 2

# actualizar:

# a = 3
# b = 2 + 3

# a = 3
# b = 5

# Quinta repetición:
# mostrar a:
# 3

# actualizar:

# a = 5
# b = 3 + 5

# a = 5
# b = 8


# Sexta repetición:
# mostrar a:
# 5

# actualizar:

# a = 8
# b = 5 + 8

# a = 8
# b = 13

# resultado:
# 0 1 1 2 3 5

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso repetitivo.
# Cada número de Fibonacci se obtiene
# usando los dos valores anteriores.
# En cada repetición se hace:
# 1. Mostrar el valor actual de a.
# 2. Mover b hacia a.
# 3. Calcular el siguiente número
#    sumando a + b.
# El patrón principal es:
# a, b = b, a + b
# Este proceso se repite N veces,
# por eso se utiliza un ciclo for.

#-------- 4. ESCRIBIR EL CÓDIGO --------
n = int(input("¿Cuántos? "))

a, b = 0, 1

for _ in range(n):

    print(a, end=" ")

    a, b = b, a + b

print()

#-------- 5. PRUEBA DE ESCRITORIO --------
# n = 6

# repetición    a antes    b antes    salida    a después    b después
#     1            0          1          0           1            1
#     2            1          1          1           1            2
#     3            1          2          1           2            3
#     4            2          3          2           3            5
#     5            3          5          3           5            8
#     6            5          8          5           8           13


# pantalla:
# 0 1 1 2 3 5                           
