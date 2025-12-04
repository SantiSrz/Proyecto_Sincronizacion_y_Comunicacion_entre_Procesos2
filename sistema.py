import math
import random

class Sistema:

    def __init__(self):
        self.taxis = []
        self.clientes = []
        self.historial_de_registros = []

    def registrar_taxi(self, taxi):
        if taxi.antecedentes_penales == False:
            self.taxis.append(taxi)
        else:
            print(f"El taxista {taxi.id} no puede trabajar aqui debido a sus antecedentes penales")
            self.escribir_log(f"El taxista {taxi.id} ha sido rechazado debido a sus antecedentes penales")
            taxi.detener_servicio()
        
    def registrar_clientes(self, cliente):
        self.clientes.append(cliente)
        
    def calcular_distancia(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def asignar_taxi(self, cliente):
        mejor_distancia = 2000
        taxi_mas_cercano = None
        mejor_calificacion = -1
        
        for t in self.taxis:
            if t.conteo_viajes == 0:
                media_actual = 0
            else:
                media_actual = t.total_estrellas / t.conteo_viajes
            
            distancia_actual = self.calcular_distancia(t.x, t.y, cliente.x_origen, cliente.y_origen)
            
            if (distancia_actual < mejor_distancia) and (t.ocupado == False):
                taxi_mas_cercano = t  
                mejor_distancia = distancia_actual
                mejor_calificacion = media_actual
            
            elif (distancia_actual == mejor_distancia) and (t.ocupado == False):
                if media_actual > mejor_calificacion:
                    taxi_mas_cercano = t
                    mejor_calificacion = media_actual
                    
        if taxi_mas_cercano is not None:
            if taxi_mas_cercano.intentar_ocupar(cliente) == True:
                return taxi_mas_cercano
            else:
                return None
        else:
            return None
            
    def cierre_contable(self):
        print(f"\n")
        for t in self.taxis:
            if t.recaudado > 0:
                comision = (t.recaudado * 0.20)
                pago_taxista = t.recaudado * 0.80
                print(f"Todo lo que ha recaudado el taxi {t.id}: {t.recaudado:.2f}. UNIETAXI se lleva: {comision:.2f} y taxista: {pago_taxista:.2f}")
                self.escribir_log(f"Todo lo que ha recaudado el taxi {t.id}: {t.recaudado:.2f}. UNIETAXI se lleva: {comision:.2f} y taxista: {pago_taxista:.2f}")
                t.recaudado = 0
                
    def almacenar_viaje(self, taxi_id, cliente_id, precio, media):
        datos = {"Taxi":taxi_id,
                 "Cliente":cliente_id,
                 "Precio":f"{precio:.2f}",
                 "Media de califiacion:":f"{media:.2f}"}
        self.escribir_log(f"El taxi {taxi_id}, llevo al cliente {cliente_id} por {precio:.2f} euros. Calificacion media del taxista: {media:.2f} estrellas")
        self.historial_de_registros.append(datos)
        
    def reporte_calidad(self):
        total_viajes = len(self.historial_de_registros)
        if total_viajes > 0:
            cantidad_a_revisar = min(5, total_viajes)
            auditoria_random = random.sample(self.historial_de_registros, cantidad_a_revisar)
            print(f"\n Auditorias de 5 viajes aleatorios de hoy:")
            for viaje in auditoria_random: 
                print(f"{viaje}")

        else:
            print("No hay viajes para auditorias hoy.")
            return
        
    def escribir_log(self, mensaje):
        with open("Datos.txt", "a") as archivo:
            archivo.write(mensaje + "\n")