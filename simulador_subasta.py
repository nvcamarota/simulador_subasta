"""
SIMULADOR DE SUBASTA CON GENERADOR Y DECORADOR
Objetivo: Crear un generador que simule una subasta donde se reciben ofertas dinámicamente, y un decorador que valide que las ofertas sean mayores a la actual.
"""

# Función madre para aceptar y rechazar ofertas según la lógica escrita:
def validar_oferta(func):
    def wrapper(oferta_actual, nueva_oferta):
        if nueva_oferta > oferta_actual:
            return func(oferta_actual, nueva_oferta)
        else:
            print(f'Oferta rechazada: ${nueva_oferta}. Debe ofrecer un valor mayor a la oferta actual: ${oferta_actual}.')
            return oferta_actual
    return wrapper

#  Función para definir el valor inicial de la subasta y condicional para procesar las ofertas ingresadas:
def subasta():
    oferta_inicial = 0
    print(f'Iniciando subasta en: ${oferta_inicial}.')
    
    while True:
        nueva_oferta = yield oferta_inicial
        oferta_inicial = procesar_oferta(oferta_inicial, nueva_oferta)

# Decorando función «procesar_oferta» con la función madre:
@validar_oferta
def procesar_oferta(oferta_actual, nueva_oferta):
    print(f'Oferta actual: ${oferta_actual}.')
    print(f'Oferta aceptada: ${nueva_oferta}.')
    return nueva_oferta

# Next continúa con la pausa del yield hacia la siguiente oferta:
generador_subasta = subasta()
next(generador_subasta)

# Lista de ofertas, se iteran para mostrar las nuevas ofertas:
ofertas = [1000, 2500, 500, 10000, 50000, 100000, 200000]
for oferta in ofertas:
    print(f'Procesando nueva(s) oferta(s): ${oferta}')
    generador_subasta.send(oferta)
