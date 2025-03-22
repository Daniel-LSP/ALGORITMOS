#Ejercicio 1.5 
'''
Escriba un programa que realice la comprobación 
de la división. Recuerde:  
Divisor * Cociente + Residuo = Dividendo 
Tome como entrada dos números, realice la 
división entre ellos y entregue al usuario un texto 
descriptivo con la comprobación de la división. '
'''

print(10/2)
print(10//2)
print(float(10/2))
print(int(10/2))

dividendo=int(input("Ingrese el primer numero"))
divisor=int(input("Ingrese el segundo numero"))

#calculos
cociente=dividendo/divisor
residuo=dividendo%divisor

print(f"La comprobacion de la division es: {divisor} por {cociente} mas {residuo} es igual a {dividendo}")

