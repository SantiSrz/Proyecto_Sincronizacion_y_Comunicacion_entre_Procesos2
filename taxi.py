import threading
import time
import math

class Taxi(threading.Thread):
    
    def __init__(self, id, matricula, x, y, empresa):
        super().__init__()
        self.id = id
        self.matricula = matricula
        self.x = x
        self.y = y
        self.ocupado = False
        self.candado = threading.Lock()    
        self.cliente_actual = None
        self.recaudado = 0
        self.empresa = empresa
            
    def __str__(self):
        return f"Taxi {self.id} cuya matricula es: {self.matricula}, esta en {self.x}, {self.y} y se dirige a recoger a un cliente"
    
    def run(self):
        while True:
            if self.ocupado == True:
                print(f"Taxi {self.id} yendo a recoger a {self.cliente_actual.id}")
                time.sleep(3)
                print(f"Cliente {self.cliente_actual.id} ya recogido por el taxi {self.id}")
                time.sleep(3)
                distancia_recorrida = math.sqrt((self.cliente_actual.x_destino - self.cliente_actual.x_origen)**2 + (self.cliente_actual.y_destino - self.cliente_actual.y_origen)**2)
                precio = distancia_recorrida * 0.5
                self.recaudado += precio
                print(f"Cliente {self.cliente_actual.id} ha sido entregado en su destino por el taxi {self.id}")
                print(f"El cliente {self.cliente_actual.id} ha pagado {precio:.2f} al taxi {self.id}")
                self.candado.acquire() 
                try:
                    self.x = self.cliente_actual.x_destino
                    self.y = self.cliente_actual.y_destino
                    self.empresa.almacenar_viaje(self.id, self.cliente_actual.id, precio)
                    self.ocupado = False
                    self.cliente_actual = None
                    print(f"Taxi {self.id} vuelve a estar libre.")
                finally:
                    self.candado.release()
                    
            else:
                print(f"Taxi {self.id} esperando a un cliente en [{self.x}, {self.y}]")
                time.sleep(3)
            
    def intentar_ocupar(self, cliente):
        self.candado.acquire()
        try:
            if self.ocupado == False:
                self.ocupado = True
                self.cliente_actual = cliente
                return True
            else:
                return False
        finally:
            self.candado.release()