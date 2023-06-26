from FrameMenu import VentanaRedimencionar as Ventana
from tkinter import ttk
from Datos.ConectorMysql   import Cursor
from Datos.DatosClientes import DatosClientes as Cliente
from Datos.DatosCombos import SeachCombos as TraerIdCombos
from Datos.DatosDireccion import DatosDireccion as Direccion
from Datos.DatosEmail import DatosEmail as Email
from Datos.DatosURL import DatosURL as URL
from tkinter import *


def EditarCliente(id):
      cursor=Cursor()
      result=cursor.Query(f"SELECT * FROM wisemendb_saller.clientes where Idcliente={id}")
      cursor.connectio.close()
      cursor.cursor.close()
      print(result)


def Idcombos(provincia,localidad,genero,redsocial):
   IdCombos=TraerIdCombos()

   idubicacion=IdCombos.ReturnIdProviniciaIdLocalidad(provincia,localidad)
   idgenero=IdCombos.ReturnIDCombosGenero(genero)
   idRedsocial=IdCombos.ReturnIdRedSocial(redsocial)
   return (idubicacion,idgenero,idRedsocial)




class ABMClientes:
      def __init__(self,cliente,idcliente):
            self.cliente=cliente
            self.idcliente=idcliente
            self.cursor=Cursor()
            self.win=Toplevel()
            self.win.title(f"Cliente {cliente} ")
            self.win.resizable(0,0)
            self.win.geometry("600x400")
            self.win.config(relief="solid")
            self.win.config(background="#958235")
            self.funcion()


      def funcion(self):
             global direccion
             global numero
             global CodigoPostal
             global Piso
             global email
             global textoURL
             global nombre
             global apellido
             global DNIcliente
             global telefono

             nombre=StringVar()
             apellido=StringVar()
             DNIcliente=StringVar()
             telefono=StringVar()

             textoURL=StringVar()
             email=StringVar()
             direccion=StringVar()
             numero=IntVar()
             CodigoPostal=IntVar()
             Piso=StringVar()
           

             menubar = Menu(self.win)
             self.win.config(menu=menubar)
             menuarchivo=["Clientes","Abrir","Guardar","Cerrar"]
             menueditar=("Cortar","Copiar","Pegar")
            
             filemenu = Menu(menubar, tearoff=0)
           
             for menuarchi in list(menuarchivo):
                filemenu.add_command(label=str(menuarchi),command="")
             filemenu.add_separator()
             filemenu.add_command(label="Salir", command=self.win.quit)

             editmenu = Menu(menubar, tearoff=0)
             for menuedi in list(menueditar):
                editmenu.add_command(label=str(menuedi),command="")

             helpmenu = Menu(menubar, tearoff=0)
             helpmenu.add_command(label="Ayuda")
             helpmenu.add_separator()
             helpmenu.add_command(label="Acerca de...")

             menubar.add_cascade(label="Archivo", menu=filemenu)
             menubar.add_cascade(label="Editar", menu=editmenu)
             menubar.add_cascade(label="Ayuda", menu=helpmenu)
         
             def TraerLocalidad():
               cura=Cursor()
               idprovincia=[item for item in list(cura.Query(f"SELECT id FROM wisemendb_saller.provinciaswise where texto='{comboProvincias.get()}'"))]
               Listalocalidad=[item for item in list(cura.Query(f"SELECT * FROM wisemendb_saller.localidadeswise where idprovincia={idprovincia[0]}",True))]
               comboLocalidad['values']=['']
               comboLocalidad['values']=[item[2] for item in list(Listalocalidad)]
               cura.connectio.close()
               cura.cursor.close()

             def EnviarDatosCliente():
                  combosid= Idcombos(comboProvincias.get(),comboLocalidad.get(),combogenero.get(),comboredsocial.get())
                  Direc=Direccion(True,direccion.get(),numero.get(),combosid[0]['idprovincia'][0],combosid[0]['idlocalidad'][0],CodigoPostal.get(),Piso.get())
                  iddireccion=Direc.MetodoAccion()
                  emailarmado=email.get()+comboemail.get()
                  instanciaemail=Email(True,emailarmado,1)
                  resulemail=instanciaemail.MetodoAccion()

                  url=URL(textoURL.get(),combosid[2]['idRedsocial'][0])
                  idUrl=url.MetodoAccion(True)
                  cli=Cliente(nombre.get(),apellido.get(),DNIcliente.get(),resulemail,iddireccion,idUrl,combosid[1]['idgenero'][0],telefono.get())
                  cli.MetodoAccion(True)
               

             framadatosabm=Frame(self.win)
             Label(framadatosabm, text='Nombre').grid(row=0,column=0)
             Label(framadatosabm, text='Apellido').grid(row=0,column=1)
             Label(framadatosabm, text='Dni').grid(row=0,column=2)
             Label(framadatosabm, text='Telefono').grid(row=0,column=3)

             Label(framadatosabm, text='Provincias').grid(row=2,column=0)
             Label(framadatosabm, text='Localidad').grid(row=2,column=1)
             Label(framadatosabm, text='Genero').grid(row=2,column=2)
             
             Label(framadatosabm, text='Direccion').grid(row=5,column=0)
             Label(framadatosabm, text='Numero').grid(row=5,column=1)
             Label(framadatosabm, text='Piso').grid(row=5,column=2)
             Label(framadatosabm, text='CP').grid(row=5,column=3)


             Label(framadatosabm, text='Email').grid(row=7,column=0)
             Label(framadatosabm, text='Termino Email').grid(row=7,column=1)
             Label(framadatosabm, text='Direccion Url').grid(row=7,column=2)
             Label(framadatosabm, text='Combo Red Social').grid(row=7,column=3)

             TextoNombre = Entry(framadatosabm,textvariable=nombre)
             TextoApellido = Entry(framadatosabm,textvariable=apellido)
             TextoDni = Entry(framadatosabm,textvariable=DNIcliente)
             TextoTelefono = Entry(framadatosabm,textvariable=telefono)

             TxtoDireccion = Entry(framadatosabm,textvariable=direccion)
             Txtonumero = Entry(framadatosabm,textvariable=numero)
             Txtopiso = Entry(framadatosabm,textvariable=Piso)
             Textocp = Entry(framadatosabm,textvariable=CodigoPostal)
             
             TextoEmail = Entry(framadatosabm,textvariable=email)
             TextoUrl = Entry(framadatosabm,textvariable=textoURL)
             
             TextoNombre.grid(row=1, column=0)
             TextoApellido.grid(row=1, column=1)
             TextoDni.grid(row=1, column=2)
             TextoTelefono.grid(row=1, column=3)
             TxtoDireccion.grid(row=6,column=0)

             TextoEmail.grid(row=8,column=0)
             TextoUrl.grid(row=8,column=2)

             Txtonumero.grid(row=6,column=1)
             Txtopiso.grid(row=6,column=2)
             Textocp.grid(row=6,column=3)
             
             listaProvincia=[item for (n,item) in list(self.cursor.Query("SELECT * FROM wisemendb_saller.provinciaswise",True))]
             comboProvincias = ttk.Combobox(framadatosabm,values=listaProvincia,width=17)
             comboProvincias.current(0)
             comboProvincias.grid(row=3,column=0,sticky=W)
             Button(framadatosabm,text="seleccionar Provincia",bg='gold',command=locals()['TraerLocalidad'] ).grid(row=4,column=0)

             comboLocalidad = ttk.Combobox(framadatosabm,values=[""],width=17)
             comboLocalidad.current(0)
             comboLocalidad.grid(row=3,column=1,sticky=W)
            
             combogenero = ttk.Combobox(framadatosabm,values=[item for (n,item) in list(self.cursor.Query("SELECT * FROM wisemendb_saller.genero",True))],width=17)
             combogenero.current(0)
             combogenero.grid(row=3,column=2,sticky=W)

             comboemail = ttk.Combobox(framadatosabm,values=[item for (n,item) in list(self.cursor.Query("SELECT * FROM wisemendb_saller.tiposdecorreos",True))],width=17)
             comboemail .current(0)
             comboemail .grid(row=8,column=1,sticky=W)

             comboredsocial = ttk.Combobox(framadatosabm,values=[item for (n,item) in list(self.cursor.Query("SELECT *  FROM wisemendb_saller.redsocial",True))],width=17)
             comboredsocial.current(0)
             comboredsocial.grid(row=8,column=3,sticky=W)

             Button(framadatosabm,text="Guardar",bg='SteelBlue1',command=locals()['EnviarDatosCliente']).grid(row=9,column=1)
             Button(framadatosabm,text="Cancelar",bg='Khaki',command="" ).grid(row=9,column=2)
             #combo.place(x=150, y=150)
             self.cursor.connectio.close()
             self.cursor.cursor.close()

             framadatosabm.grid(row=0,column=1)
             framadatosabm.config(bd=25)
             framadatosabm.pack(fill=BOTH,expand=False,pady=20,padx=20)
             #framadatosabm.mainloop
         

             EditarCliente(self.idcliente)
             #vent = Ventana(self.win)
             #vent.pack(fill=BOTH, expand=YES)
