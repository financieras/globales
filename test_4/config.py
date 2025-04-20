from dataclasses import dataclass

@dataclass(frozen=True)
class GlobalConfig:
    luz: int = 3
    # otras variables...

# Creamos una instancia inicial
initial_config = GlobalConfig()

# Variable para almacenar la configuración actual
current_config = initial_config

# Función para actualizar la configuración (creando una nueva instancia)
def update_config(**kwargs):
    global current_config
    # Creamos un diccionario con los valores actuales
    new_values = {field: getattr(current_config, field) 
                 for field in current_config.__dataclass_fields__}
    # Actualizamos con los nuevos valores
    new_values.update(kwargs)
    # Creamos una nueva instancia
    current_config = GlobalConfig(**new_values)
    return current_config


'''
Explicación
Esta solución utiliza una dataclass inmutable (con frozen=True), lo que significa que no puedes modificar sus atributos directamente. Para "cambiar" un valor, creamos una nueva instancia con los valores actualizados usando la función update_config.
Ventajas:

Más seguridad: los valores no pueden ser modificados accidentalmente
Tipado estático: puedes definir los tipos de tus variables
Más legible y autodocumentado
Detección de errores durante el desarrollo

Desventajas:

Más complejo que tu solución original
Cada actualización crea un nuevo objeto (más uso de memoria)
Necesitas usar una función especial para actualizar valores

Esta solución es buena cuando:

Necesitas garantías sobre los tipos de datos
Quieres documentación integrada sobre las variables
Prefieres un estilo más funcional donde los estados no cambian directamente

Si prefieres la simplicidad sobre estas ventajas, tu solución original o la clase Config con métodos get/set podrían ser más apropiadas.
'''