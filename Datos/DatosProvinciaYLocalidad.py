from Datos.ConectorMysql   import Cursor
class SeachProvinciaLocalidad:
    def __init__(self,Provincia,Localidad):
        self.Provincia=Provincia
        self.Localidad=Localidad
    def ReturnIdProviniciaIdLocalidad(self):
            cursor1=Cursor() 
            idprovincia=[item for item in list(cursor1.Query(f"SELECT id FROM wisemendb_saller.provinciaswise where texto='{self.Provincia}'"))]
            cursor2=Cursor()
            idlocalidad=[item for item in list(cursor2.Query(f"SELECT id  FROM wisemendb_saller.localidadeswise where texto='{self.Localidad}'and idprovincia={idprovincia[0]}"))]
            return {'idprovincia':idprovincia,'idlocalidad':idlocalidad}


        
