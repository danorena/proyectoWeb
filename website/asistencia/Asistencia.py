# Instalar pandas
# instalar openpyxl
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
            text_file = open(f"../template/asistenciaFicha.html", "w")
            text_file.write(dataFrame.to_html())
            text_file.close()
            print('HTML exportado correctamente')
        except:
            print('Hubo un error exportado el archivo html')


fecha = '2022-05-11'
ficha = '01'

asistencia = Asistencia(ficha,fecha)

# asistencia.toExcel(asistencia.dataFrameAsistencia(fecha))
# print(asistencia.mostrarAsistencia(asistencia.dataFrameAsistencia(fecha)))
# asistencia.toHtml(asistencia.dataFrameAsistencia(fecha))

