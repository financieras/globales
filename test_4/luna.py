# luna.py
import config

print("'luz' en Luna (Inicial):", config.current_config.luz)
config.update_config(luz=config.current_config.luz + 1)
print("'luz' en Luna (Final):  ", config.current_config.luz)