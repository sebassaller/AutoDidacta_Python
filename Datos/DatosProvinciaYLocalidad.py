from Datos.ConectorMysql   import Cursor
class SeachProvinciaLocalidad:
    def __init__(self,Provincia,Localidad):
        self.Provincia=Provincia
        self.Localidad=Localidad
        self.cursor=Cursor()
    def ReturnIdProviniciaIdLocalidad(self):
            idprovincia=[item for item in list(self.cursor.Query(f"SELECT id FROM wisemendb_saller.provinciaswise where texto='{self.Provincia}'"))]
            idlocalidad=[item for item in list(self.cursor.Query(f"SELECT id  FROM wisemendb_saller.localidadeswise where texto='{self.Localidad}'and idprovincia={idprovincia[0]}"))]
            return {'idprovincia':idprovincia,'idlocalidad':idlocalidad}

    def ReturnIDCombosGenero(self,busqueda):
          query=f"SELECT id  FROM wisemendb_saller.genero where texto='{busqueda}'"
          idgenero=self.cursor.Query(query)
          return {'idgenero':idgenero}




        
