import time
from cliente import Cliente
from taxi import Taxi
from sistema import Sistema

if __name__ == "__main__":
    print("Iniciando Sistema de UnieTaxi")
    
    empresa = Sistema()
    
    taxi1 = Taxi("01", "4352 HBG", 0, 0, empresa)
    taxi2 = Taxi("02", "5689 FER", 250, 250, empresa)
    taxi3 = Taxi("03", "3689 LKT", 500, 500, empresa)
    taxi4 = Taxi("04", "1047 JQT", 750, 750, empresa)
    taxi5 = Taxi("05", "3876 JUY", 1000, 1000, empresa)
    taxi6 = Taxi("06", "1085 QUI", 1250, 1250, empresa)
    taxi7 = Taxi("07", "1720 ZJR", 1500, 1500, empresa)
    taxi8 = Taxi("08", "0915 RMO", 1750, 1750, empresa)
    taxi9 = Taxi("09", "2986 TRQ", 2000, 2000, empresa)
    
    taxi1.start()
    taxi2.start()
    taxi3.start()
    taxi4.start()
    taxi5.start()
    taxi6.start()
    taxi7.start()
    taxi8.start()
    taxi9.start()
    
    empresa.registrar_taxi(taxi1)
    empresa.registrar_taxi(taxi2)
    empresa.registrar_taxi(taxi3)
    empresa.registrar_taxi(taxi4)
    empresa.registrar_taxi(taxi5)
    empresa.registrar_taxi(taxi6)
    empresa.registrar_taxi(taxi7)
    empresa.registrar_taxi(taxi8)
    empresa.registrar_taxi(taxi9)

    cliente1 = Cliente("Santiago", 500, 709, 200, 420, empresa)
    cliente2 = Cliente("Pedro", 600, 200, 530, 940, empresa)
    cliente3 = Cliente("Marcos", 708, 100, 870, 900, empresa)
    cliente4 = Cliente("Maria", 1000, 1200, 1500, 1900, empresa)
    cliente5 = Cliente("Lucia", 1400, 200, 650, 780, empresa)
    cliente6 = Cliente("Lucas", 669, 1250, 1523, 1956, empresa)
    
    cliente1.start()
    cliente2.start()
    cliente3.start()
    cliente4.start()
    cliente5.start()
    cliente6.start()
    
    time.sleep(20)
    
    empresa.cierre_contable()
    empresa.reporte_calidad()