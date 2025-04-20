# principal.py
import config

if __name__ == "__main__":
    import luna
    import marte

    print("C_LUZ en Principal (Inicial):", config.estado_global["C_LUZ"])
    luna.modificar_y_mostrar()
    print("C_LUZ en Principal (Tras Luna):", config.estado_global["C_LUZ"])
    marte.mostrar()