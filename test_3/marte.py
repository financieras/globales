# marte.py
from config import config

print("'luz' en Marte (Inicial):", config.get("luz"))
config.set("luz", config.get("luz") + 1)
print("'luz' en Marte (Final):", config.get("luz"))