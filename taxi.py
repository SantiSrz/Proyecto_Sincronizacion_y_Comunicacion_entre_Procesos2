import threading # importo la libreria threading para trabajar con hilos
import time # importo la libreria time para poder hacer esperar al programa por x segundos donde lo necesite
import math # importo la libreria math para hacer operaciones como una raiz cuadrada
import random # importo la libreria random para poder obtener valores aleatorios donde lo necesite

# creo un clase llamada Taxi que hereda de threading.Thread para que actue como un hilo
class Taxi(threading.Thread):
    
    # creo un metodo __init__ que sirve como un constructor donde prepara este nuevo taxi
    def __init__(self, id, matricula, x, y, empresa, ocupado = False, cliente_actual = None, recaudado = 0, total_estrellas = 0, conteo_viajes = 0, antecedentes_penales = False, en_servicio = True):
        super().__init__() # basicamente lo que hace esta linea es ir a ejecutar todo el codigo de inicializacion que necesita la clase Thread antes que cualquier otra cosa.
        self.id = id # esto es el id del taxi
        self.matricula = matricula # esto es la matricula del taxi
        self.x = x # la coordenada x
        self.y = y # la coordenada y
        self.ocupado = ocupado # la variable con la que sabemos si esta ocupado
        self.candado = threading.Lock() # el candado para los semaforos
        self.cliente_actual = cliente_actual # el cliente acutal que esta llevando
        self.recaudado = recaudado # lo que ha recaudado
        self.empresa = empresa # le pone en contacto con el sistema central (empresa) para que puedan comunicarse
        self.antecedentes_penales = antecedentes_penales # los antecedentes penales
        self.en_servicio = en_servicio # si esta en servicio
        self.total_estrellas = total_estrellas # su total de estrellas recibidas
        self.conteo_viajes = conteo_viajes # su total de viajes del dia
          
    # el metodo __str__ sirve para que cuando intentes printear el cliente no aparezcan valores raros, asique le pones una frase que diga quien es el taxi  
    def __str__(self):
        return f"Taxi {self.id} cuya matricula es: {self.matricula}, esta en {self.x}, {self.y} y se dirige a recoger a un cliente"

    # el metodo run lo que hace es decir que hace la clase taxi cuando haga el .start() para inicializar el hilo
    def run(self):
        # mientras que en_servicio sea True el run se va a ejecutar siempre 
        while self.en_servicio:
            # Si el taxi esta ocupado se printean mensajes diciendo lo que esta haciendo con un espacio de 1 segundo entre ellos
            if (self.ocupado == True):
                print(f"Taxi {self.id} yendo a recoger a {self.cliente_actual.id}")
                time.sleep(1)
                print(f"Cliente {self.cliente_actual.id} ya recogido por el taxi {self.id}")
                time.sleep(1)
                distancia_recorrida = math.sqrt((self.cliente_actual.x_destino - self.cliente_actual.x_origen)**2 + (self.cliente_actual.y_destino - self.cliente_actual.y_origen)**2) # se calcula la distancia recorrida
                precio = distancia_recorrida * 0.1 # se calcula el precio final del viaje
                self.recaudado += precio # se suma el precio del viaje al total recaudado por ese taxi
                nota = random.randint(1, 5) # se le asigna una valoracion aleatoria entre 1 y 5 estrellas
                self.total_estrellas += nota # se añade el total de estrellas a la nota
                self.conteo_viajes += 1 # se suma el numero de viajes que ha hecho de uno en uno cada vez que hace 1
                media = (self.total_estrellas / self.conteo_viajes) # se calcula la media
                # se hacen prints dando informacion sobre el trayecto
                print(f"Cliente {self.cliente_actual.id} ha sido entregado en su destino por el taxi {self.id}")
                print(f"El cliente {self.cliente_actual.id} ha pagado {precio:.2f} al taxi {self.id} y le ha calificado con un total de {nota} estrellas. Calificacion media del taxista: {media:.2f} estrellas")
                self.candado.acquire() # el taxi cierra el candado, nadie  puede leer ni escribir en las variables de este taxi hasta que termine.
                # el try es para que si ocurre un error dentro de el, el finally asegura que el candado se abra pase lo que pase. Si no, el taxi se quedaria bloqueado para siempre y nadie podria volver a usarlo.
                try:
                    # aqui se actualiza la posicion del taxi
                    self.x = self.cliente_actual.x_destino
                    self.y = self.cliente_actual.y_destino
                    self.empresa.almacenar_viaje(self.id, self.cliente_actual.id, precio, media) # guarda el viaje en los datos
                    self.ocupado = False # pones el taxi vacio de nuevo
                    self.cliente_actual = None # borras al pasajero anterior
                    print(f"Taxi {self.id} vuelve a estar libre.")
                finally:
                    self.candado.release() # abre el candado
            # este else hace que si no esta con ningun cliente, simplemente espere        
            else:
                print(f"Taxi {self.id} esperando a un cliente en [{self.x}, {self.y}]")
                time.sleep(1)
    
    # cuando se llame a esta funcion la variable en_servicio sera False y el While del run se detendra poniendo fin al servicio
    def detener_servicio(self):
        self.en_servicio = False
    
    # este metodo lo que hace es comprobar si el taxi esta libre y en caso de estarlo reservarle un cliente
    def intentar_ocupar(self, cliente):
        self.candado.acquire() #cierra el candado
        # pase lo que pase abrir el candado con el finally
        try:
            # el if comprueba que vaya libre el taxi
            if self.ocupado == False:
                self.ocupado = True # pongo el taxi en ocupado
                self.cliente_actual = cliente # guardo al cliente actual
                return True
            else:
                return False
        finally:
            self.candado.release() # abre el candado