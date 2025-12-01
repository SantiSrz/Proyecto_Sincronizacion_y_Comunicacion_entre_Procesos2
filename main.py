import time
from cliente import Cliente
from taxi import Taxi
from sistema import Sistema

if __name__ == "__main__":
    print("Iniciando Sistema de UnieTaxi")
    
    empresa = Sistema()
    
    taxi1 = Taxi("01", "4352 HBG", 0, 0)
    taxi2 = Taxi("02", "3689 LKT", 500, 500)
    taxi3 = Taxi("03", "3876 JUY", 1000, 1000)
    taxi4 = Taxi("04", "1720 ZJR", 1500, 1500)
    taxi5 = Taxi("05", "2986 TRQ", 2000, 2000)
    
    taxi1.start()
    taxi2.start()
    taxi3.start()
    taxi4.start()
    taxi5.start()
    
    empresa.registrar_taxi(taxi1)
    empresa.registrar_taxi(taxi2)
    empresa.registrar_taxi(taxi3)
    empresa.registrar_taxi(taxi4)
    empresa.registrar_taxi(taxi5)

    cliente1 = Cliente("Santiago", 500, 700, 200, 400, empresa)
    cliente2 = Cliente("Pedro", 600, 200, 500, 900, empresa)
    
    cliente1.start()
    cliente2.start()
    
    time.sleep(6)
    
    empresa.cierre_contable()