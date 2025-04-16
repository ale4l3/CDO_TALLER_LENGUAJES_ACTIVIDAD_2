import random
import string
from datetime import datetime

def generate_discount_code(username):
    # Procesar nombre de usuario (primeros 5 caracteres en mayusculas)
    # El método .replace() en Python es una función de cadenas (strings) que reemplaza todas las ocurrencias de un substring por otro
    if len(username) <= 15:
        username_part = username.upper().replace(" ", "")
    else:
        print("El nombre de usuario tiene mas de 15 caracteres")
    
    # ABAJO como sería si es el usuario que ingresa la fecha. Lo dejo para ver bien el proceso de conversión
    # datetime.strptime() (String Parse Time):  Convierte un string en un objeto datetime (fecha+hora).
    # .date(): Extrae solo la parte de fecha (elimina la hora, que es 00:00:00 por defecto en strptime). Retorna un objeto date (solo fecha, sin hora).
    #date_obj = datetime.strptime(date_str, "%Y%m%d").date()
    # strftime() (String Format Time): Convierte un objeto fecha (o datetime) en string con formato personalizado.
    # formatted_date = date_obj.strftime("%Y%m%d")

    #Fecha actual con datetime.now() y la transformo en date
    current_date = datetime.now().date().strftime('%Y%m%d')
    
    # Generar parte aleatoria
    random_chars = string.ascii_uppercase + string.digits
    random_part = ''.join(random.choices(random_chars, k=17))
    
    # Combinar todo
    return f"{username_part}-{current_date}-{random_part}"