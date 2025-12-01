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
            if (distancia_actual < mejor_distancia) and (t.ocupado == False):
                taxi_mas_cercano = t  
                mejor_distancia = distancia_actual
                
        if taxi_mas_cercano is not None:
            if taxi_mas_cercano.intentar_ocupar(cliente) == True:
                return taxi_mas_cercano
            else:
                return None
            
    def cierre_contable(self):
        for t in self.taxis:
            if t.recaudado > 0:
                comision = t.recaudado * 0.20
                pago_taxista = t.recaudado * 0.80
                print(f"Todo lo que ha recaudado el taxi {t.id}: {t.recaudado}. UNIETAXI se lleva: {comision} y taxista: {pago_taxista}")
                t.recaudado = 0