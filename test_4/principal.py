# principal.py
import config
import luna
import marte

# El orden de ejecución sigue siendo importante
# Al importar luna y marte, ya se ejecutan sus códigos

print("'luz' en 'principal':", config.current_config.luz)