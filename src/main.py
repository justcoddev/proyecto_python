from datetime import datetime as dt

current_time = dt.now()

print('Hola! Este es mi primer código Python :D')
print(f'Hora actual: {current_time.strftime("%H:%M:%S")}')
print(f'Fecha actual: {current_time.strftime("%d/%m/%Y")}')
