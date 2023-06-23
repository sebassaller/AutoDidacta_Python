from Datos.ConectorMysql   import Cursor

class DatosDireccion:
    def __init__(self,Accion=None,direccion=None,numero=None,idprovincia=None,idlocalidad=None,CP=None,piso=None):
        self.Accion=Accion
        self.direccion=direccion
        self.numero=numero
        self.idprovincia=idprovincia
        self.idlocalidad=idlocalidad
        self.cp=CP
        self.piso=piso
        self.cursor=Cursor()


 
    def MetodoAccion(self):
            if self.Accion==True:
                #------------es verdadero asi que va a agregar-------------------------------------
                query=f"INSERT INTO wisemendb_saller.direccion (direccion,numero,idProvincia,idLocalidad,CP,piso)VALUES ('{self.direccion}',{self.numero},{self.idprovincia},{self.idlocalidad},{self.cp},'{self.piso}');"
                Existe=self.cursor.Query(f"SELECT idDireccion FROM wisemendb_saller.direccion  where idProvincia={self.idprovincia}  and idLocalidad={self.idlocalidad} and numero={self.numero} and direccion='{self.direccion}'")
                if Existe is not None:
                    return Existe[0]

                result=self.cursor.insertar(query)
                self.cursor.connectio.close()
                self.cursor.cursor.close()
                return result
            else:
                print("Es falso asi que va a editar")
 



    