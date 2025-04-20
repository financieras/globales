# principal.py

from config import var
import luna
import marte

# Ahora el orden de importación no importa
# ya que el código en luna.py y marte.py no se ejecuta automáticamente

print("'luz' inicial en 'principal':", var.luz)

# Ejecutamos las funciones en el orden que queramos
luna.procesar_luna()
marte.procesar_marte()

print("'luz' final en 'principal':", var.luz)