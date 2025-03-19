# Autor: Lewin Daniel 
# Este es un comentario de una sola linea 
'''
Este es un comentario de 
multiples 
lineas

'''

print("Estudiando python")
#Definicion de variables 
'''
Reglas: 
Python es sensible a minusculas y mayusculas
No se pueden usar espacios
No se pueden usar palabras reservadas
No es conveniente usar numeros como nombres de variables

'''
x=50
y=15
print(x+y)  
print(type(x))
# <class 'int'> : significa que x es un numero entero
#--
nombre="Andres"
print(nombre)
print(type(nombre))
#<class 'str'> : significa que la variable nombre es un string (cadena)

print(type(x))
x=4.8
print(type(x))
#<class 'float'> : significa que la variable es un flotante (numero decimal)

print(x , nombre)



#Variables 

my_string_variable = "My string variable"
print(my_string_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de varaibles en un print 
print(my_string_variable, my_int_variable, my_bool_variable)
print("Ese es el valor de:", my_bool_variable)

# Algunas funciones del sistema
print(len(my_string_variable))

# Variables en una sola linea
name, surname, alias, age = "Lewin", "Daniel", "Flash", 18
print("Me llamo:", name, surname, ".Mi edad es:", age, ".Y mi alias es:", alias)

#Inputs
"""

name = input('¿Cual es tu nombre? ')
age = input('¿Cuantos años tienes? ')
print(name)
print(age)

"""
#Cambiamos su tipo
name = 18
age = "Lewin"
print(name)
print(age)

### Operadores ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 2)
print(10 // 3)
print(2 ** 3)
print("Hola" +" ""Python")
print("Hola" == "python")
print("Hola" < "Python")
print("Hola" > "Python")
print("Hola" >= "Python")
print("Hola" * 5)
print("Hola" + str(5))











