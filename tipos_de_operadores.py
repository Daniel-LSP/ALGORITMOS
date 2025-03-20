'''
Operadores aritmeticos 

'''

# Suma 
# x=2+6
# print(x)

# Resta 
# y=8-2
# print(y)

# Multiplicacion
# print(2*25)

#Division
''' para python la divsion siempre retorna un float'''
# divide=25/5
# print(divide)
# print(type(divide))

#Division piso (floor)
''' la division piso me devuelve el numero entero mas proximo hacia abajo '''
# print(10/3)
# print(10//3)

# print(4/3)
# print(4//3)

# print(14.5/3)
# print(14.5//3)

'''Prueba realizar la division piso 8//-3 y 
comparala con la division tradicional 8/-3'''
# print(8/-3)
# print(8//-3)

#Modulo
'''el resultado de % (modulo) es el residuo '''
# w=20/3
# y=20%3

# print(w)
# print(y)

# print(type(y))

#Potencia 
# print(2**3)

'''Operadores de comparacion
Este tipo de operadores los usamos cuando 
deseamos comparar expresiones o variables. 
Python evalua si se cumple la comparacion
y nos devuelve (retorna) un valor True o False '''

#Es igual a
# print("x"=="x")

# print(3==3.0)
# print(3==3.00000)
# print(3==3.0000000000001)

# x = 4.123456789000001058946546
# y =  4.123456789000001
# print (x == y)

#es diferente a
# print(4 != 3)
# print(False != True)

#es mayor que
# print(5 > 8)

#es menor que
# print(5 < 8)

# <=
# >=


'''Operadores de asignacion'''
# x=20
# x=20 + 1
# print(x)

# incremento
#+=
# print(x++2)

#decrecimiento
# y=5
# y=y-1
# y-=1
# print(y)

'''operadores logicos
and: exige que todas las condiciones sean True para responder True, de lo contrario responde false
or: este operador solo necesia que algunas de las condiciones sea true para responder  true
not
'''
x=4#Defino el valor de la variable x
# x==4#preguntando si x es igual a 4
y=4
# print(x==4 and y==8)

#uso el operador or
print(x==100 or y==4)

#uso del operador not
'''
En el caso del operador not es valida si una variable es false o true 
si la variable existe en memoria tenemos un valor por defecto true
'''
print(not x)