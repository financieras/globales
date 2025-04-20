# luna.py
import config

def modificar_y_mostrar():
    print("C_LUZ en Luna (Inicial):", config.estado_global["C_LUZ"])
    config.estado_global["C_LUZ"] *= 2
    print("C_LUZ en Luna (Final):  ", config.estado_global["C_LUZ"])

