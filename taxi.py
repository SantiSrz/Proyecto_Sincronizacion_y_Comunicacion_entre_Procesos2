import threading
import time

class Taxi(threading.Thread):
    
    def __init__(self, id, matricula, x, y, ocupado = False):
        super().__init__()
        self.id = id
        self.matricula = matricula
        self.x = x
        self.y = y
        self.ocupado = ocupado
        self.candado = threading.Lock()    
            
    def __str__(self):
        return f"Taxi {self.id} cuya matricula es: {self.matricula}, esta en {self.x}, {self.y} y se dirige a recoger a un cliente"
    
    def run(self):
        while True:
            if self.ocupado == True:
                print(f"Taxi {self.id} en camino")
            else:
                print(f"Taxi {self.id} esperando")
            time.sleep(3)
            
    def intentar_ocupar(self):
        self.candado.acquire()
        try:
            if self.ocupado == False:
                self.ocupado = True
                return True
            else:
                return False
        finally:
            self.candado.release()