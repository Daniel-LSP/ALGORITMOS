# Ejercicio 2.1 
'''
Cree una variable llamada cadena que contenga 
una cadena de texto “Python puro”.  Al crearla 
verifique el tipo de dato que queda guardado en 
memoria utilizando la función type.
'''
# # Crear la variable 'cadena' con el texto "Python puro"
# cadena = "Python puro"

# # Verificar el tipo de dato con la función type
# tipo_de_dato = type(cadena)

# # Mostrar el tipo de dato
# print(f"El contenido de la variable 'cadena' es: '{cadena}'")
# print(f"El tipo de dato almacenado en 'cadena' es: {tipo_de_dato}")

# Ejercicio 2.2 
'''
Utilice un método que le permita poner en 
mayúscula la palabra puro. 
'''
# # Crear una lista que contenga palabras
# palabras = ["Python", "puro"]

# # Buscar y convertir la palabra "puro" a mayúsculas
# palabras_modificadas = [palabra.upper() if palabra == "puro" else palabra for palabra in palabras]

# # Mostrar el resultado
# print(" ".join(palabras_modificadas))

# Ejercicio 2.3 
'''
Qué diferencia encuentra entre el método titlle y el 
método capitalize. 
'''
# #CAPITALIZE
# #Convierte únicamente la primera letra de la cadena a mayúscula y convierte el resto a minúsculas.
# texto = "python ES asombroso"
# print(texto.capitalize())  # Resultado: "Python es asombroso"

# #TITLE
# #Convierte la primera letra de cada palabra en mayuscula y convierte el resto de las letras de cada palabra en minuscula
# texto = "python ES asombroso"
# print(texto.title())  # Resultado: "Python Es Asombroso"

# Ejercicio 2.4 
'''
Aplique un método para verificar si la letra o es la 
que finaliza la cadena de caracteres. 
'''
# # Definir la cadena
# cadena = "Python puro"

# # Verificar si la letra 'o' es la última usando el método endswith
# termina_con_o = cadena.endswith("o")

# # Mostrar el resultado
# print(f"¿La cadena termina con la letra 'o'? {termina_con_o}")

# Ejercicio 2.5 
'''
Investigue cómo utilizar el método casefold sobre 
la cadena de texto y para qué serviría. 
'''
#METODO CASEFOLD
#Este método se utiliza para realizar comparaciones de texto
#que no distingan entre mayúsculas y minúsculas. Es más potente 
#que  porque maneja mejor ciertos idiomas y caracteres especiales.
#Proposito: El metodo casefold sirve para comparar cadenas de texto de manera 
#insensible a las diferencias de casos, util en validaciones o busquedas.
# Comparar cadenas ignorando mayúsculas y minúsculas
# texto1 = "Python".casefold()
# texto2 = "PYTHON".casefold()

# # Verificar si son iguales
# son_iguales = texto1 == texto2

# # Mostrar el resultado
# print(f"¿Son iguales? {son_iguales}")

# Ejercicio 2.6 
'''
Cree un programa que defina una lista con las 
primeras cinco letras del alfabeto en minúscula. 
Posterior a la creación de la lista, aplique un método 
para insertar en la posición 2 la letra a. Ahora, 
aplique un método para contar el número de veces 
que la letra a se encuentra en la lista creada. 
'''
# Crear la lista con las primeras cinco letras del alfabeto
# letras = ["a", "b", "c", "d", "e"]

# # Insertar la letra 'a' en la posición 2
# letras.insert(2, "a")

# # Contar el número de veces que aparece la letra 'a'
# conteo_a = letras.count("a")

# # Mostrar la lista y el conteo
# print(f"Lista: {letras}")
# print(f"Número de veces que aparece la letra 'a': {conteo_a}")

# Ejercicio 2.7 
'''
Utilizando la lista creada en el punto anterior 
aplique el método que le permita eliminar la letra c 
que se encuentra en la posición 3. Confirme que el 
método utilizado devuelva la letra eliminada y que 
al llamar nuevamente la lista el elemento no se 
encuentre en la posición indicada. 
'''
# Utilizar la lista creada en el ejercicio anterior
# letras = ["a", "b", "a", "c", "d", "e"]

