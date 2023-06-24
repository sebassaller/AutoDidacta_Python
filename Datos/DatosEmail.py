from Datos.ConectorMysql   import Cursor

class DatosEmail:
    def __init__(self,Accion=None,email=None,Tipopersona=None):
        self.email=email
        self.Tipopersona=Tipopersona
        self.Accion=Accion
        self.cursor=Cursor()
    def MetodoAccion(self):
        Existe=self.cursor.Query(f"select idemail from wisemendb_saller.email where email='{self.email}' and TipoPersona={self.Tipopersona}")
        if Existe is not None:
                    return Existe[0]
        if self.Accion==True:
          query=f"INSERT INTO wisemendb_saller.email(email,TipoPersona)VALUES ('{self.email}',{self.Tipopersona});"
          result=self.cursor.insertar(query)
          self.cursor.connectio.close()
          self.cursor.cursor.close()
          return result
        else:
            print("Es falso asi que va a editar")
