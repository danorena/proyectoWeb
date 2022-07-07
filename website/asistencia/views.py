from django.shortcuts import render

# Create your views here.
def asistenciaCall(request):
    
    if request.method == 'POST':
        asistencia = Asistencia()
        d= request.POST
        # for key,value in d.items():
        #     # Obtiene la fecha 
        #     if key=='date':
        #         date = value
        #     # Obtiene ficha
        #     if key == 'ficha':
        #         ficha = value
        fecha = '2022-05-11'
        ficha = '01'
        asistencia.toHtml(asistencia.dataFrameAsistencia(fecha ))
        return render(request,'asistenciaFicha.html')

    fichas = dir()
    return render(request,'asistencia.html',{'fichas' : fichas})
    



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

# Hacemos una funcion para leer las fichas
def dir():
    import os
    # buscamos la ruta que contiene todas la fichas
    path  = ruta() 
    # guardamos todas las fichas en una lista iterable
    grupo = os.listdir(path)
    # Devolvemos una lista para iterar sobre esta 
    return grupo


# Instalar pandas
# instalar openpyx

class Asistencia:
    # Constructor 
    def __init__(self,ficha,fecha):
        self.ficha = ficha
        self.fecha = fecha

    # Funcion para obtener el nombre del aprendiz, la asistencia y el dia
    def dataFrameAsistencia(self,fecha):

        # Importamos la libreria de pandas
        import pandas as pd

        # Leemos el archivo .Json
        fileJson = pd.read_json('attendance.json')

        # Inicializamos una variable en 0 para el contador y una lista vacia
        a = 0
        aprendiz = []
        idAprendiz = []
        # Recorremos todos los estudiantes
        for sKey, sValue in fileJson['student'].items():
            # Contador para buscar el valor
            a +=1
            count = str(a)
            # Obtenemos el id
            idAprendiz.append(sKey)
            # Obtenemos el valor/Nombre del aprendiz
            aprendiz.append(sValue[count][0])
        # Creamos una lista vacia
        asistencia = []
        # Recorremos todos las asistencias
        for aList in fileJson['attendance'].values:
            # Evaluamos si la fecha obtenida es igual que buscaremos
            try:
                # [K] corresponde a fecha y [V] al id del aprendiz
                for k,value in aList.items():
                    if fecha == k:
                        for v in value.keys():
                            asistencia.append(int(v))
            except:
                pass
        
        # Creamos una lista para guardar la asistencia
        asistenciaAprendiz = []
        for id in idAprendiz:
            # Evaluamos si el id esta en la asistencia
            if id in asistencia:
                asistenciaAprendiz.append("Presente")
            else:
                asistenciaAprendiz.append('No vino')
        
        
        data = {
            'Nombre Aprendiz' : aprendiz,
            'Asistencia' : asistenciaAprendiz
        }
        
        
        # Columnas a mostrar en el excel
        # Convertimos el diccionario a un DataFrame
        excelAsistencia = pd.DataFrame.from_dict(data)
        return excelAsistencia

    # Funcion para mostrar la asistencia
    def mostrarAsistencia(self,dataFrame):
        return dataFrame

    # Funcion para convertir el dataFrame a Excel
    def toExcel(self,dataFrame):
        try:
            dataFrame.to_excel(f'../template/asistenciaFicha{self.ficha}.xlsx')
            print('Excel exportado correctamente')
        except:
            print('Hubo un error exportado el archivo Excel')

    def toHtml(self,dataFrame):
        try:
            html_string = """
            {{% load static %}}
            <html>
                <head><title>Asisteencia</title>
                    <link rel="stylesheet" type="text/css" href="{{% static 'asistencia/css/tables.css'%}}"/>
                </head>
                <body>
                    {table}
                </body>
                </html>.
            """
            text_file = open("../template/asistenciaFicha.html", "w")
            text_file.write(html_string.format(table=dataFrame.to_html()))
            text_file.close()
            print('HTML exportado correctamente')
        except:
            print('Hubo un error exportado el archivo html')
