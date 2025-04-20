# marte.py
from config import get_luz, set_luz

print("'luz' en Marte (Inicial):", get_luz())
set_luz(get_luz() + 1)
print("'luz' en Marte (Final):", get_luz())