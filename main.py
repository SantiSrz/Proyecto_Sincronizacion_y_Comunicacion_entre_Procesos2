import time # importo la libreria time para poder hacer esperar al programa por x segundos donde lo necesite
import random # importo la libreria random para poder obtener valores aleatorios donde lo necesite
from cliente import Cliente # importo la clase Cliente del archivo cliente
from taxi import Taxi # importo la clase Taxi del archivo taxi
from sistema import Sistema # importo la clase Sistema del archivo sistema

# aqui lo que hago es un metodo para que no se haga print a ninguna linea que pueda haber quedado suelta de otro archivo y solo se haga print a lo que hay en el archivo main
if __name__ == "__main__":
    print("Iniciando Sistema de UnieTaxi")
    
    empresa = Sistema() # asigno la clase Sistema a la variable empresa para comunicarme con los taxis y clientes
    
    # Creo los taxis con sus debidos valores
    taxi1 = Taxi("01", "4352 HBG", 0, 0, empresa, antecedentes_penales = False)
    taxi2 = Taxi("02", "5689 FER", 250, 250, empresa, antecedentes_penales = False)
    taxi3 = Taxi("03", "3689 LKT", 500, 500, empresa, antecedentes_penales = False)
    taxi4 = Taxi("04", "4595 SDU", 1000, 1000, empresa, antecedentes_penales = False)
    taxi5 = Taxi("05", "3876 JUY", 1000, 1000, empresa, antecedentes_penales = False)
    taxi6 = Taxi("06", "1047 JQT", 1250, 1250, empresa, antecedentes_penales = False)
    taxi7 = Taxi("07", "1085 QUI", 1500, 1500, empresa, antecedentes_penales = False)
    taxi8 = Taxi("08", "1720 ZJR", 1750, 1750, empresa, antecedentes_penales = False)
    taxi9 = Taxi("09", "0915 RMO", 2000, 2000, empresa, antecedentes_penales = False)
    taxi10 = Taxi("010", "2986 TRQ", 567, 1345, empresa, antecedentes_penales = True)
    taxi11 = Taxi("011", "8782 HGQ", 50, 350, empresa, antecedentes_penales = True)
    
    # inicializo los hilos inicializando los metodos run de los taxis
    taxi1.start()
    taxi2.start()
    taxi3.start()
    taxi4.start()
    taxi5.start()
    taxi6.start()
    taxi7.start()
    taxi8.start()
    taxi9.start()
    taxi10.start()
    taxi11.start()
    
    # registro los taxis en una lista
    empresa.registrar_taxi(taxi1)
    empresa.registrar_taxi(taxi2)
    empresa.registrar_taxi(taxi3)
    empresa.registrar_taxi(taxi4)
    empresa.registrar_taxi(taxi5)
    empresa.registrar_taxi(taxi6)
    empresa.registrar_taxi(taxi7)
    empresa.registrar_taxi(taxi8)
    empresa.registrar_taxi(taxi9)
    empresa.registrar_taxi(taxi10)
    empresa.registrar_taxi(taxi11)

    # Creo los clientes con sus debidos valores
    cliente1 = Cliente("Santiago", 500, 700, 200, 420, empresa)
    cliente2 = Cliente("Pedro", 600, 200, 530, 940, empresa)
    cliente3 = Cliente("Marcos", 708, 100, 870, 900, empresa)
    cliente4 = Cliente("Maria", 1000, 1200, 1500, 1900, empresa)
    cliente5 = Cliente("Lucia", 1400, 200, 650, 780, empresa)
    cliente6 = Cliente("Lucas", 669, 1250, 1520, 1950, empresa)
    cliente7 = Cliente("Ana", 120, 300, 500, 600, empresa)
    cliente8 = Cliente("Raul", 2200, 150, 1000, 1000, empresa)
    cliente9 = Cliente("Sofia", 800, 900, 100, 200, empresa)
    cliente10 = Cliente("Diego", 150, 1500, 800, 800, empresa)
    cliente11 = Cliente("Laura", 300, 400, 1200, 1200, empresa)
    cliente12 = Cliente("Pablo", 1800, 1800, 500, 500, empresa)
    cliente13 = Cliente("Carmen", 50, 50, 300, 300, empresa)
    cliente14 = Cliente("Jorge", 900, 100, 2000, 2000, empresa)
    cliente15 = Cliente("Sara", 600, 1600, 400, 400, empresa)
    cliente16 = Cliente("Alberto", 1100, 1100, 100, 900, empresa)
    cliente17 = Cliente("Marina", 400, 200, 1500, 1500, empresa)
    cliente18 = Cliente("Luis", 1900, 500, 800, 200, empresa)
    cliente19 = Cliente("Clara", 750, 750, 300, 900, empresa)
    cliente20 = Cliente("Manuel", 200, 2000, 1000, 500, empresa)
    cliente21 = Cliente("Patricia", 1300, 300, 600, 600, empresa)
    cliente22 = Cliente("Daniel", 500, 1000, 200, 200, empresa)
    cliente23 = Cliente("Paula", 1600, 1600, 900, 900, empresa)
    cliente24 = Cliente("Roberto", 100, 800, 1400, 1400, empresa)
    cliente25 = Cliente("Teresa", 950, 450, 1100, 1100, empresa)
    cliente26 = Cliente("Fernando", 350, 1350, 700, 700, empresa)
    cliente27 = Cliente("Isabel", 1250, 150, 400, 1600, empresa)
    cliente28 = Cliente("Ricardo", 50, 1900, 850, 850, empresa)
    cliente29 = Cliente("Rosa", 2100, 2100, 100, 100, empresa)
    cliente30 = Cliente("Miguel", 1000, 500, 2000, 1000, empresa)
    cliente31 = Cliente("Elena", 300, 1800, 900, 900, empresa)
    cliente32 = Cliente("Beatriz", 100, 100, 2000, 2000, empresa)
    
    # registro los clientes en una lista
    empresa.registrar_clientes(cliente1)
    empresa.registrar_clientes(cliente2)
    empresa.registrar_clientes(cliente3)
    empresa.registrar_clientes(cliente4)
    empresa.registrar_clientes(cliente5)
    empresa.registrar_clientes(cliente6)
    empresa.registrar_clientes(cliente7)
    empresa.registrar_clientes(cliente8)
    empresa.registrar_clientes(cliente9)
    empresa.registrar_clientes(cliente10)
    empresa.registrar_clientes(cliente11)
    empresa.registrar_clientes(cliente12)
    empresa.registrar_clientes(cliente13)
    empresa.registrar_clientes(cliente14)
    empresa.registrar_clientes(cliente15)
    empresa.registrar_clientes(cliente16)
    empresa.registrar_clientes(cliente17)
    empresa.registrar_clientes(cliente18)
    empresa.registrar_clientes(cliente19)
    empresa.registrar_clientes(cliente20)
    empresa.registrar_clientes(cliente21)
    empresa.registrar_clientes(cliente22)
    empresa.registrar_clientes(cliente23)
    empresa.registrar_clientes(cliente24)
    empresa.registrar_clientes(cliente25)
    empresa.registrar_clientes(cliente26)
    empresa.registrar_clientes(cliente27)
    empresa.registrar_clientes(cliente28)
    empresa.registrar_clientes(cliente29)
    empresa.registrar_clientes(cliente30)
    empresa.registrar_clientes(cliente31)
    empresa.registrar_clientes(cliente32)

    # creo otra lista con los clientes para que una vez ya haya cumplido su viaje no vuelvan a aparecer
    clientes_pendientes = [cliente1, cliente2, cliente3, cliente4, cliente5, cliente6, cliente7, cliente8, cliente9, cliente10, cliente11, cliente12, cliente13, cliente14, cliente15, cliente16, cliente17, cliente18, cliente19, cliente20, cliente21, cliente22, cliente23, cliente24, cliente25, cliente26, cliente27, cliente28, cliente29, cliente30, cliente31, cliente32]
    
    # hago un bucle for para simular las horas de trabajo que van desde las 6am hasta las 12 de la noche
    for hora in range(6, 25):
        print(f"\nSon las {hora}:00")
        cantidad_a_sacar = min(2, len(clientes_pendientes)) # aqui lo que se hace es ir cogiendo de dos en dos hasta que haya menos de dos, que se cogera el mas pequeño debido a la funcion min()
        if cantidad_a_sacar > 0:
            elegidos = random.sample(clientes_pendientes, cantidad_a_sacar) # aqui se eligen dos clientes aleatorios de la lista
            for c in elegidos:
                print(f"- Ha aparecido un nuevo cliente:  {c.id}") # este for hace que aparezca en la consola el cliente seleccionado y lo inicialice, una vez terminado lo quita de la lista para que no se repita
                c.start()
                clientes_pendientes.remove(c)           
        time.sleep(1) # el sistema duerme por 1 segundo, hay que poner esto para que no se impriman todos a la vez
     
    empresa.cierre_contable() # se llama a la funcion cierre_contable() una vez ha acabado el dia para poner un resumen de cuanto ha facturado cada taxista
    empresa.reporte_calidad() # se llama a la funcion reporte_calidad() una vez ha acabado el dia para elegir 5 viajes realizados en ese dia aleatoriamente y enseñar los datos de ese mismo viaje
    
    # aqui uso estos dos bucles for para poner fin al programa una vez ha llegado a las 12 de la noche
    for t in empresa.taxis:
        t.detener_servicio()
    for t in empresa.taxis:
        t.join()
    print("\nEl programa ha terminado por hoy\n")