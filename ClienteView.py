from tkinter import *
from tkinter import messagebox as MensajeBox
from tkinter import colorchooser as colorBox
from tkinter import filedialog as FileBox
from FrameMenu import VentanaRedimencionar as Ventana
class ClienteView():
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
            #vent = Ventana(win)
            #vent.pack(fill=BOTH, expand=YES)
