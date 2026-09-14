# Colecciones básicas de Python

#Ejercicios propuestos

#____1) P1 -- Contar vocales en una cadena
# Pide una frase al usuario y cuenta cuántas vocales
# (a, e, i, o, u) tiene.
# Ignora mayúsculas/minúsculas.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# frase (input)


#---- Proceso:

# Pedir una frase al usuario.

# Convertir toda la frase a minúsculas
# usando .lower().

# Crear un conjunto con las vocales:

# a, e, i, o, u

# Crear un contador llamado total
# que empiece en 0.

# Recorrer cada carácter de la frase.

# Verificar si el carácter
# se encuentra dentro de vocales.

# Si es una vocal,
# aumentar total en 1.


#---- Salida:

# Mostrar la cantidad total
# de vocales encontradas.



#-------- 2. BOSQUEJO A MANO ------------

# frase = "Hola Mundo"


# Convertir a minúsculas:

# frase = "hola mundo"


# vocales = {"a", "e", "i", "o", "u"}

# total = 0


# Primer carácter:

# ch = "h"

# "h" no está en vocales

# total = 0


# Segundo carácter:

# ch = "o"

# "o" está en vocales

# total = 0 + 1

# total = 1


# Tercer carácter:

# ch = "l"

# no es vocal

# total = 1


# Cuarto carácter:

# ch = "a"

# es vocal

# total = 2


# El proceso continúa con
# todos los caracteres.


# En "mundo":

# "u" → vocal

# "o" → vocal


# total final = 4


# resultado:

# 4 vocales



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Cada carácter de la frase pasa
# por el mismo proceso:
#
# 1. Tomar un carácter.
#
# 2. Verificar si está dentro
#    del conjunto de vocales.
#
# 3. Si es una vocal,
#    aumentar el contador.
#
# El patrón principal es:
#
# for ch in frase:
#
#     if ch in vocales:
#
#         total += 1
#
# Este proceso se repite para todos
# los caracteres de la frase.



#-------- 4. ESCRIBIR EL CÓDIGO --------

frase = input("Frase: ").lower()

vocales = {"a", "e", "i", "o", "u"}

total = 0

for ch in frase:

    if ch in vocales:
        total += 1

print(f"{total} vocales")



#-------- 5. PRUEBA DE ESCRITORIO --------

# frase = "Hola Mundo"

# después de .lower():

# frase = "hola mundo"


# carácter    ¿es vocal?    total

#    h            No           0

#    o            Sí           1

#    l            No           1

#    a            Sí           2

# espacio         No           2

#    m            No           2

#    u            Sí           3

#    n            No           3

#    d            No           3

#    o            Sí           4


# pantalla:

# 4 vocales

#____2) P2 -- Promedio y máximo de una lista de notas
# Dada una lista fija de notas [7, 8.5, 6, 9, 10, 5.5],
# calcula el promedio, la nota máxima y la mínima.
# Imprime los tres valores con 2 decimales.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# notas = [7, 8.5, 6, 9, 10, 5.5]


#---- Proceso:

# Sumar todas las notas usando sum().

# Contar cuántas notas existen usando len().

# Dividir la suma entre la cantidad de notas
# para obtener el promedio.

# Buscar la nota más alta usando max().

# Buscar la nota más baja usando min().


#---- Salida:

# Mostrar el promedio con 2 decimales.

# Mostrar la nota máxima con 2 decimales.

# Mostrar la nota mínima con 2 decimales.



#-------- 2. BOSQUEJO A MANO ------------

# notas = [7, 8.5, 6, 9, 10, 5.5]


# Sumar las notas:

# 7 + 8.5 + 6 + 9 + 10 + 5.5

# suma = 46


# Cantidad de notas:

# len(notas) = 6


# Calcular promedio:

# promedio = 46 / 6

# promedio = 7.6666...


# Con 2 decimales:

# promedio = 7.67


# Buscar máxima:

# max(notas)

# maxima = 10


# Buscar mínima:

# min(notas)

# minima = 5.5


# resultado:

# Promedio: 7.67

# Máximo: 10.00

