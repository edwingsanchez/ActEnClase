
#Funciones basicas de mate
def SUMA (num1, num2):
    resultado=num1+num2
    return resultado

def RESTA (num1, num2):
    Resultado= num1-num2
    return Resultado

def MULTIPLICACION (num1, num2):
    Resultado=num1*num2
    return Resultado

def DIVISION (num1, num2):
    resultado = num1/num2
    return resultado

#Usar funciones
print(SUMA(5, 6))

print(MULTIPLICACION(5, 5))

print(RESTA(5, 3))

print(DIVISION(10, 5))


#Tablas de multiplicar
def Tabla(num):
    tabla1=num*1, num*2, num*3, num*4, num*5, num*6, num*7, num*8, num*9, num*10
    return tabla1

#Usar la fncion de tabla de multiplicar 
print("Tabla de:", Tabla(1))






#Funcion Cadenad
def SALUDAR(nombre):
    miope= ("Hola", nombre, "en que te puedo ayudar hoy?")
    return miope
SALUDAR()

print(SALUDAR("Mauricio"))

#Funcion cadenas con input
def SALUDAR2():
    nombre = input("Como te llamas?: ")
    print(f"Hola, {nombre}!")
SALUDAR()

#Usar la funcion de input
Pregunta=input("Te presento a un amigo?")
if Pregunta=="si":
    SALUDAR2("Daniela")
elif Pregunta=="no":
    sgura = input("segura?: ")
    if sgura== "Si":
        print("Ah ok")
    elif sgura== "No":
        print("Por")