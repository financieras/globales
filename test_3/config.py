# config.py
class Config:
    def __init__(self):
        self._variables = {"luz": 3}
    
    def get(self, key):
        return self._variables.get(key)
    
    def set(self, key, value):
        # Puedes agregar validación aquí
        self._variables[key] = value

config = Config()