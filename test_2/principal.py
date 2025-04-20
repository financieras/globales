# principal.py
import config
import luna
import marte

# El orden de ejecución es importante para el valor de la variable global
luna.config.glo["luz"]      # primero ejecutamos luna
marte.config.glo["luz"]     # luego ejecutamos marte

print("'luz' en 'principal':", config.glo["luz"])