
import mysql.connector

class Cursor():
    def __init__(self):
        self.connectio=mysql.connector.connect(host='localhost',port=3306,user='root',password='jpjpc0789',db='wisemendb_saller')
        self.cursor=self.connectio.cursor() 
        self.info_server=self.connectio.get_server_info()

    def Query(self,query,filas=False):
        try:
            if self.connectio.is_connected():
                print("conexion exitosa")
                row=self.cursor.execute(query)
                if filas==False:
                    row=self.cursor.fetchone()# trae un solo registro de la base de datos
                else:
                     row=self.cursor.fetchall()# trae la consulta selecionada

                return row
        except Exception as ex:
              return  str(ex)


    def insertar(self,query):
            try:
                  if self.connectio.is_connected():
                    self.cursor.execute(query)
                    self.connectio.commit()
                    row=self.cursor.lastrowid
                    return row
            except Exception as ex:
              return  str(ex)





        