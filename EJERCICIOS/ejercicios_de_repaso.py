'''
Ejercicio 1: Contar Letras en una Palabra
Problema:Solicitar al usuario una palabra y contar cuántas letras tiene.
'''
# palabra = input("Por favor, ingresa una palabra: ")
# contador = 0
# for letra in palabra:
#     contador += 1
# print(f"La palabra '{palabra}' tiene {contador} letras.")
'''
Ejercicio 2: Contar Vocales en un String
Problema:Pedir una frase al usuario y contar cuántas vocales (a, e, i, o, u) tiene.
'''
# palabra=input("Ingrese la palabra:")
# vocales="aeiouAEIOU"
# contador_de_vocales=0
# for letra in palabra:
#     if letra in vocales:
#         contador_de_vocales+=1
# print(contador_de_vocales)


'''
Ejercicio 3: Buscar una Palabra en una Lista
Problema:Crear una lista de palabras predefinida y pedir al usuario una palabra. Indicar si está en la lista o no.
'''

'''
Ejercicio 4: Contar Números Pares en una Lista
Problema:Solicitar 5 números al usuario, almacenarlos en una lista y contar cuántos son pares.
'''
# mi_lista=[2,4,5,6,4,3,7,8,4,9,10]

# cantidad_de_numeros_pares=0
# for numero in mi_lista:
#     if numero%2==0:
#         cantidad_de_numeros_pares+=1
# print(cantidad_de_numeros_pares)


'''
Ejercicio 5: Filtrar Palabras Cortas y Largas
Problema:Pedir al usuario 5 palabras y separar las que tienen más de 5 letras y las que tienen menos o igual.
'''
# lista_palabras = ["manzana", "pera", "plátano", "uva", "naranja"]
# palabra_buscar = input("Por favor, ingresa una palabra para buscar: ")
# encontrada = False
# for palabra in lista_palabras:
#     if palabra == palabra_buscar:
#         encontrada = True
#         break  
# if encontrada:
#     print(f"La palabra '{palabra_buscar}' está en la lista.")
# else:
#     print(f"La palabra '{palabra_buscar}' no está en la lista.")
'''
Ejercicio 6: Clasificar Números en Positivos y Negativos
Problema:Pedir 6 números al usuario y separarlos en positivos y negativos.
'''
# mi_lista=[-8, 3, -6, 4, 5, -4]
# cantidad_de_positivos=0
# cantidad_de_negativos=0

# for numero in mi_lista:
#     if numero<0:
#         cantidad_de_negativos+=1
#     else:
#         cantidad_de_positivos+=1
# print(cantidad_de_positivos)
# print(cantidad_de_negativos)
'''
Ejercicio 7: Contar Ocurrencias en una Lista
Problema:Pedir al usuario 7 números y contar cuántas veces aparece cada uno.
'''

# numeros = []
# print("Por favor, ingresa 7 números:")
# for i in range(7):
#     numero = int(input(f"Número {i + 1}: "))
#     numeros.append(numero)

# conteo = {}

# for numero in numeros:
#     if numero in conteo:
#         conteo[numero] += 1
#     else:
#         conteo[numero] = 1

# print("\nOcurrencias de cada número:")
# for numero, cantidad in conteo.items():
#     print(f"El número {numero} aparece {cantidad} veces.")
'''
Ejercicio 8: Diccionario de Notas y Promedio
Problema:Pedir 3 nombres de estudiantes y sus notas, guardarlas en un diccionario y calcular el promedio.
'''
# notas_estudiantes = {}

# print("Por favor, ingresa los nombres de 3 estudiantes y sus respectivas notas.")
# for i in range(3):
#     nombre = input(f"Nombre del estudiante {i + 1}: ")
#     nota = float(input(f"Nota de {nombre}: "))
#     notas_estudiantes[nombre] = nota

# promedio = sum(notas_estudiantes.values()) / len(notas_estudiantes)

# print("\nDiccionario de notas:")
# for nombre, nota in notas_estudiantes.items():
#     print(f"{nombre}: {nota}")

# print(f"\nEl promedio de las notas es: {promedio:.2f}")
'''
Ejercicio 9: Encontrar la Palabra Más Larga
Problema:Pedir al usuario una lista de 4 palabras y encontrar la más larga.
'''

# palabras = []
# print("Por favor, ingresa 4 palabras:")
# for i in range(4):
#     palabra = input(f"Palabra {i + 1}: ")
#     palabras.append(palabra)

# palabra_mas_larga = ""

# for palabra in palabras:
#     if len(palabra) > len(palabra_mas_larga):
#         palabra_mas_larga = palabra

# print(f"\nLa palabra más larga es: '{palabra_mas_larga}' con {len(palabra_mas_larga)} letras.")
'''
Ejercicio 10: Clasificación de Edades
Problema:Solicitar 5 edades y clasificarlas en menores de edad (0-17), adultos (18-64) y adultos mayores (65+)
'''

edades = []
print("Por favor, ingresa 5 edades:")
for i in range(5):
    edad = int(input(f"Edad {i + 1}: "))
    edades.append(edad)

menores = 0
adultos = 0
adultos_mayores = 0

for edad in edades:
    if 0 <= edad <= 17:
        menores += 1
    elif 18 <= edad <= 64:
        adultos += 1
    elif edad >= 65:
        adultos_mayores += 1

print("\nClasificación de edades:")
print(f"Menores de edad (0-17 años): {menores}")
print(f"Adultos (18-64 años): {adultos}")
print(f"Adultos mayores (65+ años): {adultos_mayores}")