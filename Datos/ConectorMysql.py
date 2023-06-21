
import mysql.connector


class Cursor():
    def Query(query,filas=False):
        try:
            connectio=mysql.connector.connect(host='localhost',port=3306,user='root',password='jpjpc0789',db='wisemendb_saller')
            if connectio.is_connected():
                print("conexion exitosa")
                info_server=connectio.get_server_info()
                print(info_server)
                cursor=connectio.cursor()
                #row=cursor.execute("SELECT * FROM wisemendb_saller.clientes")
                row=cursor.execute(query)

                if filas==False:
                    row=cursor.fetchone()# trae un solo registro de la base de datos
                else:
                     row=cursor.fetchall()# trae la consulta selecionada

                return row
        except Exception as ex:
              return  str(ex)
        finally:
            if connectio.is_connected():
               connectio.close()

        