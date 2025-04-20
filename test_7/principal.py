# principal.py
from config import get_luz
import luna
import marte

# El orden de ejecución sigue siendo importante
# Al importar luna y marte, ya se ejecutan sus códigos

print("'luz' en 'principal':", get_luz())