#JS vs Python

##Taller: primeros ejercicios paso a paso

# __1) Ejercicio 1 -- Saludo Personalizado
# Leer el nombre del usuario y saludarlo por su nombre.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# nombre (input)
#---- Proceso:
# Guardar el nombre ingresado por el usuario.

#---- Salida:
# Mostrar un saludo utilizando el nombre ingresado.

#-------- 2. BOSQUEJO A MANO ------------
# nombre = "Dennis"
# resultado:
# Hola Dennis

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón que se repita.
# El código es lineal: se pide el nombre,
# se guarda y luego se muestra dentro de un saludo.

#-------- 4. ESCRIBIR EL CÓDIGO --------
nombre = input("¿Cómo te llamas? ")
print(f"Hola, {nombre}. Bienvenida al curso.")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción          nombre        pantalla
# input                Dennis
# print                Dennis        Hola Dennis

##Reto: Amplíalo para que además pida la edad y muestre «tienes X años».
nombre = input("¿Cómo te llamas? -- ")
edad = int(input("Ingrese su edad: "))
print(f"Hola, {nombre}. Bienvenida al curso. Tienes {edad} años.")

#___2) Ejercicio 2 -- Promedio de tres notas
#Leer tres notas de un estudiante y mostrar su promedio.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# n1 (input)
# n2 (input)
# n3 (input)

#---- Proceso:
# promedio = (n1 + n2 + n3) / 3

#---- Salida:
# Mostrar el promedio de las tres notas.

#-------- 2. BOSQUEJO A MANO ------------
# n1 = 8
# n2 = 9
# n3 = 7

# promedio = (8 + 9 + 7) / 3
# promedio = 24 / 3
# promedio = 8
# resultado:
# Promedio: 8.0

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón que se repita.
# El código es lineal: se leen las tres notas,
# se suman, se dividen para 3 y se muestra el promedio.

