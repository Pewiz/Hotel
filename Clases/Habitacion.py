import csv
import random

#La capacidad se va a ir restando de acuerdo al tamaño de la mascota
# -MuyPequeño= capacidad-1
# -Pequeño = capacidad-2
# -Mediano = capacidad-3
# -Grande = capacidad-4
# -MuyGrande = capacidad-5


class Habitacion:
    def __init__(self, id, capacidad, separada, precioBase):
        self.__id=id
        self.__capacidad=capacidad
        self.__separada=separada
        self.__precioBase= precioBase
    
    #Getters
    def get_id(self):
        return self.__id

    def get_capacidad(self):
        return self.__capacidad

    def get_separada(self):
        return self.__separada

    def get_precio_base(self):
        return self.__precioBase
    
    #Setters
    def set_id(self, id):
        self.__id = id

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad

    def set_separada(self, separada):
        self.__separada = separada

    def set_precio_base(self, precioBase):
        self.__precioBase = precioBase
