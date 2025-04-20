# principal.py
from config import config
import luna
import marte

# El orden de ejecución sigue siendo importante para el valor de la variable global
# Al importar luna y marte, ya se ejecutan sus códigos

print("'luz' en 'principal':", config.get("luz"))