# Mínimo: 5.50



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio no hay un patrón repetitivo
# que necesitemos programar con un ciclo.
#
# Python ya realiza internamente
# las operaciones necesarias usando:
#
# sum(notas)
#
# len(notas)
#
# max(notas)
#
# min(notas)
#
# El problema se resuelve de forma secuencial:
#
# primero se calcula el promedio,
#
# después se obtiene el máximo,
#
# y finalmente se obtiene el mínimo.



#-------- 4. ESCRIBIR EL CÓDIGO --------

notas = [7, 8.5, 6, 9, 10, 5.5]

promedio = sum(notas) / len(notas)

print(f"Promedio: {promedio:.2f}")

print(f"Máximo:   {max(notas):.2f}")

print(f"Mínimo:   {min(notas):.2f}")



#-------- 5. PRUEBA DE ESCRITORIO --------

# notas = [7, 8.5, 6, 9, 10, 5.5]


# operación             resultado

# sum(notas)              46

# len(notas)               6

# 46 / 6                  7.6666...

# max(notas)              10

# min(notas)               5.5


# pantalla:

# Promedio: 7.67

# Máximo:   10.00

# Mínimo:   5.50

#____3) P3 -- Eliminar duplicados manteniendo el orden
# Dada la lista ["a", "b", "a", "c", "b", "d"],
# retorna una nueva lista sin duplicados
# respetando el orden de la primera aparición.
#
# Con set se eliminan duplicados,
# pero para conservar el orden se combina set + list.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# datos = ["a", "b", "a", "c", "b", "d"]


#---- Proceso:

# Crear un conjunto vacío llamado vistos.

# Crear una lista vacía llamada resultado.

# Recorrer cada elemento de datos.

# Verificar si el elemento
# todavía no está en vistos.

# Si no está:

# agregarlo al conjunto vistos.

# agregarlo también a resultado.

# Si ya estaba en vistos,
# no volver a agregarlo.


#---- Salida:

# Mostrar una nueva lista
# sin elementos repetidos
# y manteniendo el orden original.



#-------- 2. BOSQUEJO A MANO ------------

# datos = ["a", "b", "a", "c", "b", "d"]

# vistos = set()

# resultado = []


# Primer elemento:

# x = "a"

# "a" no está en vistos.

# vistos = {"a"}

# resultado = ["a"]


# Segundo elemento:

# x = "b"

# "b" no está en vistos.

# vistos = {"a", "b"}

# resultado = ["a", "b"]


# Tercer elemento:

# x = "a"

# "a" ya está en vistos.

# No se agrega.


# resultado sigue:

# ["a", "b"]


# Cuarto elemento:

# x = "c"

# "c" no está en vistos.

# vistos = {"a", "b", "c"}

# resultado = ["a", "b", "c"]


# Quinto elemento:

# x = "b"

# "b" ya está en vistos.

# No se agrega.


# Sexto elemento:

# x = "d"

# "d" no está en vistos.

# vistos = {"a", "b", "c", "d"}

# resultado = ["a", "b", "c", "d"]


# resultado:

# ["a", "b", "c", "d"]



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Para cada elemento de la lista
# se repite el mismo proceso:
#
# 1. Tomar un elemento.
#
# 2. Verificar si ya apareció.
#
# 3. Si no apareció,
#    guardarlo en vistos.
#
# 4. Agregarlo también a resultado.
#
# El patrón principal es:
#
# for x in datos:
#
#     if x not in vistos:
#
#         vistos.add(x)
#
#         resultado.append(x)
#
# De esta manera,
# cada elemento se guarda
# solamente la primera vez que aparece.



#-------- 4. ESCRIBIR EL CÓDIGO --------

datos = ["a", "b", "a", "c", "b", "d"]

vistos = set()

resultado = []

for x in datos:

    if x not in vistos:

        vistos.add(x)

        resultado.append(x)

print(resultado)



#-------- 5. PRUEBA DE ESCRITORIO --------

# datos = ["a", "b", "a", "c", "b", "d"]


# x      ¿está en vistos?      vistos               resultado

# a           No              {"a"}                 ["a"]

# b           No              {"a", "b"}            ["a", "b"]

# a           Sí              {"a", "b"}            ["a", "b"]

# c           No              {"a", "b", "c"}       ["a", "b", "c"]

# b           Sí              {"a", "b", "c"}       ["a", "b", "c"]

