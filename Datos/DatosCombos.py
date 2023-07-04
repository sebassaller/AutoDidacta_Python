from Datos.ConectorMysql   import Cursor
class SeachCombos:

    @staticmethod
    def ReturnIdProviniciaIdLocalidad(Provincia,Localidad):
            cursor=Cursor()
            idprovincia=[item for item in list(cursor.Query(f"SELECT id FROM wisemendb_saller.provinciaswise where texto='{Provincia}'"))]
            idlocalidad=[item for item in list(cursor.Query(f"SELECT id  FROM wisemendb_saller.localidadeswise where texto='{Localidad}'and idprovincia={idprovincia[0]}"))]
            cursor.CloseCursor()
            return {'idprovincia':idprovincia,'idlocalidad':idlocalidad}


    @staticmethod
    def ReturnIDCombosGenero(busqueda):
          cursor=Cursor()
          query=f"SELECT id  FROM wisemendb_saller.genero where texto='{busqueda}'"
          idgenero=cursor.Query(query)
          cursor.CloseCursor()
          del cursor
          return {'idgenero':idgenero}


    @staticmethod
    def ReturnIdRedSocial(redsocial):
          cursor=Cursor()
          query=f"SELECT id  FROM wisemendb_saller.redsocial where texto='{redsocial}';"
          idgenero=cursor.Query(query)
          cursor.CloseCursor()
          del cursor
          return {'idRedsocial':idgenero[0]}

     
    @staticmethod
    def TraerListaCombo(query,valor=None):
         cursor=Cursor()
         lista= [item for item in list(cursor.Query(query,True))]   if valor is not None else [item for item in list(cursor.Query(query))] 
         cursor.CloseCursor()
         del cursor
         return lista
    
    @staticmethod
    def TRaerCombosLista(query):
      cursor=Cursor()
      lista=[item for (n,item) in list(cursor.Query(query,True))] 
      cursor.CloseCursor()

      return lista 





        
