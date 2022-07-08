# Funcion para obtener la ruta
def ruta():
    import os
    # Obtenemos la ruta actual
    path = os.getcwd()
    # Partimos todo lo que tenga el backslash \\ y nos retorna una lista
    path = path.split('\\')
    # Creamos una lista
    entirePath = []
    # recorremos la lista de la ruta.
    for p in path:
        if (p == 'web'):
            break
        else:
            p += '/'
            entirePath.append(p)
    entirePath.append('attendance/')
    letter = ''    
    path = letter.join(entirePath)
    path += 'model/datasets/attendance_system_dataset'
    return path
