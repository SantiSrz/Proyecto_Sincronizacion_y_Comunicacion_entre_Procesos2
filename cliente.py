import threading # importo la libreria threading para trabajar con hilos

# creo un clase llamada clientes que hereda de threading.Thread para que actue como un hilo
class Cliente(threading.Thread):

    # creo un metodo __init__ que sirve como un constructor donde prepara este nuevo cliente
    def __init__(self, id, x_origen, y_origen, x_destino, y_destino, empresa):

        super().__init__() # basicamente lo que hace esta linea es ir a ejecutar todo el codigo de inicializacion que necesita la clase Thread antes que cualquier otra cosa.
        self.id = id # con su nombre
        self.x_origen = x_origen # posición inicial x
        self.y_origen = y_origen # posición inicial y
        self.x_destino = x_destino # posición de destino x
        self.y_destino = y_destino # posición de destino y
        self.empresa = empresa # le pone en contacto con el sistema central (empresa) para que puedan comunicarse
        
    # el metodo __str__ sirve para que cuando intentes printear el cliente no aparezcan valores raros, asique le pones una frase que diga quien es el cliente
    def __str__(self):
        return f"Cliente {self.id} de origen: {self.x_origen}, {self.y_origen} quiere ir a {self.x_destino}, {self.y_destino}"

    # el metodo run lo que hace es decir que hace la clase cliente cuando haga el .start() para inicializar el hilo
    def run(self):
        self.empresa.asignar_taxi(self) # aqui lo que hago es llamar a la empresa para que le asignen al cliente un taxi llamandose a si mismo con el .self y con la funcion asignar_taxi que esta en la clase Sistema