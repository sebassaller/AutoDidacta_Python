from Datos.ConectorMysql   import Cursor

class DatosDireccion:
    def __init__(self,Accion,direccion,numero,idprovincia,idlocalidad,CP,piso):
        self.Accion=Accion
        self.direccion=direccion
        self.numero=numero
        self.idprovincia=idprovincia
        self.idlocalidad=idlocalidad
        self.cp=CP
        self.piso=piso
    def MetodoAccion(self):
            if self.Accion==True:
                print("es verdadero asi que va a agregar")
                query=f"INSERT INTO wisemendb_saller.direccion (direccion,numero,idProvincia,idLocalidad,CP,piso)VALUES ('{self.direccion}',{self.numero},{self.idprovincia},{self.idlocalidad},{self.cp},'{self.piso}');"
                print(query)
                cursa=Cursor()
                result=cursa.insertar(query)
                return result
            else:
                print("Es falso asi que va a editar")
 



    