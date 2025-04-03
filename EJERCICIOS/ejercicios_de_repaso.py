'''
Ejercicio 1: Contar Letras en una Palabra
Problema:Solicitar al usuario una palabra y contar cuántas letras tiene.
'''

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
mi_lista=[2,4,5,6,4,3,7,8,4,9,10]
cantidad_de_numeros_pares=0
for numero in mi_lista:
    if numero%2==0:
        cantidad_de_numeros_pares+=1
print(cantidad_de_numeros_pares)


'''
Ejercicio 5: Filtrar Palabras Cortas y Largas
Problema:Pedir al usuario 5 palabras y separar las que tienen más de 5 letras y las que tienen menos o igual.
'''

'''
Ejercicio 6: Clasificar Números en Positivos y Negativos
Problema:Pedir 6 números al usuario y separarlos en positivos y negativos.
'''
mi_lista=[-8, 3, -6, 4, 5, -4]
cantidad_de_positivos=0
cantidad_de_negativos=0

for numero in mi_lista:
    if numero<0:
        cantidad_de_negativos+=1
    else:
        cantidad_de_positivos+=1
print(cantidad_de_positivos)
print(cantidad_de_negativos)
'''
Ejercicio 7: Contar Ocurrencias en una Lista
Problema:Pedir al usuario 7 números y contar cuántas veces aparece cada uno.
'''
'''
Ejercicio 8: Diccionario de Notas y Promedio
Problema:Pedir 3 nombres de estudiantes y sus notas, guardarlas en un diccionario y calcular el promedio.
'''
'''
Ejercicio 9: Encontrar la Palabra Más Larga
Problema:Pedir al usuario una lista de 4 palabras y encontrar la más larga.
'''
'''
Ejercicio 10: Clasificación de Edades
Problema:Solicitar 5 edades y clasificarlas en menores de edad (0-17), adultos (18-64) y adultos mayores (65+)
'''