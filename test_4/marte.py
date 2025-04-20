# marte.py
import config

print("'luz' en Marte (Inicial):", config.current_config.luz)
config.update_config(luz=config.current_config.luz + 1)
print("'luz' en Marte (Final):", config.current_config.luz)