#-------- 4. ESCRIBIR EL CÓDIGO --------
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3
print(f"Promedio: {promedio:.1f}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                     n1      n2      n3      promedio      pantalla
# input n1                        8
# input n2                        8       9
# input n3                        8       9       7
# promedio = (n1+n2+n3)/3         8       9       7       8.0
# print                           8       9       7       8.0           Promedio: 8.0

##Reto: Modifícalo para que muestre «Aprueba» si el promedio es ≥ 7 
#       y «Reprueba» si no. (Necesitas el if del módulo 3).
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
promedio = (n1 + n2 + n3) / 3
if promedio >= 7:
    mensaje = "Aprueba"
else:
    mensaje = "Reprueba"
print(f"Promedio: {promedio} \nEl estudiante «{mensaje}» la asignatura.")

#___3) Ejercicio 3 -- Área y perímetro de un réctángulo
# Leer la base y la altura de un rectángulo y mostrar su área y su perímetro.
# Recuerda: área = base x altura, perímetro = 2 x (base + altura).

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# base (input)
# altura (input)

#---- Proceso:
# area = base * altura
# perimetro = 2 * (base + altura)

#---- Salida:
# Mostrar el área del rectángulo.
# Mostrar el perímetro del rectángulo.

#-------- 2. BOSQUEJO A MANO ------------
# base = 5
# altura = 3
# area = 5 * 3
# area = 15
# perimetro = 2 * (5 + 3)
# perimetro = 2 * 8
# perimetro = 16
# resultado:
# Área: 15.00
# Perímetro: 16.00

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón que se repita.
# El código es lineal: se leen la base y la altura,
# se calcula el área, luego el perímetro
# y finalmente se muestran ambos resultados.

#-------- 4. ESCRIBIR EL CÓDIGO --------
base = float(input("Base: "))
altura = float(input("Altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                    base    altura    area    perimetro    pantalla
# input base                     5
# input altura                   5       3
# area = base * altura           5       3         15
# perimetro = 2*(base+altura)    5       3         15      16
# print area                     5       3         15      16           Área: 15.00
# print perimetro                5       3         15      16           Perímetro: 16.00

##Reto: Ampliar para leer el radio de un círculo y mostrar área (pi * radio^2)
##      y perímetro (2pi * radio). Usa import math y math.pi

import math

base = float(input("Base del rectángulo: "))
altura = float(input("Altura del rectángulo: ")) 

area_rectangulo = base * altura
perimetro_rectangulo = 2 * (base + altura) 

radio = float(input("Radio del círculo: "))

area_circulo = math.pi * radio ** 2
perimetro_circulo = 2 * math.pi * radio

print(f"Área del rectángulo: {area_rectangulo:.2f}")
print(f"Perímetro del rectángulo: {perimetro_rectangulo:.2f}")
print(f"Área del círculo: {area_circulo:.2f}")
print(f"Perímetro del círculo: {perimetro_circulo:.2f}")

## --- Ejercicios Propuestos ---

##________ 1) P1 -- Convertir grados Celsius a Fahrenheit
#Pide una temperatura en grados Celsius y muéstrala en Fahrenheit. Fórmula: F = C × 9/5 + 32.


#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# temperatura_celsius (input)

#---- Proceso:
# fahrenheit = temperatura_celsius * 1.8 + 32

#---- Salida:
# Mostrar la temperatura ingresada en Celsius.
# Mostrar la temperatura convertida a Fahrenheit.

#-------- 2. BOSQUEJO A MANO ------------
# temperatura_celsius = 30
# fahrenheit = 30 * 1.8 + 32
# fahrenheit = 54 + 32
# fahrenheit = 86

# resultado:
# Temperatura (Celsius): 30
# Temperatura (Fahrenheit): 86

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón que se repita.
# El código es lineal: se pide la temperatura,
# se aplica la fórmula de conversión
# y finalmente se muestran ambos valores.

#-------- 4. ESCRIBIR EL CÓDIGO --------
temperatura_celsius = float(input("Ingrese la temperatura (Celsius): "))
fahrenheit = temperatura_celsius * 1.8 + 32

print(
    f"Temperatura (Celsius): {temperatura_celsius}\n"
    f"Temperatura (Fahrenheit): {fahrenheit:.1f}"
)

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                         temperatura_celsius    fahrenheit    pantalla
# input                              30
# fahrenheit = 30 * 1.8 + 32         30                     86.0
# print                              30                     86.0          Temperatura (Celsius): 30.0
#                                                                         Temperatura (Fahrenheit): 86.0

#________ 2) P2 -- Segundos a horas, minutos y segundos
#Pide un total de segundos y muéstralos como hh:mm:ss. Ej.: 3725 segundos → 1:02:05.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# segundos_ingresados (input)

#---- Proceso:
# horas = segundos_ingresados // 3600
# restante = segundos_ingresados % 3600
# minutos = restante // 60
# segundos = restante % 60

#---- Salida:
# Mostrar la cantidad de segundos ingresados.
# Mostrar el tiempo convertido en formato hh:mm:ss.

#-------- 2. BOSQUEJO A MANO ------------
# segundos_ingresados = 3725

# horas = 3725 // 3600
# horas = 1

# restante = 3725 % 3600
# restante = 125

# minutos = 125 // 60
# minutos = 2

# segundos = 125 % 60
# segundos = 5

# resultado:
# Segundos: 3725
# La hora es: 01:02:05

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón que se repita.
# El código es lineal: se ingresan los segundos,
# se calculan las horas, luego los minutos
# y finalmente los segundos restantes.

#-------- 4. ESCRIBIR EL CÓDIGO --------
segundos_ingresados = int(input("Ingrese una cantidad de segundos: "))
horas = segundos_ingresados // 3600
restante = segundos_ingresados % 3600
minutos = restante // 60
segundos = restante % 60

print(
    f"Segundos: {segundos_ingresados}\n"
    f"La hora es: {horas:02d}:{minutos:02d}:{segundos:02d}"
)

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                    seg_ingresados   horas   restante   minutos   segundos
# input                          3725
# horas = 3725 // 3600           3725             1
# restante = 3725 % 3600         3725             1       125
# minutos = 125 // 60            3725             1       125        2
# segundos = 125 % 60            3725             1       125        2         5

# pantalla:
# Segundos: 3725
# La hora es: 01:02:05

#________ 3) P3 -- Intercambiar dos variables
# Lee dos números y muéstralos intercambiados.
# Python permite hacerlo en una sola línea, muy diferente a JS.

#-------- 1. ENTENDER EL PROBLEMA --------
#---- Entrada:
# numero1 (input)
# numero2 (input)

#---- Proceso:
# Intercambiar los valores de numero1 y numero2.
# numero1, numero2 = numero2, numero1

#---- Salida:
# Mostrar numero1 con el valor que tenía numero2.
# Mostrar numero2 con el valor que tenía numero1.

#-------- 2. BOSQUEJO A MANO ------------
# numero1 = 10
# numero2 = 20

# intercambiar:
# numero1 = 20
# numero2 = 10

# resultado:
# número 1 = 20
# número 2 = 10

#-------- 3. DESCUBRIR EL PATRÓN --------
# En este ejercicio no hay un patrón que se repita.
# El código es lineal: se leen dos números,
# se intercambian sus valores
# y finalmente se muestran.

#-------- 4. ESCRIBIR EL CÓDIGO --------
numero1 = int(input("Número 1: "))
numero2 = int(input("Número 2: "))

numero1, numero2 = numero2, numero1

print(f"Número 1 = {numero1}\nNúmero 2 = {numero2}")

#-------- 5. PRUEBA DE ESCRITORIO --------
# instrucción                         numero1     numero2     pantalla
# input numero1                       10
# input numero2                       10          20
# numero1, numero2 = numero2, numero1
#                                     20          10
# print                               20          10          Número 1 = 20
#                                                             Número 2 = 10

#_____4) Calcular el IVA (15% Ecuador)
#Lee el precio de un producto sin IVA y muestra el IVA (15%) y el total.

precio_producto = float(input("Ingrese el precio del producto: "))
iva = precio_producto * 0.15
precio_total = precio_producto + iva

print(
    f"Precio: {precio_producto:.2f}\n"
    f"Iva: {iva:.2f}\nPrecio total: {precio_total:.2f}"
    )

