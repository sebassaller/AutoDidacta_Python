from Datos.ConectorMysql   import Cursor
from Datos.DatosDireccion import DatosDireccion as Direccion


class DatosClientes(Direccion):
    def __init__(self, Accion, direccion, numero, idprovincia, idlocalidad, CP, piso):
        super().__init__(Accion, direccion, numero, idprovincia, idlocalidad, CP, piso)

    def Accion(self):
        Direccion(self.Accion,self.direccion,self.numero,self.idprovincia,self.idlocalidad,self.cp,self.piso)
        re=Direccion.MetodoAccion()





        
