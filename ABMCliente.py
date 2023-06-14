from FrameMenu import VentanaRedimencionar as Ventana
from tkinter import ttk
from Datos.ConectorMysql   import Cursor
from tkinter import *


def EditarCliente(id):
      query=f"SELECT * FROM wisemendb_saller.clientes where Idcliente={id}"
      result=Cursor.Query(query)
      print(result)


class ABMClientes():

    def funcion(cliente,id=0):
             win=Toplevel()
             win.title(f"Cliente {cliente} ")
             win.geometry("1000x500")
             win.config(relief="solid")
             win.config(background="#958235")

             menubar = Menu(win)
             win.config(menu=menubar)
             menuarchivo=("Clientes","Abrir","Guardar","Cerrar")
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

             framadatosabm=Frame(win)
             Label(framadatosabm, text='Nombre').grid(row=0,column=0)
             Label(framadatosabm, text='Apellido').grid(row=0,column=1)
             Label(framadatosabm, text='Dni').grid(row=0,column=2)
             Label(framadatosabm, text='Telefono').grid(row=0,column=3)
             Label(framadatosabm, text='Provincias').grid(row=2,column=0)
             Label(framadatosabm, text='Localidad').grid(row=2,column=1)
             Label(framadatosabm, text='Genero').grid(row=2,column=2)
             Label(framadatosabm, text='Direccion').grid(row=4,column=0)

             Label(framadatosabm, text='Numero').grid(row=4,column=1)
             Label(framadatosabm, text='Piso').grid(row=4,column=2)
             Label(framadatosabm, text='CP').grid(row=4,column=3)
             TextoNombre = Entry(framadatosabm)
             TextoApellido = Entry(framadatosabm)
             TextoDni = Entry(framadatosabm)
             TextoTelefono = Entry(framadatosabm)
             TxtoDireccion = Entry(framadatosabm)
             Txtonumero = Entry(framadatosabm)
             Txtopiso = Entry(framadatosabm)
             Textocp = Entry(framadatosabm)
             
             TextoNombre.grid(row=1, column=0)
             TextoApellido.grid(row=1, column=1)
             TextoDni.grid(row=1, column=2)
             TextoTelefono.grid(row=1, column=3)
             TxtoDireccion.grid(row=5,column=0)

             Txtonumero.grid(row=5,column=1)
             Txtopiso.grid(row=5,column=2)
             Textocp.grid(row=5,column=3)

             comboProvincias = ttk.Combobox(framadatosabm,values=["Python", "C", "C++", "Java"],width=17)
             comboProvincias.current(0)
             comboProvincias.grid(row=3,column=0,sticky=W)

             comboLocalidad = ttk.Combobox(framadatosabm,values=["Python", "C", "C++", "Java"],width=17)
             comboLocalidad.current(0)
             comboLocalidad.grid(row=3,column=1,sticky=W)

             combogenero = ttk.Combobox(framadatosabm,values=["Masculino", "Femenino", "Otro"],width=17)
             combogenero.current(0)
             combogenero.grid(row=3,column=2,sticky=W)
             #combo.place(x=150, y=150)
             framadatosabm.pack()
             framadatosabm.mainloop
         

             EditarCliente(id)
             #vent = Ventana(win)
             #vent.pack(fill=BOTH, expand=YES)