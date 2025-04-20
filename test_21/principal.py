# principal.py
from config import config
import luna     # Importante: 1º luna
import marte    # Importante: 2º marte

# El orden de ejecución sigue siendo importante
# Al importar luna y marte, ya se ejecutan sus códigos

print("'luz' en 'principal':", config.luz)