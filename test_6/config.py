# config.py
import os

# Inicialización de valores por defecto
if "LUZ" not in os.environ:
    os.environ["LUZ"] = "3"

def get(key, default=None):
    return os.environ.get(key, default)

def set(key, value):
    os.environ[key] = str(value)  # os.environ solo acepta strings

def get_int(key, default=0):
    try:
        return int(get(key, default))
    except (ValueError, TypeError):
        return default

'''
Vamos a implementar el enfoque basado en variables de entorno usando os.environ. Este es un método útil cuando quieres que la configuración pueda ser modificada desde fuera de la aplicación, como al iniciar el programa.


Explicación
Esta solución utiliza variables de entorno para almacenar la configuración:

El módulo config.py proporciona funciones helper para obtener y establecer valores
Todos los valores en os.environ deben ser strings, por lo que usamos funciones de conversión como get_int
Se establecen valores predeterminados si las variables no están definidas

Ventajas:

Permite establecer la configuración desde fuera del programa (ej: LUZ=5 python principal.py)
Sigue el patrón de 12-Factor App para configuración
Facilita diferentes configuraciones para diferentes entornos (desarrollo, producción, etc.)
No requiere archivos de configuración adicionales

Desventajas:

Todos los valores deben ser strings (requiere conversión para otros tipos)
Menos seguro (las variables de entorno son accesibles para todos los procesos del usuario)
Menos adecuado para configuraciones complejas o jerárquicas

Este enfoque es particularmente útil para aplicaciones que siguen los principios de 12-Factor App y especialmente en entornos de contenedores o cloud donde la configuración a través de variables de entorno es una práctica común.

'''