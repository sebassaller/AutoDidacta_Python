from Datos.ConectorMysql   import Cursor
from Datos.DatosDireccion import DatosDireccion as Direccion


class DatosClientes():
    def __init__(self,nombre,apellido,DNI,Idemail,Iddireccion,IdURL,IdGenero,Habilitado=0):
        self.nombre=nombre
        self.apellido=apellido
        self.DNI=DNI
        self.Idemail=Idemail
        self.Iddireccion=Iddireccion
        self.IdURL=IdURL
        self.Idgenero=IdGenero
        self.Habilitado=Habilitado


        


    #def Accion(self):
    #    Direccion(self.Accion,self.direccion,self.numero,self.idprovincia,self.idlocalidad,self.cp,self.piso)
    #    re=Direccion.MetodoAccion()





        
