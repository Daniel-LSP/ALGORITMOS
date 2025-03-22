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
# Definir la cadena
cadena = "Python puro"

# Verificar si la letra 'o' es la última usando el método endswith
termina_con_o = cadena.endswith("o")

# Mostrar el resultado
print(f"¿La cadena termina con la letra 'o'? {termina_con_o}")

# Ejercicio 2.5 
'''
Investigue cómo utilizar el método casefold sobre 
la cadena de texto y para qué serviría. 
'''
#METODO CASEFOLD
#Este método se utiliza para realizar comparaciones de texto
#que no distingan entre mayúsculas y minúsculas. Es más potente 
#que  porque maneja mejor ciertos idiomas y caracteres especiales.

# Comparar cadenas ignorando mayúsculas y minúsculas
texto1 = "Python".casefold()
texto2 = "PYTHON".casefold()

# Verificar si son iguales
son_iguales = texto1 == texto2

# Mostrar el resultado
print(f"¿Son iguales? {son_iguales}")

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
letras = ["a", "b", "c", "d", "e"]

# Insertar la letra 'a' en la posición 2
letras.insert(2, "a")

# Contar el número de veces que aparece la letra 'a'
conteo_a = letras.count("a")

# Mostrar la lista y el conteo
print(f"Lista: {letras}")
print(f"Número de veces que aparece la letra 'a': {conteo_a}")

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
letras = ["a", "b", "a", "c", "d", "e"]

# Eliminar la letra 'c' de la posición 3
letra_eliminada = letras.pop(3)

# Mostrar la letra eliminada y la lista actualizada
print(f"Letra eliminada: {letra_eliminada}")
print(f"Lista actualizada: {letras}")

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
# Crear la lista con números en orden aleatorio
valores = [3, 1, 4, 10, 7, 5, 2, 8, 9, 6]

# Ordenar la lista de mayor a menor
valores.sort(reverse=True)
print(f"Lista ordenada de mayor a menor: {valores}")

# Utilizar la función sorted para comparar
valores_sorted = sorted(valores)
print(f"Lista ordenada con sorted: {valores_sorted}")
# Ejercicio 2.9 
'''
Considere la creación de una nueva lista 
llamada duplicada que sea una copia de la 
lista valores. Posteriormente ejecute una 
instrucción para que la copia quede 
ordenada desde los valores más bajos a los 
más altos.
'''
# Crear la lista original
valores = [3, 1, 4, 10, 7, 5, 2, 8, 9, 6]

# Crear una copia de la lista
duplicada = valores.copy()

# Ordenar la copia de menor a mayor
duplicada.sort()
print(f"Lista original: {valores}")
print(f"Lista duplicada y ordenada: {duplicada}")

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
# Crear la tupla con nombre de producto y precio
ventas = ("leche", 5)

# Consultar el índice del precio usando index()
indice_precio = ventas.index(5)
print(f"El índice del precio es: {indice_precio}")

# Intentar modificar el elemento en el índice obtenido
try:
    ventas[indice_precio] = 8  # Esto generará un error
except TypeError as e:
    print(f"Error: {e}")
