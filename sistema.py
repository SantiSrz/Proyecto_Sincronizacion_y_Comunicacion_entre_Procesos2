import math
import random

class Sistema:

    def __init__(self):
        self.taxis = []
        self.clientes = []
        self.historial_de_registros = []

    def registrar_taxi(self, taxi):
        if self.taxi_antecedentes == False:
            self.taxis.append(taxi)
        else:
            print(f"El taxista {taxi.id} no puede trabajar aqui debido a sus antecedentes penales")
            self.escribir_log(f"El taxista {taxi.id} no ha sido rechazado debido a sus antecedentes penales")
        
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
                print(f"Todo lo que ha recaudado el taxi {t.id}: {t.recaudado}. UNIETAXI se lleva: {comision:.2f} y taxista: {pago_taxista:.2f}")
                self.escribir_log(f"Todo lo que ha recaudado el taxi {t.id}: {t.recaudado}. UNIETAXI se lleva: {comision:.2f} y taxista: {pago_taxista:.2f}")
                t.recaudado = 0
                
    def almacenar_viaje(self, taxi_id, cliente_id, precio):
        datos = {"Taxi":taxi_id,
                 "Cliente":cliente_id,
                 "Precio":f"{precio:.2f}"}
        self.escribir_log(f"El taxi {taxi_id}, llevo al cliente {cliente_id} por {precio:.2f} euros")
        self.historial_de_registros.append(datos)
        
    def reporte_calidad(self):
        total_viajes = len(self.historial_de_registros)
        if total_viajes > 0:
            cantidad_a_revisar = min(5, total_viajes)
            auditoria_random = random.sample(self.historial_de_registros, cantidad_a_revisar)
            for viaje in auditoria_random: 
                print(f"Auditorias de hoy:")
                print(viaje)
        else:
            print("No hay viajes para auditorias hoy.")
            return
        
    def escribir_log(self, mensaje):
        with open("bitacora.txt", "a") as archivo:
            archivo.write(mensaje + "\n")