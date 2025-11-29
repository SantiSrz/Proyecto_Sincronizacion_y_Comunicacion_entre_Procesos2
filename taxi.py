import threading
import time

class Taxi(threading.Thread):
    
    def __init__(self, id, matricula, x, y):
        super().__init__()
        self.id = id
        self.matricula = matricula
        self.x = x
        self.y = y
        
    def __str__(self):
        return f"Taxi {self.id} cuya matricula es: {self.matricula}, esta en {self.x}, {self.y}"
    
    
    def run(self):
        while True:
            print(f"El taxi {self.id} esta esperando")
            time.sleep(3)