# # Eliminar la letra 'c' de la posición 3
# letra_eliminada = letras.pop(3)
# letras.append('c')

# # Mostrar la letra eliminada y la lista actualizada
# print(f"Letra eliminada: {letra_eliminada}")
# print(f"Lista actualizada: {letras}")

# Ejercicio 2.8 
'''
Cree una lista con los números del 1 al 10 
considerando el orden de su preferencia. 
Llame a la lista valores. Aplique un método 
que le permita ordenar los valores desde el 
mayor al menor. Si ahora utiliza la función 
sorted sobre la lista, ¿qué diferencia 
encuentra?. 
'''
#Diferencia:
#sort() modifica directamente la lista original.
#sorted() crea una nueva lista con los valores ordenados, dejando la original
# Crear la lista con números en orden aleatorio
# valores = [3, 1, 4, 10, 7, 5, 2, 8, 9, 6]

# # Ordenar la lista de mayor a menor
# valores.sort(reverse=True)
# print(f"Lista ordenada de mayor a menor: {valores}")

# # Utilizar la función sorted para comparar
# valores_sorted = sorted(valores)
# print(f"Lista ordenada con sorted: {valores_sorted}")
# Ejercicio 2.9 
'''
Considere la creación de una nueva lista 
llamada duplicada que sea una copia de la 
lista valores. Posteriormente ejecute una 
instrucción para que la copia quede 
ordenada desde los valores más bajos a los 
más altos.
# '''
# # # Crear la lista original
# valores = [3, 1, 4, 10, 7, 5, 2, 8, 9, 6]

# # # Crear una copia de la lista
# duplicada = valores.copy()

# # # Ordenar la copia de menor a mayor
# duplicada.sort()
# print(f"Lista original: {valores}")
# print(f"Lista duplicada y ordenada: {duplicada}")

# Ejercicio 2.10 
'''
Cree una tupla llamada ventas que considere 
en la primera posición el nombre de un 
producto y su precio. Para el ejemplo puede 
considerar leche como el nombre y su precio 
5. Utilice el método index para consultar el 
índice correspondiente al precio. Ahora en 
otra instrucción y utilizando el índice intente 
reemplazar el elemento asignándole un 
nuevo valor 8. ¿Qué interpreta del error que 
sale al ejecutar la instrucción? 
'''
# # Crear la tupla con nombre de producto y precio
# ventas = ("leche", 5)

# # Consultar el índice del precio usando index()
# indice_precio = ventas.index(5)
# print(f"El índice del precio es: {indice_precio}")

# # Intentar modificar el elemento en el índice obtenido
# try:
#     ventas[indice_precio] = 8  # Esto generará un error
# except TypeError as e:
#     print(f"Error: {e}")
'''
Interpretacion del error:
El error ocurre porque las tuplas son inmutables,
lo que significa que no se pueden modificar despues 
de ser creadas. Eso es diferente a una lista, que si permite 
cambios en sus elementos.
'''

#Ejercicio 2.11
'''
Con la tupla definida en el ejercicio anterior 
aplique el metodo count para consultar cuantas veces
aparece la letra "e" dentro de la tupla, de esta manera:
>>> ventas.count("e")
Interprete el resultado
Posteriormente indexe la tupla y consulte cuantas veces
aparece la letra "e" dentro del primer elemento de la tupla.
>>> ventas[0].count("e")
¿Que diferencias encuentra en los dos resultados?
'''
# ventas = ("leche", 5)
# resultado = ventas.count("e")
# resultado_elemento = ventas[0].count("e")
# print(resultado)
# print(resultado_elemento)

