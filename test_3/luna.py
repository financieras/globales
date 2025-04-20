# luna.py
from config import config

print("'luz' en Luna (Inicial):", config.get("luz"))
config.set("luz", config.get("luz") + 1)
print("'luz' en Luna (Final):  ", config.get("luz"))