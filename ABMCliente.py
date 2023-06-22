from FrameMenu import VentanaRedimencionar as Ventana
from tkinter import ttk
from Datos.ConectorMysql   import Cursor
from Datos.DatosClientes import DatosClientes as DatoCliente
from Datos.DatosProvinciaYLocalidad import SeachProvinciaLocalidad as seachubucacion
from tkinter import *


def EditarCliente(id):
      query=f"SELECT * FROM wisemendb_saller.clientes where Idcliente={id}"
      result=Cursor.Query(query)
      print(result)


def ubicacion(pro,lo):
   ubuca=seachubucacion(pro,lo)
   return ubuca.ReturnIdProviniciaIdLocalidad()



class ABMClientes():
    def funcion(cliente,id=0):
             global Direccion
             global numero

             global CodigoPostal
             global Piso
             Direccion=StringVar()
             numero=IntVar()

             CodigoPostal=IntVar()
             Piso=StringVar()
       
             win=Toplevel()
             win.title(f"Cliente {cliente} ")
             win.geometry("1000x500")
             win.config(relief="solid")
             win.config(background="#958235")

             menubar = Menu(win)
             win.config(menu=menubar)
             menuarchivo=["Clientes","Abrir","Guardar","Cerrar"]
             menueditar=("Cortar","Copiar","Pegar")
            
             filemenu = Menu(menubar, tearoff=0)
           
             for menuarchi in list(menuarchivo):
                filemenu.add_command(label=str(menuarchi),command="")
             filemenu.add_separator()
             filemenu.add_command(label="Salir", command=win.quit)

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
               idprovincia=[item for item in list(Cursor.Query(f"SELECT id FROM wisemendb_saller.provinciaswise where texto='{comboProvincias.get()}'"))]
               Listalocalidad=[item for item in list(Cursor.Query(f"SELECT * FROM wisemendb_saller.localidadeswise where idprovincia={idprovincia[0]}",True))]
               comboLocalidad['values']=['']
               comboLocalidad['values']=[item[2] for item in list(Listalocalidad)]
             def EnviarDatosCliente():
                  SendDatos={'Direccion':[Direccion.get(),numero.get(),Piso.get(),CodigoPostal.get() ]}
                  print(SendDatos['Direccion'])
                  result=ubicacion(comboProvincias.get(),comboLocalidad.get())
                  print(result)
                  cli=DatoCliente(True,Direccion.get(),numero.get(),result['idprovincia'][0],result['idlocalidad'][0],CodigoPostal.get(),Piso.get())
                  cli.Accion()
               

             framadatosabm=Frame(win)
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



             TextoNombre = Entry(framadatosabm)
             TextoApellido = Entry(framadatosabm)
             TextoDni = Entry(framadatosabm)
             TextoTelefono = Entry(framadatosabm)

             TxtoDireccion = Entry(framadatosabm,textvariable=Direccion)
             Txtonumero = Entry(framadatosabm,textvariable=numero)
             Txtopiso = Entry(framadatosabm,textvariable=Piso)
             Textocp = Entry(framadatosabm,textvariable=CodigoPostal)
             
             TextoEmail = Entry(framadatosabm)
             TextoUrl = Entry(framadatosabm)
             
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
             listaProvincia=[item for (n,item) in list(Cursor.Query("SELECT * FROM wisemendb_saller.provinciaswise",True))]
             comboProvincias = ttk.Combobox(framadatosabm,values=listaProvincia,width=17)
             comboProvincias.current(0)
             comboProvincias.grid(row=3,column=0,sticky=W)
             Button(framadatosabm,text="seleccionar Provincia",bg='gold',command=locals()['TraerLocalidad'] ).grid(row=4,column=0)

             comboLocalidad = ttk.Combobox(framadatosabm,values=[""],width=17)
             comboLocalidad.current(0)
             comboLocalidad.grid(row=3,column=1,sticky=W)

             combogenero = ttk.Combobox(framadatosabm,values=[item for (n,item) in list(Cursor.Query("SELECT * FROM wisemendb_saller.genero",True))],width=17)
             combogenero.current(0)
             combogenero.grid(row=3,column=2,sticky=W)


             comboemail = ttk.Combobox(framadatosabm,values=[item for (n,item) in list(Cursor.Query("SELECT * FROM wisemendb_saller.tiposdecorreos",True))],width=17)
             comboemail .current(0)
             comboemail .grid(row=8,column=1,sticky=W)


             Button(framadatosabm,text="Guardar",bg='SteelBlue1',command=locals()['EnviarDatosCliente']).grid(row=9,column=1)
             Button(framadatosabm,text="Cancelar",bg='Khaki',command="" ).grid(row=9,column=2)
             #combo.place(x=150, y=150)

             framadatosabm.grid(row=0,column=1)
             framadatosabm.pack()
             framadatosabm.mainloop
         

             EditarCliente(id)
             #vent = Ventana(win)
             #vent.pack(fill=BOTH, expand=YES)