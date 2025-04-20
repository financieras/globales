# luna.py
from config import get_luz, set_luz

print("'luz' en Luna (Inicial):", get_luz())
set_luz(get_luz() + 1)
print("'luz' en Luna (Final):  ", get_luz())