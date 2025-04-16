#  Eliminar espacios extra en los nombres. --> Con strip
#  Convertir todos los nombres a formato de título (primera letra en mayúscula y el resto en minúscula). --> con title
#  Eliminar registros duplicados para evitar clientes repetidos. --> con un set
#  Eliminar valores vacíos o nulos, ya que no aportan información válida. --> Con la funcion filter
#  Mostrar la lista limpia de clientes listos para usar en el sistema de facturación.

def clean_data_list_str(data_list_string):
    # Filter va ir iterando en cada elemento de la lista y solo agrega al iterable lo que 
    filtered = filter(
        lambda x: (
            x is not None and                  # Elimina None
            isinstance(x, str) and             # Asegura que sea string
            x.strip() and                      # Elimina vacíos/espacios
            not x.isdigit() and                # Elimina puros números ("123")
            not x.isspace() and                # Elimina solo espacios ("   ")
            '\n' not in x                      # Elimina strings con saltos de línea
            # Agregar más condiciones si es necesario
        ),
        data_list_string
    )
    
    # Map aplica a cada elemento del iterable filtrado el strip y el title
    processed = map(lambda x: x.strip().title(), filtered)
    # Con la funcion sorted que retorna una lista ordenada y se puede usar sobre cualquier iterable
    return sorted(set(processed))  # Otra forma: Mantiene el orden original, se necesita python 3.2, dict.fromkeys 