'''
Interpretación del 1 resultado: El método  aplicado sobre 
la tupla busca exactamente el objeto  dentro de los elementos
completos de la tupla. En este caso,  como elemento individual
no está presente en la tupla, por lo que el resultado es .
'''
'''
Interpretacion del 2 resultado: Aquí estás utilizando el método  
sobre una cadena (el primer elemento de la tupla, ). Este método 
busca y cuenta cuántas veces aparece la letra  en esa cadena específica.
En este caso,  tiene 2 apariciones de la letra , por lo que el resultado
es 2.
'''
'''
Diferencias:
En el primer caso (), se busca la presencia del objeto  como elemento 
independiente dentro de la tupla.
En el segundo caso (), se busca dentro de un elemento específico de
la tupla (una cadena) cuántas veces aparece.
'''
# Ejercicio 2.12 
'''
Defina un conjunto vacío denominado figuras. A 
continuación, utilice un método para que el 
conjunto contenga los nombres de tres figuras 
geométricas, por ejemplo: circulo, cuadrado, 
rectángulo. Aplique un método que permita 
agregar un nuevo elemento utilizando 
exactamente uno de los nombres ya definidos. 
Consulte el estado actual del conjunto figuras, 
¿qué interpreta del resultado?
'''
# figuras = set()
# figuras.add("circulo")
# figuras.add("cuadrado")
# figuras.add("rectangulo")
# print(figuras)  # Resultado: {'circulo', 'cuadrado', 'rectangulo'}
# figuras.add("circulo")
# print(figuras)  # Resultado: {'circulo', 'cuadrado', 'rectangulo'}

'''
Interpretacion del resultado
El conjunto  mantiene la propiedad de no permitir
elementos duplicados, lo que significa que aunque 
se intente agregar  (que ya existe en el conjunto),
no se genera un cambio en su contenido. Los conjuntos 
en Python son estructuras que automáticamente evitan la
duplicidad de sus elementos.
'''
# Ejercicio 2.13
''' 
Emplee el conjunto figuras definido en el 
ejercicio 
anterior. 
instrucción: 
>>> figuras[0] 
Emplee la siguiente 
¿Qué interpreta del resultado? 
'''
# figuras[0] #TypeError: 'set' object is not subscriptable
'''
Intentar acceder al conjunto  mediante un índice, como en figuras[0], 
generará un error en Python. Esto sucede porque los conjuntos ()
en Python no están indexados. A diferencia de las listas o tuplas,
los conjuntos no tienen un orden específico para sus elementos, 
ya que su propósito principal es almacenar elementos únicos y no 
necesariamente ordenados.
'''
# figuras_lista = list(figuras)
# print(figuras_lista[0])  # Acceder al primer elemento del conjunto como lista
'''
Esto te permitirá acceder a los elementos, aunque el orden en 
el que se convierten los elementos del conjunto en la lista será 
aleatorio (ya que los conjuntos no conservan un orden).
'''

# Ejercicio 2.14 
'''
Utilice el conjunto figuras definido 
anteriormente. Aplique el método unión 
agregando dentro del argumento otro conjunto 
que incluya más figuras geométricas. Consulte de 
nuevo el conjunto figuras. ¿que interpreta del resultado?
'''
# figuras = {"circulo", "cuadrado", "rectangulo"}
# nuevas_figuras = {"triangulo", "pentagono", "hexagono"}
# conjunto_union = figuras.union(nuevas_figuras)
# print(conjunto_union)  # Resultado: {'circulo', 'cuadrado', 'rectangulo', 'triangulo', 'pentagono', 'hexagono'}

'''El método union no modifica el conjunto original figuras.
En su lugar, devuelve un nuevo conjunto que contiene los elementos 
de ambos conjuntos (figuras y nuevas_figuras).'''
'''El conjunto resultante incluye todos los elementos de ambos conjuntos, 
pero sin duplicados. Por ejemplo, si una figura geométrica estuviera en 
ambos conjuntos, aparecería solo una vez en el conjunto final, gracias a 
la propiedad de unicidad de los conjuntos.'''

# print(figuras)  # Resultado: {'circulo', 'cuadrado', 'rectangulo'}

