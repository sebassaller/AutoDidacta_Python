from tkinter import *
from tkinter import messagebox as MensajeBox
from tkinter import colorchooser as colorBox
from tkinter import filedialog as FileBox
from FrameMenu import VentanaRedimencionar as Ventana
from Datos.ConectorMysql   import Cursor
from tkinter import ttk
from ABMCliente import ABMClientes





def LoadClientes(query,valorbool):
          cursor=Cursor()
          
          result=cursor.Query(query,valorbool)
          return result 

class ClienteView():
    global queryLoad
    global selectitem
    def __init__(self):
         self.win=Toplevel()
         self.win.title("Modulo Cliente")
         self.win.geometry("1200x500")
         self.win.config(relief="solid")
         self.win.config(background="#958235")
         self.funcion()
   
    queryLoad="SELECT Idcliente,Nombre,Apellido,Dni,Telefono,Ge.texto,Em.email,Dire.direccion,Dire.CP,Pro.texto as Provincia,Loca.texto as Localidad,Habilitado FROM wisemendb_saller.clientes as CLi inner join genero  as Ge on CLi.idGenero=Ge.id inner join email as Em on CLi.idEmail=Em.idemail inner join direccion as Dire on CLi.idDireccion=Dire.idDireccion inner join provinciaswise as Pro on Dire.idProvincia=Pro.id inner join localidadeswise as Loca on Dire.idLocalidad=Loca.id ;"
    def funcion(self):
            global idCliente
            global Dni
            global Email
            global Clientehabilitado
            idCliente=IntVar()
            Dni=StringVar()
            Email=StringVar()
            Clientehabilitado=StringVar()



            menubar = Menu(self.win)
            self.win.config(menu=menubar)
            label=Label(self.win)#image=imagen#)
            label.pack(anchor="center")
            label.config(fg="#217434", bg="#518CAD",font=("Comic Sans MS",24,"bold"),text="pantalla Cliente")
            frameboton=Frame(self.win)
            def Seleccion():
                item=tree.selection()[0]
                selectitem=tree.item(item)#['text']
                id=int(selectitem['text'])
                client=f"{selectitem['values'][1]}-{selectitem['values'][2]}"
                idCliente.set(int(selectitem['text']))
                Dni.set(selectitem['values'][3])
                Email.set(selectitem['values'][6])
                Clientehabilitado.set(selectitem['values'][11])
                if selectitem['values'][11]=="habilitado":
                   Entry(frameboton,background="green").grid(row=3,column=3)
                else:
                    Entry(frameboton,background="red").grid(row=3,column=3)

            def EliminarCliente():
                valor=MensajeBox.askyesno(message="¿Desea eliminar el cliente?",title="Eliminar Cliente")
                if valor==True:
                    if idCliente.get()==0:
                      return  MensajeBox.showerror(message="Debe Seleccionar un cliente para continuar",title="Error")
                    else:
                        cursor=Cursor()
                        e=cursor.insertar(f"DELETE FROM `wisemendb_saller`.`clientes` WHERE (`Idcliente` = '{idCliente.get()}');")
                        print(e)
                        self.win.withdraw()
                        ClienteView()
                

               
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo Cliente")
            filemenu.add_command(label="Editar cliente")
            filemenu.add_command(label="Eliminar Cliente")
            filemenu.add_command(label="Cerrar")
            filemenu.add_separator()
            filemenu.add_command(label="Salir", command=self.win.quit)
            
            frame=Frame(self.win)
            
            s = ttk.Style()
            s.theme_use('clam')
            colubnas=("IdCliente", "Nombre", "Apellido", "DNI","Telefono","Genero","Email","Direccion","CP","Provincia","Localidad","Habilitado")
            tree = ttk.Treeview(frame, column=colubnas, show='headings', height=5,selectmode='browse')
            contador=0
            def habilitado(a):
                if a==1:
                    return  "habilitado"
                else: 
                    return("Desafectado")
            for item in list(colubnas):
                print(item,item.index)
                tree.column(f'#{str(contador)}',width=90, anchor=CENTER)
                tree.heading(str(contador), text=str(item),anchor=CENTER)
                contador +=1
            tabla=LoadClientes(queryLoad,True)
            for items in tabla:
                tree.insert('', 'end', text=str(items[00]), values=(str(items[00]),str(items[1]),str(items[2]),str(items[3]),str(items[4]),str(items[5]),str(items[6]),str(items[7]),str(items[8]),str(items[9]),str(items[10]),habilitado(int(items[11]))))
            
            scrollbar=Scrollbar(frame,orient="vertical", command=tree.yview)
            scrollbar.pack(side=RIGHT,fill=Y)


            tree.place(x=30,y=95)
            tree.config(yscrollcommand=scrollbar.set)

            tree.pack()
            frame.config(pady=10)
            frame.config(width="900", height="150")
            frame.pack(expand=1)             

            Button(frameboton,text="Nuevo Cliente",bg="#3BC2CD",fg="white",command=lambda:ABMClientes("Nuevo Cliente",0)).grid(row=1,column=0)
            Button(frameboton,text="Editar Cliente",bg="#3BC2CD",fg="white").grid(row=1,column=1)
            Button(frameboton,text="Eliminar Cliente",bg="#F0A448",fg="white",command=EliminarCliente).grid(row=1,column=2)
            Button(frameboton,text="Seleccionar Cliente",command=Seleccion,bg="#289426",fg="white").grid(row=1,column=3)
            Label(frameboton,text='Id Cliete',background="#958235").grid(row=2,column=0)
            Label(frameboton,text='DNI Cliete',background="#958235").grid(row=2,column=1)
            Label(frameboton,text='Email',background="#958235").grid(row=2,column=2)
            Label(frameboton,text='Habilitado',background="#958235").grid(row=2,column=3)
            Entry(frameboton ,textvariable=idCliente).grid(row=3,column=0)
            Entry(frameboton,textvariable=Dni).grid(row=3,column=1)
            Entry(frameboton,textvariable=Email).grid(row=3,column=2)
            Entry(frameboton,textvariable=Clientehabilitado).grid(row=3,column=3)

            frameboton.config(bg="#958235")
            frameboton.config(relief="sunken")
            frameboton.config(width="500", height="50")
            frameboton.pack(expand=1) 
           
            #vent = Ventana(win)
            #vent.pack(fill=BOTH, expand=YES)
