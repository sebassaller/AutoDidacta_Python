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
   
    queryLoad="SELECT Idcliente,Nombre,Apellido,Dni,Telefono,Ge.texto,Em.email,Dire.direccion,Dire.CP,Pro.texto as Provincia,Loca.texto as Localidad,Habilitado FROM wisemendb_saller.clientes as CLi inner join genero  as Ge on CLi.idGenero=Ge.id inner join email as Em on CLi.idEmail=Em.idemail inner join direccion as Dire on CLi.idDireccion=Dire.idDireccion inner join provinciaswise as Pro on Dire.idProvincia=Pro.id inner join localidadeswise as Loca on Dire.idLocalidad=Loca.id ;"
    def funcion():
            win=Toplevel()
            win.title("Modulo Cliente")
            win.geometry("1000x500")
            win.config(relief="solid")
            win.config(background="#958235")

            menubar = Menu(win)
            win.config(menu=menubar)
            selectitem=StringVar()
            label=Label(win)#image=imagen#)
            label.pack(anchor="center")
            label.config(fg="#217434", bg="#518CAD",font=("Comic Sans MS",24,"bold"),text="pantalla Cliente")
            frameboton=Frame(win)
            def Seleccion():
                item=tree.selection()[0]
                selectitem=tree.item(item)#['text']
                id=int(selectitem['text'])
                client=f"{selectitem['values'][1]}-{selectitem['values'][2]}"
                ABMClientes(client,id)
                
                #abmcliente.funcion()
                print(selectitem)
                
               
     
            botonnuevocliente = ttk.Button(frameboton,text="Nuevo Cliente")

            botonnuevocliente.pack()
            botoneditarcliente = ttk.Button(frameboton,text="Editar Cliente")
            botoneditarcliente.pack(anchor='w')
            botonEliminarcliente= ttk.Button(frameboton,text="Eliminar Cliente")
            botonEliminarcliente.pack()
            botonseleccionarcliente= ttk.Button(frameboton,text="Seleccionar Cliente",command=Seleccion)
            botonseleccionarcliente.pack()
            frameboton.config(bg="red")
            frameboton.pack(fill=BOTH,expand=20)

            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo Cliente")
            filemenu.add_command(label="Editar cliente")
            filemenu.add_command(label="Eliminar Cliente ")
            filemenu.add_command(label="Cerrar")
            filemenu.add_separator()
            filemenu.add_command(label="Salir", command=win.quit)
            tabla=LoadClientes(queryLoad,True)
            s = ttk.Style()
            s.theme_use('clam')
            
            frame=Frame(win)
            h = Scrollbar(frame, orient = 'horizontal')
  
            colubnas=("IdCliente", "Nombre", "Apellido", "DNI","Telefono","Genero","Email","Direccion","CP","Provincia","Localidad","Habilitado")
            h.pack(side = BOTTOM, fill = X)
            tree = ttk.Treeview(frame, column=colubnas, show='headings', height=5)
           
            contador=0
            for item in list(colubnas):
                print(item,item.index)
                tree.column(f'#{str(contador)}', anchor=CENTER)
                tree.heading(str(contador), text=str(item))
                contador +=1


            
            

            def habilitado(a):
                if a==1:
                    return  "habilitado"
                else: 
                    return("Desafectado")
            for items in tabla:
                print(items)
                tree.insert('', 'end', text=str(items[00]), values=(str(items[00]),str(items[1]),str(items[2]),str(items[3]),str(items[4]),str(items[5]),str(items[6]),str(items[7]),str(items[8]),str(items[9]),str(items[10]),habilitado(int(items[11]))))
            
            scrollbar=Scrollbar(frame)
            scrollbar.pack(side=RIGHT,fill=Y)
            tree['yscrollcommand']=scrollbar.set
            tree.pack()
            frame.pack()
            #vent = Ventana(win)
            #vent.pack(fill=BOTH, expand=YES)
    
