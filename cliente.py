import threading
import time

class Cliente(threading.Thread):
    
    def __init__(self, id, x_origen, y_origen, x_destino, y_destino, empresa):
        super().__init__()
        self.id = id
        self.x_origen = x_origen
        self.y_origen = y_origen
        self.x_destino = x_destino
        self.y_destino = y_destino
        self.empresa = empresa
    
    def __str__(self):
        return f"Cliente {self.id} de origen: {self.x_origen}, {self.y_origen} quiere ir a {self.x_destino}, {self.y_destino}"

    def run(self):
        time.sleep(3)
        self.empresa.asignar_taxi(self)