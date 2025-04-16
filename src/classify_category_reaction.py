def classify_category(time):
    if time < 200: return 'Rápido'
    if time < 500: return 'Normal'
    return 'Lento'