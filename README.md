1. Introducción
Este proyecto va de crear una simulación de un sistema de taxis llamado UNIETAXI. La idea principal es poner en práctica lo que he ido aprendiendo sobre programación concurrente (hilos) para manejar recursos compartidos sin que el programa reviente. Yo al principio no tenía ni idea de como hacer esto, pero con unos cuantos videos y ayuda de la inteligencia artificial para ayudarme a entender lo que tenía que hacer, he aprendido mucho y estoy muy satisfecho con mi trabajo.
Básicamente, lo que hacemos en el programa es simular un entorno en tiempo real donde hay Taxis y Clientes moviéndose a la vez. Como todos intentaban acceder a los mismos datos al mismo tiempo, el reto ha sido usar mecanismos de sincronización para que no haya errores como que dos clientes se suban al mismo taxi y que el servicio funcione bien.

2. Arquitectura del programa
Este código lo he creado usando Python y he utilizado la programación orientada a objetos. Dividí el código en 4 archivos:
Taxi.py: Es el trabajador. Cada taxi es un hilo independiente que hace su vida: espera al cliente, conduce, cobra y actualiza su estado.
Cliente.py: Es el usuario. También es un hilo que aparece, pide un taxi al sistema y espera a que lo recojan.
Sistema.py: Es el cerebro de todo. Es el hilo más importante ya que gestiona la lógica: registra a la gente, decide qué taxi asignar (el match), lleva las cuentas y hace las auditorías.
Main.py: Es el que controla el tiempo. Simula el reloj del día (de 6:00 a 24:00) y va sacando a los clientes poco a poco para que no entren todos de golpe.

3. Hilos y Recursos Críticos

3.1. Hilos
He usado la librería threading de Python. Los archivos Taxi y Cliente heredan de threading.Thread. Esto lo que hace es:
Permitir que varios taxis estén ocupados a la vez.
Permitir que los clientes puedan pedir servicio sin bloquear el programa principal.

3.2. Recursos Críticos
Identifique unas variables que eran peligrosas si dos hilos las tocaban a la vez. Las más importantes eran:
Estado del Taxi (self.ocupado): Si dos clientes leían que un taxi estaba libre en el mismo microsegundo, los dos intentaban cogerlo y esto generaba un problema.
Posición (self.x, self.y): El sistema las leía para calcular distancias mientras el taxi las escribía al moverse.
Dinero (self.recaudado): Había que protegerlo para que el cierre de caja final cuadrase bien.

3.3. Locks
Para solucionar los anteriores problemas, he usado Semáforos (threading.Lock). Cada Taxi tiene su propio candado (self.candado). La lógica es la siguiente:
Pedir llave: Antes de cambiar algo, el hilo hace .acquire().
Sección Crítica: Hace los cambios necesarios de forma segura.
Soltar llave: Hace .release() siempre dentro de un finally para asegurarse de que no quede bloqueado si el código falla.

4. Cómo se asignan los taxis
En el módulo Sistema he programado un algoritmo para elegir el mejor taxi en base a las siguientes cosas:
Filtro: Si el taxi está ocupado o tiene antecedentes penales.
Distancia: Calculo quién está más cerca del cliente.
Calidad: Si hay empate de distancia, gana el que tenga mejor nota media.
Azar: Si aun así siguen empatados en todo, elegimos uno aleatoriamente usando random.choice de la librería random.

5. Estructura de las funciones principales
En Sistema.py:
asignar_taxi(cliente):
Entra: El cliente con su posición.
Sale: El objeto Taxi elegido o None si no hay libres.
registrar_taxi(taxi):
Entra: El objeto Taxi nuevo.
Sale: Lo mete en una lista o lo rechaza si tiene antecedentes.
En Taxi.py:
intentar_ocupar(cliente):
Entra: El cliente.
Sale: True si consiguió reservarlo o False si alguien ha sido más rápido.

6. Guardar datos (Logs)
Para cumplir con lo de la trazabilidad, he hecho que el sistema escriba todo lo que pasa en un archivo llamado Datos.txt. Cada vez que hay un viaje, un cobro o se rechaza a un taxista, se escribe una línea en el archivo .txt. Así queda todo guardado ahí aunque cerremos el programa.

7. Pruebas de que funciona
He ejecutado el programa y estos son los resultados de la consola:

Caso 1: Seguridad basada en los antecedentes: Intenté meter a los taxis 010 y 011 con antecedentes penales y aparece lo siguiente:
Salida: El taxista 010 no puede trabajar aqui debido a sus antecedentes penales Resultado: El sistema los detectó, no los metió en la lista y apagó sus hilos. Correcto.

Caso 2: Un viaje completo: Se puede ver cómo el taxi se mueve, cobra y se pone libre.
Salida: Taxi 02 yendo a recoger a Laura -> Cliente Laura ya recogido -> Cliente entregado... pagado 120.42... nota: 5 estrellas -> Taxi 02 vuelve a estar libre.

Caso 3: Cierre del día: A las 24:00h, el sistema hace las cuentas.
Salida: Todo lo que ha recaudado el taxi 08: 618.84. UNIETAXI se lleva: 123.77 y taxista: 495.07 Auditoría: También sacó 5 viajes al azar para revisar la calidad.
