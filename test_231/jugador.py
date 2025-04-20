# jugador.py

from config import g, PieceColor, Direction

# Usar una dirección
delta = Direction.NORTHEAST.value  # (-1, 1)

# Acceder a una constante global
print(g.BOARD_SIZE)

# Actualizar el marcador
g.total_score[PieceColor.BLACK] += 1
