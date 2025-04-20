# principal.py

from random import randint
from config import var
import jugador

# Ahora el juego puede llamar a las funciones en el orden que necesite
# sin preocuparse por el orden de importación

print("Iniciando juego")
print(f"Puntaje inicial: {var.puntaje_actual}\n")

# Simulación de turnos de juego
for i in range(var.numero_jugadores):
    puntos = randint(1, 6)
    jugador.tirar_dado(i+1, puntos)
    var.puntaje_actual += puntos
    print(f"Puntaje actualizado: {var.puntaje_actual}")
    print()

print("Fin del juego")
print(f"Puntaje final: {var.puntaje_actual}")