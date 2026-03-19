#5 POO

#5.1 Abstraccion
class personaje:
    nombre="Deafult"
    fuerza= 0 

mi_personaje = personaje()
print ("El nombre del jugador es", mi_personaje.nombre)
#5.2 Encpasulacion
class Personaje:
    def __init__(self, nombre, fuerza):
        self.__nombre = nombre
        self.__fuerza = fuerza
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_fuerza(self):
        return self.__fuerza
    
    def set_fuerza(self, fuerza):
        if fuerza > 0:
            self.__fuerza = fuerza

personaje = Personaje("Héroe", 10)
print("Nombre:", personaje.get_nombre())
print("Fuerza:", personaje.get_fuerza())

#5.3 Herencia

#5.3 Poliformismo
