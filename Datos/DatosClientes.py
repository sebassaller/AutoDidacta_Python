from Datos.ConectorMysql   import Cursor
from Datos.DatosDireccion import DatosDireccion as Direccion


class DatosClientes():
    def __init__(self,nombre,apellido,DNI,Idemail,Idireccion,IdURL,IdGenero,telefono,Habilitado=0):
        self.nombre=nombre
        self.apellido=apellido
        self.DNI=DNI
        self.Idemail=Idemail
        self.Iddireccion=Idireccion
        self.IdURL=IdURL
        self.Idgenero=IdGenero
        self.Habilitado=Habilitado
        self.telefono=telefono
        self.cursor=Cursor()
    def MetodoAccion(self,Accion,Idcliente=0):
        Existe=self.cursor.Query(f"select idCliente from clientes where Nombre='{self.nombre}' and Apellido='{self.apellido}'and Dni={self.DNI}")
        if Existe is not None:
                    return "Usuario ya existe"
        if Accion==True:
          query=f"INSERT INTO wisemendb_saller.clientes(Nombre,Apellido,Dni,idEmail,idURL,telefono,idGenero,Habilitado,idDireccion)VALUES ('{self.nombre}','{self.apellido}',{self.DNI},{self.Idemail},{self.IdURL},{self.telefono},'{self.Idgenero}','{0}',{self.Iddireccion});"
          result=self.cursor.insertar(query)
          self.cursor.connectio.close()
          self.cursor.cursor.close()
          return result
        else:
          query=f"update Clientes set Nombre='{self.nombre}',Apellido='{self.apellido}',Dni='{self.DNI}',Telefono={self.telefono},idGenero={self.Idgenero} where Idcliente={Idcliente};"
          result=self.cursor.insertar(query)
          self.cursor.connectio.close()
          self.cursor.cursor.close()
          return result




    #def Accion(self):
    #    Direccion(self.Accion,self.direccion,self.numero,self.idprovincia,self.idlocalidad,self.cp,self.piso)
    #    re=Direccion.MetodoAccion()





        
