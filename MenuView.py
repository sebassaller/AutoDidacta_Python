from tkinter import *
from tkinter import messagebox as MensajeBox
from tkinter import colorchooser as colorBox
from tkinter import filedialog as FileBox
from FrameMenu import VentanaRedimencionar as Ventana


class CrearMenu():
    def funcion():
            win=Toplevel()
            win.title("Menu PRINCIPAL")
            win.geometry("1000x500")
            win.config(relief="solid")
            win.config(background="#958235")

            menubar = Menu(win)
            win.config(menu=menubar)

            filemenu = Menu(menubar, tearoff=0)
            filemenu.add_command(label="Nuevo")
            filemenu.add_command(label="Abrir")
            filemenu.add_command(label="Guardar")
            filemenu.add_command(label="Cerrar")
            filemenu.add_separator()
            filemenu.add_command(label="Salir", command=win.quit)

            editmenu = Menu(menubar, tearoff=0)
            editmenu.add_command(label="Cortar")
            editmenu.add_command(label="Copiar")
            editmenu.add_command(label="Pegar")


            helpmenu = Menu(menubar, tearoff=0)
            helpmenu.add_command(label="Ayuda")
            helpmenu.add_separator()
            helpmenu.add_command(label="Acerca de...")


            menubar.add_cascade(label="Archivo", menu=filemenu)
            menubar.add_cascade(label="Editar", menu=editmenu)
            menubar.add_cascade(label="Ayuda", menu=helpmenu)
            vent = Ventana(win)
            vent.pack(fill=BOTH, expand=YES)

        





        




