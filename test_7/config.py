# config.py
import os
from dotenv import load_dotenv

# Carga las variables del archivo .env
load_dotenv()

# Diccionario para almacenar valores en tiempo de ejecución
_valores = {}

def get_luz():
    if "LUZ" in _valores:
        return _valores["LUZ"]
    return int(os.environ.get("LUZ", 3))

def set_luz(valor):
    _valores["LUZ"] = valor
    os.environ["LUZ"] = str(valor)  # Actualiza también la variable de entorno

'''
# Explicación del método con python-dotenv

Este método utiliza la biblioteca `python-dotenv` para gestionar variables de configuración entre múltiples archivos Python, proporcionando una solución flexible y organizada.

### Características principales:

1. **Separación de configuración y código**: Los valores iniciales se almacenan en un archivo `.env` externo, siguiendo buenas prácticas de desarrollo.

2. **Persistencia inicial**: Al iniciarse la aplicación, `load_dotenv()` carga todas las variables del archivo `.env` al entorno del sistema.

3. **Modificación en tiempo de ejecución**: El diccionario interno `_valores` permite cambiar los valores durante la ejecución sin alterar el archivo `.env` original.

4. **Interfaz consistente**: Las funciones `get_luz()` y `set_luz()` proporcionan un API claro para acceder y modificar los valores.

5. **Priorización de valores**: Primero busca en el diccionario interno (para valores modificados), luego en las variables de entorno (valores iniciales).

Este método es especialmente útil cuando necesitas:
- Configuraciones que puedan cambiar durante la ejecución
- Separar la configuración del código fuente
- Compartir valores entre diferentes módulos
- Establecer valores predeterminados que puedan ser sobrescritos

Es una solución equilibrada que combina la simplicidad con buenas prácticas de desarrollo, perfecta para aplicaciones medianas donde quieres mantener la configuración organizada sin añadir demasiada complejidad.
'''