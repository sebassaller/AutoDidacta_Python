from Datos.DatosCombos import SeachCombos as TraerIdCombos
from Datos.DatosDireccion import DatosDireccion as Direccion
from Datos.DatosEmail import DatosEmail as Email
from Datos.DatosURL import DatosURL as URL
from Datos.DatosClientes import DatosClientes as Cliente
from Datos.ConectorMysql   import Cursor
class ControllerCliente:

    @staticmethod
    def AgregarDireccionCliente(Accion,direccion,numero,idprovincia,idlocalidad,CP,piso):
        Direc=Direccion(Accion,direccion,numero,idprovincia,idlocalidad,CP,piso)
        return Direc.MetodoAccion()


    @staticmethod
    def TraerCombos(provincia,localidad,genero,redsocial):
        IdCombos=TraerIdCombos()
        idubicacion=IdCombos.ReturnIdProviniciaIdLocalidad(provincia,localidad)
        idgenero=IdCombos.ReturnIDCombosGenero(genero)
        idRedsocial=IdCombos.ReturnIdRedSocial(redsocial)
        del IdCombos
        return (idubicacion,idgenero,idRedsocial)


    @staticmethod
    def AgregarEmail(email=None,comboemail=None):
        emailarmado = email+comboemail if email !='' else None 
        if emailarmado==None:
            return None
        instanciaemail=Email(True,emailarmado,1)
        return instanciaemail.MetodoAccion()

    @staticmethod
    def AgregarUrl(textoURL,idRedsocial):
        url=URL(textoURL,idRedsocial)
        idUrl=url.MetodoAccion(True)
        del url
        return idUrl

    @staticmethod
    def AgregarCliente(nombre,apellido,DNI,Idemail,Idireccion,IdURL,IdGenero,telefono):
        cli=Cliente(nombre,apellido,DNI,Idemail,Idireccion,IdURL,IdGenero,telefono,0)
        idcli=cli.MetodoAccion(True)
        del cli
        return idcli

    @staticmethod
    def TraerListaCombo(query,valor=None):
        ListaCombo=TraerIdCombos()
        lista=ListaCombo.TraerListaCombo(query,valor)
        del ListaCombo
        return lista

    @staticmethod
    def Combos(query):
        Combos=TraerIdCombos()
        lista=Combos.TRaerCombosLista(query)
        del Combos
        return lista
    

    @staticmethod
    def TraerCliente(id):
         cursor=Cursor()
         result=cursor.Query(f"SELECT * FROM wisemendb_saller.clientes as CLi inner join genero  as Ge on CLi.idGenero=Ge.id inner join email as Em on CLi.idEmail=Em.idemail inner join direccion as Dire on CLi.idDireccion=Dire.idDireccion inner join provinciaswise as Pro on Dire.idProvincia=Pro.id inner join localidadeswise as Loca on Dire.idLocalidad=Loca.id where Idcliente={id}")
         cursor.CloseCursor()
         del cursor
         Lista={'idCliente':result[0],'nombre':result[1],'apellido':result[2],'DNI':result[3],'Telefono':result[6],'numero':result[17],'direccion':result[16]}

         return Lista




    