# Ejercicio 2.15 
'''
Cree un conjunto llamado personas con nombres de personas que 
conozca. Aplique el método update de la siguiente manera: 
>>> personas.update( { “pedro”, “ramiro ”} ) 
Posteriormente aplique el método pop. ¿Cómo describiría el uso 
de este método y qué argumentos necesita para operar? 
'''
# personas = {"ana", "luis", "maria"}  # Por ejemplo, nombres conocidos
# personas.update({"pedro", "ramiro"})
# print(personas)  
# Resultado: {'ana', 'luis', 'maria', 'pedro', 'ramiro'}
'''
El método update agrega todos los elementos del conjunto 
proporcionado ({"pedro", "ramiro"}) al conjunto personas. Si algún elemento ya existía,
no se duplicará debido a la naturaleza de los conjuntos 
(que no permiten duplicados).
'''
# elemento_removido = personas.pop()
# print(elemento_removido)  
# print(personas)  
# Resultado: un elemento eliminado, y el conjunto actualizado
'''
El método  elimina y devuelve un elemento arbitrario del conjunto. 
Esto se debe a que los conjuntos no están ordenados.
Argumentos necesarios:  no toma argumentos.
Si el conjunto está vacío, genera un keyError.
'''
# Ejercicio 2.16
''' 
Utilice personas el conjunto de los definido ejercicios anteriores. 
Cree ahora un nuevo conjunto llamado estudiantes definido de la siguiente manera: 
>>> estudiantes = {‘ luciana‘, ‘ramiro ‘} 
Aplique el método que permite establecer los elementos diferentes 
entre los dos conjuntos tomando como base el conjunto personas, 
¿Qué logra identificar de los resultados?, ¿para qué serviría el método?  
'''
# estudiantes = {"luciana", "ramiro"}
# diferentes = personas.difference(estudiantes)
# print(diferentes)  
# Resultado: Elementos presentes en `personas` pero no en `estudiantes`
'''
El método difference devuelve un conjunto que contiene los elementos de personas 
que no están en estudiantes.
Este método sirve para identificar elementos únicos de un conjunto en comparación 
con otro, lo cual es útil en análisis de datos o para distinguir categorías.
'''
# Ejercicio 2.17 
'''
Ejecute la última instrucción del ejercicio anterior pero ahora 
tomando como base el conjunto estudiantes. 
¿Qué diferencia encuentra entre los dos resultados? 
'''
# diferentes_estudiantes = estudiantes.difference(personas)
# print(diferentes_estudiantes)
# Resultado: Elementos presentes en `estudiantes` pero no en `personas`
'''
Cuando se usa personas.difference(estudiantes), se identifican elementos 
en personas que no están en estudiantes.
Con estudiantes.difference(personas), se identifican los elementos en 
estudiantes que no están en personas. 
Los resultados dependen del conjunto base que uses para la operación difference.
'''

# Ejercicio 2.18
'''
Se desea conocer si el conjunto estudiantes es un 
subconjunto de las personas. Subconjunto significa 
que todos los elementos que son parte de 
estudiantes están igualmente definidos en el 
conjunto personas. Aplique un método para 
conocer la respuesta. 
'''
estudiantes = {"luciana", "ramiro"}
personas = {"ana", "luis", "maria", "pedro", "ramiro", "luciana"}

es_subconjunto = estudiantes.issubset(personas)
print(es_subconjunto)  # Resultado: True

