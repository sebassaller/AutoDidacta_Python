from tkinter import *
from PIL import Image, ImageTk

class VentanaRedimencionar(Frame):
    def __init__(self, master, *pargs):
        
        Frame.__init__(self, master, *pargs)
       
        self.config(bd=30)
        self.config(relief="sunken")
        self.config(background="#518CAD")
        texto=StringVar()
        texto.set("Bienvenidos a mi Primer Frame Python")
        #imagen = PhotoImage(file="./img/png/tres.jpg",height=100,width=100)
        label=Label(self)#image=imagen#)
        label.pack(anchor="center")
        label.config(fg="#217434", bg="#518CAD",font=("Comic Sans MS",24,"bold"),textvariable=texto)


        #Label.config(fg="blue",bg="green",font=("Verdana",24))
        self.image = Image.open("./IMG/fondo_python.jpg")
        self.img_copy= self.image.copy()
    
        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)



    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)
    
    def _Relieve(self,color):
        self.config(background=str(color))
        self.config(relief=str(color))