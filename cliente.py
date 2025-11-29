import threading
import time
from taxi import Taxi
import math

class Cliente:
    
    def __init__(self, id, x_origen, y_origen, x_destino, y_destino):
        self.id = id
        self.x_origen = x_origen
        self.y_origen = y_origen
        self.x_destino = x_destino
        self.y_destino = y_destino
    
    def __str__(self):
        return f"Cliente {self.id} de origen: {self.x_origen}, {self.y_origen} quiere ir a {self.x_destino}, {self.y_destino}"

