import threading
import time
import math
from cliente import Cliente

class Taxi:
    
    def __init__(self, id, matricula, x, y):
        self.id = id
        self.matricula = matricula
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Taxi {self.id} cuya matricula es: {self.matricula}, esta en {self.x}, {self.y}"
    