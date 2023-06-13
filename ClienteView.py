from tkinter import *
from tkinter import messagebox as MensajeBox
from tkinter import colorchooser as colorBox
from tkinter import filedialog as FileBox
from FrameMenu import VentanaRedimencionar as Ventana
from Datos.ConectorMysql   import Cursor
from tkinter import ttk





def LoadClientes():
            result=Cursor.Query(queryLoad,True)
            
            print(result)
            return result
class ClienteView():
    global queryLoad
    queryLoad="SELECT Idcliente,Nombre,Apellido,Dni,Telefono,Ge.texto,Em.email,Dire.direccion,Dire.CP,Pro.texto as Provincia,Loca.texto as Localidad,Habilitado FROM wisemendb_saller.clientes as CLi inner join genero  as Ge on CLi.idGenero=Ge.id inner join email as Em on CLi.idEmail=Em.idemail inner join direccion as Dire on CLi.idDireccion=Dire.idDireccion inner join provinciaswise as Pro on Dire.idProvincia=Pro.id inner join localidadeswise as Loca on Dire.idLocalidad=Loca.id ;"

        
       
        
    def funcion():
            win=Toplevel()
            win.title("Modulo Cliente")
            win.geometry("1000x500")
            win.config(relief="solid")
            win.config(background="#958235")

            menubar = Menu(win)
            win.config(menu=menubar)

            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo Cliente")
            filemenu.add_command(label="Editar cliente")
            filemenu.add_command(label="Eliminar Cliente ")
            filemenu.add_command(label="Cerrar")
            filemenu.add_separator()
            filemenu.add_command(label="Salir", command=win.quit)
            tabla=LoadClientes()
            s = ttk.Style()
            s.theme_use('clam')

            frame=Frame(win)
            h = Scrollbar(frame, orient = 'horizontal')
  

            h.pack(side = BOTTOM, fill = X)
            tree = ttk.Treeview(frame, column=("IdCliente", "Nombre", "Apellido", "DNI","Telefono","Email","Direccion","CP","Provincia","Localidad","Habilitado"), show='headings', height=5)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="IdCliente")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="Nombre")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="Apellido")
            tree.column("# 4", anchor=CENTER)
            tree.heading("# 4", text="DNI")
            tree.column("# 5", anchor=CENTER)
            tree.heading("# 5", text="Telefono")

            tree.column("# 6", anchor=CENTER)
            tree.heading("# 6", text="Genero")

            tree.column("# 7", anchor=CENTER)
            tree.heading("# 7", text="Email")

            tree.column("# 8", anchor=CENTER)
            tree.heading("# 8", text="Direccion")

            tree.column("# 9", anchor=CENTER)
            tree.heading("# 9", text="CP")

            tree.column("# 10", anchor=CENTER)
            tree.heading("# 10", text="Provincia")

            tree.column("# 11", anchor=CENTER)
            tree.heading("# 11", text="Localidad")

            #tree.column("# 12", anchor=CENTER)
            #tree.heading("# 12", text="Habilitado")




            #listbox = Listbox(win, width=200, height=200,selectforeground="#ffffff",selectbackground="#00aa00",selectborderwidth=5)
            #listbox.pack()
            #headers = ["IdCliente", "Nombre", "Apellido", "DNI","Telefono","Email","Direccion","CP","Provincia","Localidad","Habilitado"]

            #row_format ="{:8}{sp}{:5}{sp}{:30}{sp}{:20}{sp}{:20}{sp}{:20}{sp}{:20}{sp}{:20}{sp}{:20}{sp}{:20}{sp}{:20}"
            #listbox.insert(0, row_format.format(*headers, sp=" "*15))

            def habilitado(a):
                if a==1:
                    return  "habilitado"
                else: 
                    return("Desafectado")
            for items in tabla:
                print(items)
                #istbox.insert(END, row_format.format(*items, sp=" "*5))
                #listbox.insert(END,str(f"{items[00]:<20}{items[1]:<45}{items[2]:>7},{items[3]:<35},{items[4]},{items[5]},{items[6]},{items[7]}"))
                #listbox.insert(END,str(f"{items[00]:<10}{items[1]:45}{items[2]:<45},{items[3]:45},{items[4]},{items[5]},{items[6]},{items[7]}"))
                tree.insert('', 'end', text=str(items[00]), values=(str(items[00]),str(items[1]),str(items[2]),str(items[3]),str(items[4]),str(items[5]),str(items[6]),str(items[7]),str(items[8]),str(items[9]),str(items[10]),str(items[11])))
            
            
           
            tree.pack()
            frame.pack()
            #vent = Ventana(win)
            #vent.pack(fill=BOTH, expand=YES)
    
