# marte.py
import config

luz_inicial = config.get_int("LUZ")
print("'luz' en Marte (Inicial):", luz_inicial)

config.set("LUZ", luz_inicial + 1)
print("'luz' en Marte (Final):", config.get_int("LUZ"))