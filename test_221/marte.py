# marte.py

from config import var

def procesar_marte():
    print("'luz' en Marte (Inicial):", var.luz)
    var.luz += 1
    print("'luz' en Marte (Final):", var.luz)

# El código solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    procesar_marte()