'''
Interpretación: El método issubet verifica si todos los elementos del 
conjunto estudiantes están contenidos dentro del conjunto personas. En este caso, 
devuelve true , ya que ambos elementos de estudiantes están en personas.
'''
# Ejercicio 2.19 
'''
Actualmente los conjuntos no tienen un método 
built-in en Python 3.8 para ordenar los elementos 
que lo componen. Esto se debe a que en un conjunto 
el orden no interesa, sin embargo, es posible aplicar 
la función sorted. Ejecute una instrucción que utilice 
esta función e interprete el resultado. 
'''
conjunto_ordenado = sorted(personas)
print(conjunto_ordenado)  # Resultado: Lista ordenada de los elementos
'''
Interpretación: La función sorted convierte el conjunto en una lista 
ordenada de sus elementos. Esto es útil si se necesita un orden 
específico para presentar o procesar los datos, ya que los conjuntos,
por naturaleza, no mantienen un orden.
'''
# Ejercicio 2.20 
'''
Para la construcción de una aplicación de notas 
escolares es necesario crear una base de datos con 
los nombres de los estudiantes y la nota obtenida en 
un curso. Para almacenar los datos se le ha pedido 
que cree un diccionario donde las claves sean los 
nombres de los estudiantes y los valores sean las 
notas obtenidas. Tenga en cuenta los datos 
presentados en la siguiente tabla: 
Nombre de 
estudiante Nota asignada 
Liliana        4.5 
Carmen         3.3 
Josefina       4.1 
Daniela        4.9 
Pedro          2.9 
José           4.6 
Mario          3.3 
Tabla resumen de datos 
Para efectos de desarrollar los siguientes ejercicios 
se definirá el diccionario como calificaciones. Una 
vez creado compruebe el tipo de objeto que queda 
almacenado en la variable calificaciones. Utilice 
para esto la función type.
''' 
calificaciones = {
    "Liliana": 4.5,
    "Carmen": 3.3,
    "Josefina": 4.1,
    "Daniela": 4.9,
    "Pedro": 2.9,
    "José": 4.6,
    "Mario": 3.3
}
print(type(calificaciones))  # Resultado: <class 'dict'>
'''
Interpretación: El tipo de objeto que se almacena en calificaciones es un dict  
(diccionario en Python), que permite asociar claves únicas 
(nombres) con valores (notas).
'''
# Ejercicio 2.21 
'''
Aplique la función sorted sobre el 
diccionario calificaciones. Discuta la 
necesidad de usar esta función en el 
diccionario analizado. 
'''
claves_ordenadas = sorted(calificaciones)
print(claves_ordenadas)  # Resultado: Lista de las claves ordenadas alfabéticamente
'''
Interpretación: La función sorted devuelve una lista de las claves del 
diccionario, ordenadas alfabéticamente. Es útil si necesitas procesar 
o mostrar los datos en un orden específico
'''
# Ejercicio 2.22 
'''
Parece ser que el método pop 
permite eliminar un elemento de un 
diccionario. Ejecute la siguiente 
instrucción: 
>>> 
calificaciones.popitem({'Daniela': 
4.9}) 
¿Qué interpretación se le puede dar 
al mensaje de error que nos entrega 
el intérprete cuando ejecutamos?: 
TypeError: popitem() takes 
no arguments (1 given) 
¿Cuándo es conveniente aplicar este 
método? 
'''
# calificaciones.popitem({"Daniela": 4.9}) #TypeError: popitem() takes no arguments (1 given)
'''
Interpretación: El método  no toma argumentos. Solo elimina 
y devuelve el último par clave-valor del diccionario,
respetando el orden de inserción (a partir de Python 3.7).
Uso apropiado: Este método es útil si deseas eliminar 
el último elemento agregado al diccionario.
'''
# Ejercicio 2.23 
'''
Utilice el método ítems sobre el 
diccionario. ¿qué retorna este 
método?, ¿qué tipo de estructura de 
datos parece, una lista?, una lista de 
listas?, ¿una lista de tuplas?. 
Investigue para más información 
sobre los objetos de tipo dict_items. 
'''
items = calificaciones.items()
print(items)  # Resultado: dict_items([('Liliana', 4.5), ('Carmen', 3.3), ...])
'''
Interpretacion: 
Este objeto parece ser una lista de tuplas, donde cada tupla representa 
un par clave-valor del diccionario.
El método  devuelve un objeto de tipo , que es una vista del diccionario.
Adicional
Los objetos dict_items son iterables y eficientes para recorrer las claves y valores del diccionario.
'''
# Ejercicio 2.24 
'''
Sobre el diccionario calificaciones 
aplique el método update verificando 
los argumentos necesarios para el 
correcto funcionamiento si se quiere 
modificar la nota asignada a la estudiante
Liliana a un valor de 4.7.
'''
calificaciones.update({"Liliana": 4.7})
print(calificaciones)
# Resultado: {'Liliana': 4.7, 'Carmen': 3.3, ...}
'''
El método update toma un diccionario como argumento.
En este caso, se proporciona un diccionario con la clave "Liliana" y el nuevo valor 4.7. 
Esto modifica directamente la nota de Liliana
'''