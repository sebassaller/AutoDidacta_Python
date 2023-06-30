from Datos.DatosCombos import SeachCombos as TraerIdCombos
from Datos.DatosDireccion import DatosDireccion as Direccion
from Datos.DatosEmail import DatosEmail as Email
from Datos.DatosURL import DatosURL as URL
from Datos.DatosClientes import DatosClientes as Cliente
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




    