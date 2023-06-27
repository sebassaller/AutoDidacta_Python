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



            menubar = Menu(self.win)
            self.win.config(menu=menubar)
            selectitem=StringVar()
            label=Label(self.win)#image=imagen#)
            label.pack(anchor="center")
            label.config(fg="#217434", bg="#518CAD",font=("Comic Sans MS",24,"bold"),text="pantalla Cliente")
            frameboton=Frame(self.win)
            def Seleccion():
                item=tree.selection()[0]
                selectitem=tree.item(item)#['text']
                id=int(selectitem['text'])
                client=f"{selectitem['values'][1]}-{selectitem['values'][2]}"
                ABMClientes(client,id)
                print(selectitem)
           
            frame=Frame(self.win)
            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo Cliente")
            filemenu.add_command(label="Editar cliente")
            filemenu.add_command(label="Eliminar Cliente")
            filemenu.add_command(label="Cerrar")
            filemenu.add_separator()
            filemenu.add_command(label="Salir", command=self.win.quit)
            tabla=LoadClientes(queryLoad,True)
            s = ttk.Style()
            s.theme_use('clam')
            colubnas=("IdCliente", "Nombre", "Apellido", "DNI","Telefono","Genero","Email","Direccion","CP","Provincia","Localidad","Habilitado")
            tree = ttk.Treeview(frame, column=colubnas, show='headings', height=5,selectmode='browse')
           
            contador=0
            for item in list(colubnas):
                print(item,item.index)
                tree.column(f'#{str(contador)}',width=90, anchor=CENTER)
                tree.heading(str(contador), text=str(item),anchor=CENTER)
                contador +=1
            def habilitado(a):
                if a==1:
                    return  "habilitado"
                else: 
                    return("Desafectado")
            for items in tabla:
                print(items)
                tree.insert('', 'end', text=str(items[00]), values=(str(items[00]),str(items[1]),str(items[2]),str(items[3]),str(items[4]),str(items[5]),str(items[6]),str(items[7]),str(items[8]),str(items[9]),str(items[10]),habilitado(int(items[11]))))
            
            scrollbar=Scrollbar(frame,orient="vertical", command=tree.yview)
            scrollbar.pack(side=RIGHT,fill=Y)


            tree.place(x=30,y=95)
            tree.config(yscrollcommand=scrollbar.set)

            tree.pack()
            frame.config(pady=10)
            frame.config(width="900", height="150")
            frame.pack(expand=1)
            Button(frameboton,text="Nuevo Cliente").grid(row=1,column=0)
            Label(frameboton, text='     ',background="#958235").grid(row=1,column=1)
            Button(frameboton,text="Editar Cliente").grid(row=1,column=2)
            Label(frameboton, text='     ',background="#958235").grid(row=1,column=3)
            Button(frameboton,text="Eliminar Cliente").grid(row=1,column=4)
            Label(frameboton, text='     ',background="#958235").grid(row=1,column=5)
            Button(frameboton,text="Seleccionar Cliente",command=Seleccion).grid(row=1,column=6)
            frameboton.config(bg="#958235")
            frameboton.config(relief="sunken")
            frameboton.config(width="500", height="50")
            frameboton.pack(expand=1) 
           
            #vent = Ventana(win)
            #vent.pack(fill=BOTH, expand=YES)