# d           No              {"a", "b", "c", "d"}  ["a", "b", "c", "d"]


# pantalla:

# ['a', 'b', 'c', 'd']

#___4) P4 -- Contar frecuencia de palabras
# Dado un texto, retorna un diccionario con la frecuencia
# de cada palabra (ignora mayúsculas).
# Al final, imprime la palabra que más se repite.


#-------- 1. ENTENDER EL PROBLEMA --------

#---- Entrada:

# texto


#---- Proceso:

# Convertir todo el texto a minúsculas
# usando .lower().

# Separar el texto en palabras
# usando .split().

# Crear un diccionario vacío llamado conteo.

# Recorrer cada palabra del texto.

# Si la palabra todavía no existe,
# comenzar su contador en 0.

# Aumentar su frecuencia en 1.

# Después buscar la palabra
# que tenga la frecuencia más alta.


#---- Salida:

# Mostrar el diccionario
# con la frecuencia de cada palabra.

# Mostrar la palabra más repetida
# y cuántas veces aparece.



#-------- 2. BOSQUEJO A MANO ------------

# texto = "El perro y el gato y el perro"


# Convertir a minúsculas:

# "el perro y el gato y el perro"


# Separar:

# ["el", "perro", "y", "el", "gato", "y", "el", "perro"]


# conteo = {}


# Primera palabra:

# palabra = "el"

# conteo.get("el", 0)

# como "el" no existe:

# devuelve 0


# 0 + 1 = 1


# conteo = {
#     "el": 1
# }


# Segunda palabra:

# palabra = "perro"

# conteo = {
#     "el": 1,
#     "perro": 1
# }


# Tercera palabra:

# palabra = "y"

# conteo = {
#     "el": 1,
#     "perro": 1,
#     "y": 1
# }


# Cuarta palabra:

# palabra = "el"

# "el" ya tiene 1.

# 1 + 1 = 2


# conteo["el"] = 2


# El proceso continúa
# con las demás palabras.


# conteo final:

# {
#     "el": 3,
#     "perro": 2,
#     "y": 2,
#     "gato": 1
# }


# Buscar la más repetida:

# mas = "el"


# conteo["el"] = 3


# resultado:

# Más repetida: 'el' (3 veces)



#-------- 3. DESCUBRIR EL PATRÓN --------

# En este ejercicio sí existe un proceso repetitivo.
#
# Para cada palabra del texto
# se repite el mismo proceso:
#
# 1. Tomar una palabra.
#
# 2. Consultar cuántas veces
#    ha aparecido hasta el momento.
#
# 3. Aumentar su contador en 1.
#
# El patrón principal es:
#
# conteo[palabra] = conteo.get(palabra, 0) + 1
#
# Este proceso se repite
# para todas las palabras del texto.
#
# Después se utiliza max()
# para encontrar la palabra
# con la frecuencia más alta.



#-------- 4. ESCRIBIR EL CÓDIGO --------

texto = "El perro y el gato y el perro"

conteo = {}

for palabra in texto.lower().split():

    conteo[palabra] = conteo.get(palabra, 0) + 1


print(conteo)


mas = max(conteo, key=conteo.get)

print(f"Más repetida: '{mas}' ({conteo[mas]} veces)")



#-------- 5. PRUEBA DE ESCRITORIO --------

# palabras:

# ["el", "perro", "y", "el", "gato", "y", "el", "perro"]


# palabra    conteo después de procesarla

# "el"       {"el": 1}

# "perro"    {"el": 1, "perro": 1}

# "y"        {"el": 1, "perro": 1, "y": 1}

# "el"       {"el": 2, "perro": 1, "y": 1}

# "gato"     {"el": 2, "perro": 1, "y": 1, "gato": 1}

# "y"        {"el": 2, "perro": 1, "y": 2, "gato": 1}

# "el"       {"el": 3, "perro": 1, "y": 2, "gato": 1}

# "perro"    {"el": 3, "perro": 2, "y": 2, "gato": 1}


# palabra con mayor frecuencia:

# mas = "el"

# conteo["el"] = 3


# pantalla:

# {'el': 3, 'perro': 2, 'y': 2, 'gato': 1}

# Más repetida: 'el' (3 veces)