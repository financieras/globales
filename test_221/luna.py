# luna.py

from config import var

def procesar_luna():
    print("'luz' en Luna (Inicial):", var.luz)
    var.luz += 1
    print("'luz' en Luna (Final):  ", var.luz)

# El código solo se ejecuta si este archivo es el principal
if __name__ == "__main__":
    procesar_luna()