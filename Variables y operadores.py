#Variables y operadores

##Taller: 4 ejercicios paso a paso

#________ 1) Ejercicio 1 -- Calcular IVA (15%) y precio final
# Leer el precio de un producto sin IVA y mostrar el IVA
# y el precio final. El IVA en Ecuador es 15%.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# precio (input)

#---- Proceso:
# IVA = 0.15
# iva = precio * IVA
# total = precio + iva

#---- Salida:
# Mostrar el valor del IVA.
# Mostrar el precio final con IVA incluido.

#-------- 2. BOSQUEJO A MANO ------------
# precio = 100
# IVA = 0.15

# iva = 100 * 0.15
# iva = 15

# total = 100 + 15
# total = 115

# resultado:
# IVA: $15.00
# Total: $115.00

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón que se repita.
# El código es lineal: se ingresa el precio,
# se calcula el IVA, luego se suma al precio
# y finalmente se muestran los resultados.

#-------- 4. ESCRIBIR EL CÓDIGO --------
IVA = 0.15

precio = float(input("Precio sin IVA: $"))
iva = precio * IVA
total = precio + iva

print(f"IVA:   ${iva:.2f}")
print(f"Total: ${total:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                 precio     IVA     iva     total     pantalla
# IVA = 0.15                             0.15
# input                      100         0.15
# iva = precio * IVA         100         0.15    15
# total = precio + iva       100         0.15    15      115
# print                      100         0.15    15      115       IVA:   $15.00
#                                                               Total: $115.00

## Reto: Añadir un descuento del 10% que se aplique antes del IVA.
#        Muestra los tres valores: descuento, IVA, total

DESCUENTO = 0.10
IVA = 0.15

precio = float(input("Precio sin IVA: $"))
descuento = precio * DESCUENTO
iva = precio * IVA
total = precio + iva - descuento

print(f"Descuento:   ${descuento:.2f}\n"
      f"IVA:         ${iva:.2f}\n"
      f"Total:       ${total:.2f}")

#________ 2) Ejercicio 2 -- Par o impar
# Leer un número entero y determinar si es par o impar.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# num (input)

#---- Proceso:

# Comprobar el residuo de dividir num para 2.
# Si num % 2 == 0, el número es par.
# Caso contrario, el número es impar.

#---- Salida:
# Mostrar si el número ingresado es par o impar.

#-------- 2. BOSQUEJO A MANO ------------
# num = 8
# 8 % 2 = 0

# Como el residuo es 0:
# resultado = "par"

# resultado:
# 8 es par

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un proceso que se repita.
# El código es lineal y solo evalúa una condición:
# si el residuo de dividir el número para 2 es 0,
# es par; de lo contrario, es impar.

#-------- 4. ESCRIBIR EL CÓDIGO --------
num = int(input("Ingresa un número: "))

# Ternario: devuelve un valor u otro según la condición
resultado = "par" if num % 2 == 0 else "impar"

print(f"{num} es {resultado}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                    num      num % 2      resultado      pantalla
# input                          8
# num % 2                        8        0
# resultado                      8        0            par
# print                          8        0            par            8 es par

## Reto: Modificalo para que además diga si es múltiplo de 3, de 5, o de ambos

mensaje = ""

num = int(input("Ingresa un número: "))

# Ternario: devuelve un valor u otro según la condición
resultado = "par" if num % 2 == 0 else "impar"

if num%3 == 0 and num%5 == 0:
    mensaje = "y es múltiplo de 3 y de 5"
elif num%3 == 0:
    mensaje = "y es múltiplo de 3"
elif num%5 == 0:
    mensaje = "y es múltiplo de 5"

print(f"{num} es {resultado} {mensaje}")

#________ 3) Ejercicio 3 -- Convertir tiempo: segundos a hh:mm:ss
# Leer una cantidad total de segundos y mostrarla como hh:mm:ss.
# Ejemplo: 3725 segundos -> 01:02:05.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# total (input)

#---- Proceso:
# horas = total // 3600
# resto = total % 3600
# minutos = resto // 60
# segundos = resto % 60

#---- Salida:
# Mostrar el tiempo en formato hh:mm:ss.

#-------- 2. BOSQUEJO A MANO ------------
# total = 3725

# horas = 3725 // 3600
# horas = 1

# resto = 3725 % 3600
# resto = 125

# minutos = 125 // 60
# minutos = 2

# segundos = 125 % 60
# segundos = 5

# resultado:
# 01:02:05

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un proceso que se repita.
# El código es lineal: primero se calculan las horas,
# después se obtiene el resto, se calculan los minutos
# y finalmente los segundos restantes.

#-------- 4. ESCRIBIR EL CÓDIGO --------
total = int(input("Segundos totales: "))
horas = total // 3600
resto = total % 3600
minutos = resto // 60
segundos = resto % 60

print(f"{horas:02d}:{minutos:02d}:{segundos:02d}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                total     horas     resto     minutos     segundos     pantalla
# input                      3725
# horas = total // 3600      3725      1
# resto = total % 3600       3725      1         125
# minutos = resto // 60      3725      1         125       2
# segundos = resto % 60      3725      1         125       2           5
# print                      3725      1         125       2           5            01:02:05

## Reto: Al revés: leer hh:mm:ss y convertir a segundos totales. Tendrás que usar split(":").

tiempo = input("Ingrese la hora (hh:mm:ss): ")

horas, minutos, segundos = tiempo.split(":")

horas = int(horas)
minutos = int(minutos)
segundos = int(segundos)

total = horas * 3600 + minutos * 60 + segundos

print(f"Segundos totales: {total}")

#________ 4) Ejercicio 4 -- Cambio de billetes
# Un cajero solo tiene billetes de $20, $10, $5 y $1.
# Dado un monto, mostrar cuántos billetes de cada uno
# se necesitan usando la mínima cantidad.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# monto (input)

#---- Proceso:
# Guardar el monto en una variable resto.

# Calcular cuántos billetes de $20 caben en el monto
# y guardar lo que sobra.

# Repetir el proceso con billetes de $10, $5 y $1.

#---- Salida:
# Mostrar cuántos billetes de $20 se necesitan.
# Mostrar cuántos billetes de $10 se necesitan.
# Mostrar cuántos billetes de $5 se necesitan.
# Mostrar cuántos billetes de $1 se necesitan.

#-------- 2. BOSQUEJO A MANO ------------
# monto = 47
# resto = 47

# Billetes de $20:

# b20 = 47 // 20
# b20 = 2
# resto = 47 % 20
# resto = 7

# Billetes de $10:

# b10 = 7 // 10
# b10 = 0
# resto = 7 % 10
# resto = 7

# Billetes de $5:

# b5 = 7 // 5
# b5 = 1
# resto = 7 % 5
# resto = 2

# Billetes de $1:

# b1 = 2 // 1
# b1 = 2
# resto = 2 % 1
# resto = 0

# resultado:

# $20 × 2
# $10 × 0
# $5  × 1
# $1  × 2

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio sí existe un proceso que se repite.
# Para cada tipo de billete se hacen dos operaciones:

# 1. Dividir el resto entre el valor del billete usando //
#    para saber cuántos billetes se pueden utilizar.

# 2. Usar % para obtener el dinero restante.

# Este mismo proceso se repite con los billetes
# de $20, $10, $5 y $1.

#-------- 4. ESCRIBIR EL CÓDIGO --------
monto = int(input("Monto: $"))
resto = monto

b20 = resto // 20
resto = resto % 20

b10 = resto // 10
resto = resto % 10

b5 = resto // 5
resto = resto % 5

b1 = resto // 1
resto = resto % 1

print(f"$20 × {b20}")
print(f"$10 × {b10}")
print(f"$5  × {b5}")
print(f"$1  × {b1}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción             monto    resto    b20    b10    b5    b1
# input                   47
# resto = monto           47       47
# b20 = resto // 20       47       47       2
# resto = resto % 20      47       7        2
# b10 = resto // 10       47       7        2      0
# resto = resto % 10      47       7        2      0
# b5 = resto // 5         47       7        2      0      1
# resto = resto % 5       47       2        2      0      1
# b1 = resto // 1         47       2        2      0      1     2
# resto = resto % 1       47       0        2      0      1     2

# pantalla:
# $20 × 2
# $10 × 0
# $5  × 1
# $1  × 2

## Reto: Añadir billete de $50 al inicio. Después probar con monedas de 
#        $0.25, $0.10, $0.05 y $0.01 (necesitas trabajar con centavos).

entrada = input("Monto: $").strip()

if "." in entrada:
    dolares_str, centavos_str = entrada.split(".")
else:
    dolares_str, centavos_str = entrada, "0"

dolares = int(dolares_str)
centavos = int(centavos_str)

resto = dolares * 100 + centavos

b50 = resto // 5000
resto %= 5000

b20 = resto // 2000
resto %= 2000

b10 = resto // 1000
resto %= 1000

b5 = resto // 500
resto %= 500

b1 = resto // 100
resto %= 100


m25 = resto // 25
resto %= 25

m10 = resto // 10
resto %= 10

m5 = resto // 5
resto %= 5

m1 = resto

print(f"$50   × {b50}")
print(f"$20   × {b20}")
print(f"$10   × {b10}")
print(f"$5    × {b5}")
print(f"$1    × {b1}")
print(f"$0.25 × {m25}")
print(f"$0.10 × {m10}")
print(f"$0.05 × {m5}")
print(f"$0.01 × {m1}")

## --- Ejercicios Propuestos ---

#________ 1) P1 --- Suma dígitos de un número de 3 cifras
# Lee un número de 3 cifras y muestra la suma de sus dígitos.
# Ejemplo: 435 → 4 + 3 + 5 = 12.


#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# num (input)

#---- Proceso:
# Obtener la cifra de las centenas dividiendo el número entre 100.
# Obtener el resto después de quitar las centenas.
# Obtener la cifra de las decenas dividiendo el resto entre 10.
# Obtener la cifra de las unidades usando el residuo de la división entre 10.
# Sumar las centenas, decenas y unidades.

#---- Salida:
# Mostrar la suma de los tres dígitos.

#-------- 2. BOSQUEJO A MANO ------------
# num = 435

# Obtener centenas:
# centenas = 435 // 100
# centenas = 4

# Obtener el resto:
# resto = 435 % 100
# resto = 35

# Obtener decenas:
# decenas = 35 // 10
# decenas = 3

# Obtener unidades:
# unidades = 35 % 10
# unidades = 5

# Sumar los dígitos:
# suma = 4 + 3 + 5
# suma = 12

# resultado:
# La suma de sus dígitos: 12

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.

# El problema se resuelve de forma secuencial:

# primero se obtiene la centena,
# después la decena,
# luego la unidad
# y finalmente se suman los tres dígitos.

#-------- 4. ESCRIBIR EL CÓDIGO --------
num = int(input("Ingrese un número de 3 cifras: "))
centenas = num // 100
resto = num % 100

decenas = resto // 10
unidades = resto % 10

suma = centenas + decenas + unidades

print(f"La suma de sus dígitos: {suma}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                 num    centenas    resto    decenas    unidades    suma
# input                       435
# centenas = num // 100       435       4
# resto = num % 100           435       4         35
# decenas = resto // 10       435       4         35         3
# unidades = resto % 10       435       4         35         3          5
# suma = centenas +
#        decenas + unidades   435       4         35         3          5         12

# pantalla:
# La suma de sus dígitos: 12

#________ 2) P2 -- Convertir minutos a horas y minutos
# Lee una cantidad de minutos y muéstrala como
# «X horas Y minutos».
# Ejemplo: 135 → «2 horas 15 minutos».

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# ingreso_minutos (input)

#---- Proceso:
# Dividir la cantidad de minutos entre 60 usando //
# para obtener las horas completas.

# Usar % 60 para obtener los minutos que sobran.

#---- Salida:
# Mostrar la cantidad de horas.
# Mostrar los minutos restantes.

#-------- 2. BOSQUEJO A MANO ------------
# ingreso_minutos = 135

# Obtener las horas:
# horas = 135 // 60
# horas = 2

# Obtener los minutos restantes:
# minutos = 135 % 60
# minutos = 15

# resultado:
# 2 horas y 15 minutos

#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.
#
# El problema se resuelve de forma secuencial:
#
# primero se calculan las horas completas
# dividiendo entre 60,
#
# y después se obtienen los minutos restantes
# usando el residuo de la división entre 60.

#-------- 4. ESCRIBIR EL CÓDIGO --------
ingreso_minutos = int(input("Ingrese la cantidad de minutos: "))

horas = ingreso_minutos // 60
minutos = ingreso_minutos % 60

print(f"{horas} horas y {minutos} minutos")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                       ingreso_minutos    horas    minutos
# input                                  135
# horas = ingreso_minutos // 60          135             2
# minutos = ingreso_minutos % 60         135             2        15

# pantalla:
# 2 horas y 15 minutos

#________ 3) P3 -- Índice de masa corporal (IMC)
# Lee peso (kg) y estatura (m) y calcula el IMC.
# Fórmula: IMC = peso / estatura².
# Muestra el IMC con 2 decimales.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# peso (input)
# estatura (input)

#---- Proceso:
# Elevar la estatura al cuadrado.
# Dividir el peso entre la estatura al cuadrado.
# Guardar el resultado en la variable imc.

#---- Salida:
# Mostrar el IMC con 2 decimales.

#-------- 2. BOSQUEJO A MANO ------------
# peso = 70
# estatura = 1.75

# Elevar la estatura al cuadrado:

# estatura ** 2
# 1.75 ** 2 = 3.0625

# Calcular el IMC:
# imc = 70 / 3.0625
# imc = 22.8571...

# Mostrar con 2 decimales:
# imc = 22.86

# resultado:
# IMC: 22.86

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.
# El problema se resuelve de forma secuencial:
# primero se ingresan el peso y la estatura,
# después se eleva la estatura al cuadrado,
# y finalmente se divide el peso
# entre la estatura al cuadrado.

#-------- 4. ESCRIBIR EL CÓDIGO --------
peso = float(input("Ingrese el peso (KG): "))
estatura = float(input("Ingrese la estatura (m): "))

imc = peso / estatura**2

print(f"IMC: {imc:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                 peso    estatura    imc
# input peso                   70
# input estatura               70       1.75
# imc = peso /
#       estatura**2            70       1.75      22.8571...

# pantalla:
# IMC: 22.86

#________ 4) P4 -- Redondeo por cifra decimal
# Lee un número decimal y una cantidad de decimales,
# y muéstralo redondeado.
# Ejemplo: 3.14159 con 2 decimales → 3.14.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# numero_decimal (input)
# cantidad_decimal (input)

#---- Proceso:
# Redondear el número ingresado usando round().
# La cantidad de decimales indica
# cuántas cifras se conservarán después del punto.
# Guardar el valor redondeado en resultado.

#---- Salida:
# Mostrar el número redondeado.

#-------- 2. BOSQUEJO A MANO ------------
# numero_decimal = 3.14159
# cantidad_decimal = 2

# Redondear el número:
# resultado = round(3.14159, 2)
# resultado = 3.14

# resultado:
# 3.14

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.

# El problema se resuelve de forma secuencial:

# primero se ingresa el número decimal,

# después se ingresa la cantidad de decimales,

# y finalmente se utiliza round()
# para redondear el número.

#-------- 4. ESCRIBIR EL CÓDIGO --------
numero_decimal = float(input("Ingrese un número decimal: "))
cantidad_decimal = int(input("Ingrese la cantidad de decimales a mostrar: "))

resultado = round(numero_decimal, cantidad_decimal)

print(resultado)

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                     numero_decimal    cantidad_decimal    resultado
# input número                        3.14159
# input cantidad                      3.14159              2
# resultado = round(
# numero_decimal,
# cantidad_decimal)                   3.14159              2              3.14

# pantalla:
# 3.14

#________ 4) P4 -- Descuento por cantidad
# Un producto vale $12. Si compras 10 o más te dan 15% de descuento,
# si compras entre 5 y 9 te dan 5%. Calcula el total.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# cantidad_producto (input)

#---- Proceso:
# Multiplicar el precio del producto por la cantidad comprada
# para obtener el subtotal.

# Si se compran 10 productos o más,
# calcular un descuento del 15%.

# Si se compran entre 5 y 9 productos,
# calcular un descuento del 5%.

# Si se compran menos de 5 productos,
# no aplicar descuento.

# Restar el descuento al subtotal
# para obtener el total a pagar.

#---- Salida:
# Mostrar el precio unitario.
# Mostrar la cantidad de productos.
# Mostrar el subtotal.
# Mostrar el descuento.
# Mostrar el total a pagar.

#-------- 2. BOSQUEJO A MANO ------------
# PRECIO = 12
# cantidad_producto = 10

# Calcular subtotal:
# subtotal = 12 * 10
# subtotal = 120

# Como la cantidad es 10:
# cantidad_producto >= 10
# Se aplica un descuento del 15%.

# Calcular descuento:
# descuento = 120 * 0.15
# descuento = 18

# Calcular total:
# total = 120 - 18
# total = 102

# resultado:
# Precio unitario: 12
# Cantidad del producto: 10
# Subtotal: 120.00
# Descuento: 18.00
# Total: 102.00

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón repetitivo
# que necesite un ciclo.
# El problema se resuelve mediante condiciones.
# Dependiendo de la cantidad de productos comprados,
# se selecciona uno de tres casos:
# 10 o más productos → 15% de descuento.
# Entre 5 y 9 productos → 5% de descuento.
# Menos de 5 productos → sin descuento.

#-------- 4. ESCRIBIR EL CÓDIGO --------
PRECIO = 12
cantidad_producto = int(input("Cantidad del producto: "))
subtotal = PRECIO * cantidad_producto

if cantidad_producto >= 10:
    descuento = subtotal * 0.15
elif cantidad_producto > 4:
    descuento = subtotal * 0.05
else:
    descuento = 0

total = subtotal - descuento

print(f"Precio unitario: {PRECIO}\n"
      f"Cantidad del producto: {cantidad_producto}\n"
      f"Subtotal: {subtotal:.2f}\n"
      f"Descuento: {descuento:.2f}\n"
      f"Total: {total:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                     cantidad    subtotal    descuento    total
# input                              10
# subtotal = PRECIO * cantidad       10          120
# cantidad >= 10                     10          120
# descuento = subtotal * 0.15        10          120          18
# total = subtotal - descuento       10          120          18        102


# pantalla:

# Precio unitario: 12
# Cantidad del producto: 10
# Subtotal: 120.00
# Descuento: 18.00
# Total: 102.00
