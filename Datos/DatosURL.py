from Datos.ConectorMysql   import Cursor

class DatosURL:
    def __init__(self,URL,IdRedsocial):
        self.URL=URL
        self.IdResocial=IdRedsocial
        self.cursor=Cursor()
    def MetodoAccion(self,Accion,idUrl=0):
        Existe=self.cursor.Query(f"SELECT  IdURLSocial FROM wisemendb_saller.direccionredsocial where URL='{self.URL}'")
        if Existe is not None:
                    return Existe[0]
        if Accion==True:
          query=f"INSERT INTO wisemendb_saller.direccionredsocial(URL,IdRedSocial)VALUES ('{self.URL}',{self.IdResocial});"
          result=self.cursor.insertar(query)
          self.cursor.connectio.close()
          self.cursor.cursor.close()
          return result
        else:
          query=f"update  direccionredsocial set URl='{self.URL}',IdRedSocial={self.IdResocial} where IdURLSocial={idUrl}"
          result=self.cursor.insertar(query)
          self.cursor.connectio.close()
          self.cursor.cursor.close()
          return result
