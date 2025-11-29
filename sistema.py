from taxi import Taxi
from cliente import Cliente
import threading
import time
import math

class Sistema:

    def __init__(self):
        self.taxis = []
        self.clientes = []

    def registrar_taxi(self, taxi):
        self.taxis.append(taxi)
        
    def registrar_clientes(self, cliente):
        self.clientes.append(cliente)
        
    def calcular_distancia(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def asignar_taxi(self, cliente):
        mejor_distancia = 2000
        taxi_mas_cercano = None
        
        for t in self.taxis:
            distancia_actual = self.calcular_distancia(t.x, t.y, cliente.x_origen, cliente.y_origen)
            if distancia_actual < mejor_distancia:
                taxi_mas_cercano = t      
        return taxi_mas_cercano