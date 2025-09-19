from datetime import datetime

hora_actual = datetime.now().hour
if hora_actual <12:
    saludo = "Buenos días Pedro"
elif 12 <= hora_actual <20:
    saludo = "Buenas tardes Pedro"
else:
    saludo = "Buenas noches Pedro"
print(saludo)