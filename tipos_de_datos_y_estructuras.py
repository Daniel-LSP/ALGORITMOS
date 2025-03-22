'''
<class 'init'>: Identifica que la variable es un entero 
<class 'float: Identifica que la variable es un numero decimal
<class 'str: Identifica que la variable es una cadena de texto
<class 'bool: Identifica que la variable es un valor True o False (boolean)

'''

# x=True #True y False son palabras reservadas del lenguaje
# print(type(x))

# autor='andres'
# print(type(autor))

# carro="This is Lewin'car: "
# modelo='1999'
# print(carro + modelo) #el simbolo + permite concatenar textos en python

# '''
# TIPOS DE ESTRUCTURAS DE DATOS Y METODOS
# 1. Conjuntos +
# 2.Tuplas ++
# 3. Listas +++
# 4. Diccionarios ++

# '''

# #Uso de conjuntos 
# '''
# Los sets o conjuntos son estrucuturas especiales que nos ayudan a almacenar
# un grupo de elementos. Cuando el orden de los elementos no es relevante 
# podemos utilizar sets en Python.
# Ademas esta estructura no permite elementos duplicados 
# como se definen: {, , , , ,}

# '''
set1={"a", "b", 'c', 'd'}
print(type(set1))

set2={"e", 'f', "g"}

#metodos para el tratamiento de conjuntos
set1.union()
#union de conjunto
# print(set1.union(set2))

set3={"a", "b", "c", "c", "d", "d"}
print(set3)

set4=set3.union(set1)
print(set4)

# #Interseccion de conjuntos con python
set5={"f", "w", "a", "b"}
print(set5.intersection(set1))

set5.remove("w")
print(set5)

set4.add("a")
print(set4)

set4.discard("a")
print(set4)

print(set4.issuperset(set5))

set6={"andres", 5, True}
set7={"andres", 5, True, "daniel"}
# print(set6.issuperset(set7)) #False
# print(set7.issuperset(set6)) #True

# print(set6.issubset(set7)) #True
# print(set7.issubset(set6)) #False

'''
Uso de Tuplas
Son estructuras de datos rigidas, que no permiten muchos metodos 
se usan cuando queremos resguardar la informacion (inmutable)
como se definen: (, , , , ,)
si permiten valores duplicados
<class 'tuple'>
'''
# tupla1=(1, 1, 1, 3, 4, 5)
# print(type(tupla1))

# #metodos
# #count
# conteo=tupla1.count(1)
# print(conteo)

# #index
# indice=tupla1.index(1)
# print(indice)

'''
PYTHON ES UN LENGUAJE INDEXEADO EN CERO 
siempre el primer elemento en una estructura de datos tiene
el indice 0, en otras palabras, la posicion inicial siempre es 0
indice <===> posicion
'''
'''
USO DE LISTAS
Las listas en Python son estructuras de datos que almacenan 
elementos de manera ordenada y mutable.
Son un tipo de dato nativo del lenguaje de programacion Python.
como se definen: [, , , ,]
si permiten valores duplicados 
<class 'list'>
pueden contener cualquier tipo de dato,
numero, letras, o incluso otras listas
'''
lista1=[8, 9, 7, 5, 4, 10]
print(type(lista1))

lista2=[["jhon", "alejandro", "lewin",], ["Isabel", "Juan", "Daniel"]]
print(type(lista2)) #<class 'list'>

#metodos
lista2.reverse()
print(lista2)

lista1.append("andres")
print(lista1)

#acceder a los elementos de la lista
lista2=[["jhon", "alejandro", "lewin",], ["Isabel", "Juan", "Daniel"]]
print(lista2[0][2],["jhon"])