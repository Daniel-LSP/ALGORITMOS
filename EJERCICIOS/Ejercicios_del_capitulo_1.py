#Ejercicio 1.1  
'''
Escriba un programa que defina inicialmente x=4, 
utilice la función input para capturar del usuario un 
valor y. Calcule con x y con y la suma de los valores 
y guárdelo en una variable z. Al ejecutar, el 
programa debe entregar un print con el siguiente 
texto: “El resultado es: “, y el valor resultante de z.
'''

# x = 4  #Definir x
# y = int(input("Introduce un valor para y: "))  #Capturar y
# z = x + y  #Calcular la suma y guardarla en z
# print("El resultado es:", z)  #Mostrar el resultado

# Ejercicio 1.2 
'''
Escriba un programa que defina inicialmente x=4, 
utilice la función input para capturar del usuario un 
valor y. Calcule con x y con y la resta de los valores 
y guárdelo en una variable z. Al ejecutar, el 
programa debe entregar un print con el siguiente 
texto: “El resultado de la resta es: “, y el valor 
resultante de z.
'''
# x = 4  #Definir x
# y = int(input("Introduce un valor para y: "))  #Capturar y
# z = x - y  #Calcular la resta y guardarla en z
# print("El resultado de la resta es:", z)  #Mostrar el resultado

#Ejercicio 1.3 
'''
Escriba un programa que defina inicialmente x=8, 
utilice la función input para capturar del usuario un 
valor y. Calcule con x y con y la división de los 
valores y guárdelo en una variable z. Al ejecutar, el 
programa debe entregar un print con el siguiente 
texto: “El resultado es: “, y el valor resultante de z. 
'''
# x = 8  #Definir x
# y = float(input("Introduce un valor para y: ")) #Capturar y

# #Calcular la división, manejando el caso de división por cero
# if y != 0:
#     z = x / y
#     print("El resultado es:", z)  #Mostrar el resultado
# else:
#     print("Error: no se puede dividir entre cero.")

#Ejercicio 1.4 
'''
Escriba un programa que capture del usuario dos 
valores a y b en dos inputs sucesivos. Pida al 
usuario desde la función input que los valores a 
ingresar deben contener al menos un número 
decimal.  Al ejecutar, el programa debe realizar la 
multiplicación entre los dos valores y entregar la 
respuesta en un formatted string que contenga 
una variable llamada resultado y el texto de su 
preferencia.
'''

# # Capturar los valores a y b como decimales
# a = float(input("Introduce un valor para a (debe contener al menos un número decimal): "))
# b = float(input("Introduce un valor para b (debe contener al menos un número decimal): "))

# #Realizar la multiplicación
# resultado = a * b

# #Mostrar el resultado en un formatted string
# print(f"El resultado de la multiplicación es: {resultado}")

#Ejercicio 1.5 
'''
Escriba un programa que realice la comprobación 
de la división. Recuerde:  
Divisor * Cociente + Residuo = Dividendo 
Tome como entrada dos números, realice la 
división entre ellos y entregue al usuario un texto 
descriptivo con la comprobación de la división. '
'''
# dividendo=int(input("Ingrese el primer numero"))
# divisor=int(input("Ingrese el segundo numero"))

# #calculos
# cociente=dividendo/divisor
# residuo=dividendo%divisor

# print(f"La comprobacion de la division es: {divisor} por {cociente} mas {residuo} es igual a {dividendo}")

#Ejercicio 1.6 
'''
Teniendo en cuenta el ejercicio anterior calcule el 
residuo con el símbolo de módulo % y entregue la 
comprobación con los valores resultantes de dividir 
dos números entregados por el usuario del 
programa. 
'''
#Capturar los valores
# a = int(input("Introduce el dividendo (a): "))
# b = int(input("Introduce el divisor (b): "))

# #Comprobar que el divisor no sea 0
# if b != 0:
#     # Calcular cociente y residuo
#     cociente = a // b
#     residuo = a % b

#     #Verificar la fórmula
#     comprobacion = (b * cociente) + residuo

# #Mostrar resultados
#     print(f"Dividendo: {a}, Divisor: {b}")
#     print(f"Cociente: {cociente}, Residuo: {residuo}")
#     print(f"Comprobación: {b} * {cociente} + {residuo} = {comprobacion}")
#     if comprobacion == a:
#         print("La comprobación es correcta.")
#     else:
#         print("La comprobación es incorrecta.")
# else:
#     print("Error: El divisor no puede ser cero.")

#Ejercicio 1.7 
'''
Compruebe en un programa si el valor 29.0 es igual 
a 
29 utilizando el operador de comparación 
correspondiente. 
'''
# # Definir los valores
# valor1 = 29.0
# valor2 = 29

# # Comprobar si son iguales
# es_igual = valor1 == valor2

# # Mostrar el resultado
# print(f"¿29.0 es igual a 29? {es_igual}")

#Ejercicio 1.8
'''
Compruebe en un programa si la expresión “true” 
es igual a “True” mediante el operador de 
comparación correspondiente. 
'''
# Definir las dos expresiones
# expresion1 = "true"
# expresion2 = "True"

# # Comparar las expresiones
# son_iguales = expresion1 == expresion2

# # Mostrar el resultado
# print(f"¿La expresión \"true\" es igual a \"True\"? {son_iguales}")

#Ejercicio 1.9
'''
Compruebe mediante el operador de identidad 
correspondiente si la letra w se encuentra en la 
expresión “Python es un lenguaje de programación 
muy popular”. Utilice un input para consultar lo 
mismo y comprobar según la entrada que dé el 
usuario. 
'''

# # Definir el texto principal
# texto = "Python es un lenguaje de programación muy popular"

# # Comprobar si la letra 'w' está en el texto
# letra_w = 'w' in texto
# print(f"¿La letra 'w' está en el texto? {letra_w}")

# #Solicitar entrada del usuario
# entrada_usuario = input("Introduce un carácter o palabra para comprobar si está en el texto: ")

# # Verificar si la entrada del usuario está en el texto
# encontrado = entrada_usuario in texto
# print(f"¿Tu entrada ('{entrada_usuario}') está en el texto? {encontrado}")

