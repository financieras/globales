# luna.py
import config

luz_inicial = config.get_int("LUZ")
print("'luz' en Luna (Inicial):", luz_inicial)

config.set("LUZ", luz_inicial + 1)
print("'luz' en Luna (Final):  ", config.get_int("LUZ"))