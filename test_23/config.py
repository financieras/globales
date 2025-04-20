# config.py

class Var:
    def __init__(self):
        self.puntaje_actual = 0
        self.turno_jugador = 1
        self.total_tiradas = 0
        self.numero_jugadores = 3

# Instancia global única
var = Var()

'''
El juego consiste en que cada uno de los tres jugadores lanza un dado y
 obtiene unos puntos.
Los puntos individuales de cada jugador se van acumulando entre todos ellos y
 se van imprimiendo.
'''