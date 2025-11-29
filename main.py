from cliente import Cliente
from taxi import Taxi
from sistema import Sistema

if __name__ == "__main__":
    print("Iniciando Sistema de UnieTaxi")
    
    empresa = Sistema()
    
    taxi1 = Taxi("01", "4352 HBG", 100, 100)
    taxi2 = Taxi("02", "3876 JUY", 1000, 1000)
    taxi3 = Taxi("03", "2986 TRQ", 5000, 5000)
    
    taxi1.start()
    taxi2.start()
    taxi3.start()
    
    empresa.registrar_taxi(taxi1)
    empresa.registrar_taxi(taxi2)
    empresa.registrar_taxi(taxi3)
    
    cliente1 = Cliente("Santiago", 500, 700, 200, 400)
    cliente2 = Cliente("Pedro", 600, 200, 500, 900)

    empresa.registrar_clientes(cliente1)
    empresa.registrar_clientes(cliente2)

    taxi_ganador1 = empresa.asignar_taxi(cliente1)
    print(taxi_ganador1)
    
    taxi_ganador2 = empresa.asignar_taxi(cliente2)
    print(taxi_ganador2)