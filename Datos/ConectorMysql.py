
import mysql.connector
    
#global connection
#connectio=mysql.connector.connect(host='localhost',port=3306,user='root',password='jpjpc0789',db='wisemendb_saller')

class Cursor():
    def __init__(self):
        self.connectio=mysql.connector.connect(host='localhost',port=3306,user='root',password='jpjpc0789',db='wisemendb_saller')
        self.cursor=self.connectio.cursor() 

    def Query(self,query,filas=False):
        try:

            #connectio=mysql.connector.connect(host='localhost',port=3306,user='root',password='jpjpc0789',db='wisemendb_saller')
            #if self.connectio.is_connected():
                print("conexion exitosa")
                info_server=self.connectio.get_server_info()
                print(info_server)
                #cursor=self.connectio.cursor()
                #row=cursor.execute("SELECT * FROM wisemendb_saller.clientes")

                row=self.cursor.execute(query)
      

                if filas==False:
                    row=self.cursor.fetchone()# trae un solo registro de la base de datos
                else:
                     row=self.cursor.fetchall()# trae la consulta selecionada

                return row
        except Exception as ex:
              return  str(ex)
        finally:
            if self.connectio.is_connected():
               self.connectio.close()
               self.cursor.close()

    def insertar(self,query):
            try:
                  if self.connectio.is_connected():
                    #cursor=self.connectio.cursor()
                    row=self.cursor.execute(query)
                    self.connectio.commit()
                    #row=cursor.fetchall()# trae la consulta selecionada
                    return row
            except Exception as ex:
              return  str(ex)
            finally:
                if self.connectio.is_connected():
                   self.connectio.close()




        