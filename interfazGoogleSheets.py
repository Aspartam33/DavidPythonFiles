import gspread
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from oauth2client.service_account import ServiceAccountCredentials
import os
ventana = tk.Tk()

#abre un archivo
def abrir_archivo():
     archivo_abierto = filedialog.askopenfilename(initialdir = "/",title="Seleccione archivo",filetypes = (("csv files","*.csv"),("all files","*.*")))
     to_google_sheets(archivo_abierto)
     print (archivo_abierto)
#formulario para crear una nueva hoja en un libro de google sheets
def form_nueva_hoja():
    ventana2 = tk.Tk()
    Label1 = tk.Label(ventana2,text="Ingrese el nombre de la hoja")
    Label1.grid(column=0,row=0)
    dato=tk.StringVar()
    entrada1 = tk.Entry(ventana2,width=10,textvariable=dato)
    entrada1.grid(column=0,row=2)
    boton_crear=Button(ventana2, text="Crear")
    boton_crear.grid(column=0,row=3)
    ventana2.mainloop()
#carga en un fichero csv en google sheets 
def to_google_sheets(my_file):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    creds = ServiceAccountCredentials.from_json_keyfile_name('AutomarizacionTiendas-fca572e81aca.json',scope)

    client = gspread.authorize(creds)

    sheet = client.open('data-prueba')

    with open(my_file,'r') as file_obj:
        content = file_obj.read()
        res = client.import_csv(sheet.id, data=content)
        return res
        from tkinter import messagebox
Button(text="Seleccionar archivo csv",bg="Pale green",command=abrir_archivo).place(x=10,y=10)
Button(text="Crear hoja",bg="light blue",command=form_nueva_hoja).place(x=10,y=40)

ventana.mainloop()