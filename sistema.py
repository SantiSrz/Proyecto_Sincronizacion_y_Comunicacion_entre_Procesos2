import math # importo la libreria math para hacer operaciones como una raiz cuadrada
import random # importo la libreria random para poder obtener valores aleatorios donde lo necesite

# creo un clase llamada Sistema
class Sistema:

    # en el metodo constructor creo las listas donde se guardaran los taxis y clientes
    def __init__(self):
        self.taxis = []
        self.clientes = []
        self.historial_de_registros = []

    # este es el metodo por el cual se registran los taxis
    def registrar_taxi(self, taxi):
        # si el taxi no tiene antecendentes penales se añade a la lista
        if taxi.antecedentes_penales == False:
            self.taxis.append(taxi)
        # si si ha tenido antecedentes penales se printea un mensaje diciendo que no ha podido ser registrado y se añade un mensaje en el archivo .txt para que quede registrado y se detiene el servicio de ese taxi
        else:
            print(f"El taxista {taxi.id} no puede trabajar aqui debido a sus antecedentes penales")
            self.escribir_log(f"El taxista {taxi.id} ha sido rechazado debido a sus antecedentes penales")
            taxi.detener_servicio()
            
    # este es el metodo por el cual se registran los clientes
    def registrar_clientes(self, cliente):
        self.clientes.append(cliente)
    
    # este el el metodo donde se calcula la distancia con una formula global diseñada para calcular la distancia entre dos cosas y en la que uso la libreria math
    def calcular_distancia(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # este es el metodo utilizado para asignar taxis a los clientes en base a ciertas cosas
    def asignar_taxi(self, cliente):
        
        # se dan unos valores iniciales a estas variables (doy 2000 porque el limite de distancia de la aplicacion son 2km)
        mejor_distancia = 2000
        taxi_mas_cercano = None
        mejor_calificacion = -1
        
        # hago un for para asignar el taxi mas cercano y con mejor valoracion al cliente
        for t in self.taxis:
            
            # este if es para calcular la media de la calificacion que tenga el taxista
            if t.conteo_viajes == 0:
                media_actual = 0
            else:
                media_actual = t.total_estrellas / t.conteo_viajes
            
            # aqui calculo la distancia entre el cliente y el taxi llamando a la funcion anterior donde aplicaba la formula
            distancia_actual = self.calcular_distancia(t.x, t.y, cliente.x_origen, cliente.y_origen)
            
            # aqui digo que si la distancia de ese taxi es mas cercana que la mejor distancia que este guardada en la variable mejor_distancia se actualiza ese taxi como el mejor candidato para el viaje, lo mismo con la calificacion
            if (distancia_actual < mejor_distancia) and (t.ocupado == False):
                taxi_mas_cercano = t  
                mejor_distancia = distancia_actual
                mejor_calificacion = media_actual
            
            # aqui es el caso en el que dos taxis esten a la misma distancia que un cliente, el cliente se le otorga al que mejor calificacion tenga
            elif (distancia_actual == mejor_distancia) and (t.ocupado == False):
                if media_actual > mejor_calificacion:
                    taxi_mas_cercano = t
                    mejor_calificacion = media_actual
                    
        # esta funcion primero verifica si hay algun taxi candidato y luego verifica si ese taxi puede ser otorgado a un cliente ya que alomejor ya esta usandose y esta el candado cerrado 
        if taxi_mas_cercano is not None:
            if taxi_mas_cercano.intentar_ocupar(cliente) == True:
                return taxi_mas_cercano
            else:
                return None
        else:
            return None
        
    # este metodo sirve para que calcular cuanto se lleva el taxista y cuanto la empresa UNIETAXI al final del dia, luego se printea y se guarda en el archvio .txt 
    def cierre_contable(self):
        print(f"\n")
        for t in self.taxis:
            if t.recaudado > 0:
                comision = (t.recaudado * 0.20)
                pago_taxista = t.recaudado * 0.80
                print(f"Todo lo que ha recaudado el taxi {t.id}: {t.recaudado:.2f}. UNIETAXI se lleva: {comision:.2f} y taxista: {pago_taxista:.2f}")
                self.escribir_log(f"Todo lo que ha recaudado el taxi {t.id}: {t.recaudado:.2f}. UNIETAXI se lleva: {comision:.2f} y taxista: {pago_taxista:.2f}")
                t.recaudado = 0

    # este metodo sirve para almacenar todos los viajes y sus datos en una lista llena de diccionarios, tambien se guarda en el archivo .txt
    def almacenar_viaje(self, taxi_id, cliente_id, precio, media):
        datos = {"Taxi":taxi_id,
                 "Cliente":cliente_id,
                 "Precio":f"{precio:.2f}",
                 "Media de califiacion:":f"{media:.2f}"}
        self.escribir_log(f"El taxi {taxi_id}, llevo al cliente {cliente_id} por {precio:.2f} euros. Calificacion media del taxista: {media:.2f} estrellas")
        self.historial_de_registros.append(datos)
    
    # este el el metodo que hace las 5 auditorias aleatorias
    def reporte_calidad(self):
        total_viajes = len(self.historial_de_registros)
        # para hacer las auditorias hay que comprobar que haya algun viaje primero
        if total_viajes > 0:
            cantidad_a_revisar = min(5, total_viajes)  # aqui lo que se hace es coger 5
            auditoria_random = random.sample(self.historial_de_registros, cantidad_a_revisar) # esto coge 5 aleatorios
            # printeo un mensaje y voy enseñando los 5 viajes con un for
            print(f"\nAuditorias de 5 viajes aleatorios de hoy:")
            for viaje in auditoria_random: 
                print(f"{viaje}")
        else:
            print("No hay viajes para auditorias hoy.")
            return
    
    # este es el metodo que crea el archvio .txt y cuando se le llama va añadiendo lo que se le diga al archivo
    def escribir_log(self, mensaje):
        with open("Datos.txt", "a") as archivo:
            archivo.write(mensaje + "\n")