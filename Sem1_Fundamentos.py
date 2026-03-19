#1. Print
print("Hola mundo")

#2. IF, ELIF, OR y ELSE
Ib=345
#If se usa cuando se evalua una condicion como verdadera o falsa dentro de una variable.
if Ib>34 or Ib<500:
    #Or: Esta se usa cuando se evaluan dos condiciones para ejecutar la mismas intrucciones puede ser en la misma linea de conandos
    print("Wayoming")
elif Ib=="hawoplay":
    print("wayomingNomberTu")
else:
    #Else estas intrucciones se ejecutan cuando todas las de arriba resultan falsas pero no evaluan ninguna condicion.
    print("AAAAAAII NID TO KNOW NOW.")
    





#3. FUNCIONES
#En los parametros de la funcion podemos poner variables y dentro de la funcion una operacion y
#cuando llamemos a la funcion podemos darle el valor a las variables para que se ejecute la operacion de antes.

#Ponemos cuantos variables son y adentro el tipo de operacion que queremos que se ejectute
def media(num1, num2, num3):
    resultado=num1+num2+num3
    resultado=resultado/3
    return resultado

#Print porque hemos puesto return y le damos valor a las variables para que ejecute la operacion.
print(media(34, 439, 43))


#Ejercicios
def Multiplicacion (num4, num5):
    mul=num4*num5
    return mul

    print(Multiplicacion(5, 5))







#4. ESTRUCTURAS DE DATOS INTEGRADOS

#4.2 LISTAS
#mutables
#Las listas se usan con corchetes.

Lista = [29, True, 3.1415, "El numero que avogabro si que mola"]

#se puede acceder a la lista con los corchetes en el print
print (Lista[2])

#Cambiar posiciones
Lista[2]= "He cambiado este elemento"

#Puedes colocar un elemento al final de la lista
Lista.append('objeto')

#Se pueden imprimir sublistas
print (Lista[2:4])

#Nos dice cuanto se repite un elemento
print (Lista.count(3))

#Lo siguiente nos dice cuando es la primera aparicion de un elemento
print (Lista.index(4))

print (Lista.remove(3))




    #4.3 TUPLAS
#Ordenada (Posicion 1, posicion 2, poiscion 3)
#Heterogenea (1, 1.5, "meschii")
#No mutables, no se pueden modificar
#Parentesis en lugar de corchetes

Tupla = ("La tierra es plana", True, False, True)

#Imprimir un valor de alguna posicion:
print(Tupla[1]) 

#Metodo count:
print(Tupla.count[True])

#Metodo index:
print(Tupla.index[True])
print(Tupla.index[False])

print(())



    #4.4 CONJUNTOS
#No ordenados (no se puede pedir cualquier valor que este en el conjunto)
#Heterogeneos (Diferentes tipos de variables)
#Mutables

#Se usa set para crear un conjunto
print(set([5, 2, 5, 1, 1.5]))
print(set((5, 2, 5, 1, 1.5)))
print(set("52511.5"))

#Uno de sus usos es eliminar elementos repetidos de una secuencia
conjunto = set([2, 3, 3, 4])
print(conjunto)

#A;adir  y elemento:
conjunto.add(1)
print(conjunto)

conjunto.remove(1)
print (conjunto)


#Operaciones con conjuntos
conjunto_uno=  set(1, 2, 3, 4, 5)
conjunto_dos=  set(4, 3, 3, 3)
print(conjunto_uno, conjunto_dos)

#Que valor tienen en comun
print (conjunto_uno.intersection(conjunto_dos))

print (conjunto_uno & conjunto_dos)




    #4.5 DICCIONARIOS
#Heterogeno, inmutable.
Diccionario_1 = {1: "uno", 2: "value"}

Diccionario_1 [3]= 'Tres'

#Puedes ver el value de una key con unos corchetes
print (Diccionario_1[1])

#Segunda forma de crear un diccionario
dict_lista_tuplas= dict([(1, "uno") (2, "dos")(3, "Tres")])
print(dict_lista_tuplas)

dict_lista_string= dict(Uno =1, Dos=2)
print(dict_lista_string)

dict_tipos= {1: "integrer", 2.2: "float", "texto": "string", (1, 2): "tupla"}
print(dict_tipos)

dict_repeticion = {1: "primero", 2: "segundo"}
print(dict_repeticion)

print(Diccionario_1, Diccionario_1.keys(), Diccionario_1.values(), Diccionario_1.items())

claves= Diccionario_1.values()
print(claves)

#Cambiar el valor de una key
Diccionario_1[1] = "one"
print(claves)

#podemos eliminar una key con el metodo pop
Diccionario_1.pop(2)
print(Diccionario_1)
