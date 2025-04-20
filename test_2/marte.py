# marte.py
import config

print("'luz' en Marte (Inicial):", config.glo["luz"])

config.glo["luz"] += 1

print("'luz' en Marte (Final):", config.glo["luz"])