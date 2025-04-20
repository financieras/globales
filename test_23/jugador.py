# jugador.py
from config import var

def tirar_dado(jugador_id, puntos):
    var.total_tiradas += 1
    
    print(f"Jugador {jugador_id} ha tirado el dado")
    print(f"Total de tiradas: {var.total_tiradas}")
    print(f"Puntaje actual: {var.puntaje_actual}")
    print(f"Puntos obtenidos: {puntos}")
    
    # Devuelve algún resultado
    return var.total_tiradas