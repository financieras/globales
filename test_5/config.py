# config.py
class Config:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance
    
    def initialize(self):
        self.variables = {"luz": 3}
    
    def get(self, key):
        return self.variables.get(key)
    
    def set(self, key, value):
        self.variables[key] = value

# Exportamos una instancia única
config = Config()

'''
Explicación del patrón Singleton

El patrón Singleton asegura que:

    Solo exista una instancia de la clase Config en toda la aplicación
    Proporciona un punto de acceso global a esa instancia
    La instancia se crea solo cuando se necesita por primera vez (inicialización perezosa)

Ventajas:

    Garantiza un único punto de verdad para tus configuraciones
    Evita problemas de múltiples instancias con diferentes estados
    Proporciona acceso global y consistente
    Permite inicialización controlada

Desventajas:

    Puede hacer el código más difícil de probar (debido al estado global)
    Oculta las dependencias (los módulos que usan la configuración no declaran explícitamente esta dependencia)

En la práctica, cuando importas config en cualquier módulo, siempre obtendrás la misma instancia, por lo que cualquier cambio en las variables será visible en todos los módulos que lo importan.
'''