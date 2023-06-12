from tkinter import *
from tkinter import messagebox as MensajeBox
from PIL import Image, ImageTk
from tkinter import ttk
import os
from   Datos.ConectorMysql   import Cursor
from MenuView import CrearMenu as Menuvie
import getpass


root=Tk()
root.title("Login")
root.geometry("510x700")
root.config(bd=15)
root.config(relief="solid")
root.config(background="#958235")
root.resizable(0,0)
imgusuario = ImageTk.PhotoImage(Image.open(os.path.join("./IMG/", "image.png")).resize((500,325)))
Label(root,image=  imgusuario,background="#958235").pack()


class LoginView(Frame):
    global usuario
    global password
    global control
    usuario=StringVar()
    password=StringVar()
    control=IntVar()
    def __init__(self,Master=None):
        Frame.__init__(self,Master)
        def LoginCursor():
            if usuario.get()=="" or password.get()=="":
                return MensajeBox.showwarning("Datos incompletyos","Usuarop o contraseña vacios")

            result=Cursor.Query(f"SELECT idusuario FROM wisemendb_saller.usuario where usuario.usuario='{usuario.get()}'and password='{password.get()}'")
            if result is not None:
                MensajeBox.showinfo("Mensaje","Usuario comprobado con exito")
                Menuvie.funcion()
                root.withdraw()
            else:
                MensajeBox.showerror("Error","Usuario no registrado")
        
                

        def CrearFormulario(frame):
            def MostrarPassword():
                ver=control.get()
                if ver==0:
                    textopassword.config(show="")
                else:
                    textopassword.config(show="*")

            frame.config(background="#958235")
            frame.pack(side="left",expand=True,fill=BOTH)
            Label(frame,text="Usuario",background="#958235",fg="white",font=("ventana",24)).pack()
            textousuario=ttk.Entry(frame,textvariable=usuario,font=("ventana",20))
            textousuario.pack()
            Label(frame,text=" ",background="#958235").pack()
            Label (frame,text="Contraseña",background="#958235",fg="white",font=("ventana",24)).pack()
            textopassword=ttk.Entry(frame,textvariable=password,font=("ventana",20),show="*")
            textopassword.pack()
            Label(frame,text=" ",background="#958235").pack()
            Checkbutton(frame, text="ver", onvalue=1, offvalue=0,background="#958235",variable=control,font=("ventana",15),fg="white",command=MostrarPassword).pack(anchor="w",expand=True,side=TOP,fill=BOTH)
            Label(frame,text=" ",background="#958235").pack()
            Button(frame,text="inicio",width=10,height=10,font=("ventana",15),command=LoginCursor).pack(expand=True)
            Label(frame,text=" ",background="#958235").pack()
        
        CrearFormulario(self)
       

e = LoginView(root)
e.pack(fill=BOTH, expand=YES)
root.mainloop()
