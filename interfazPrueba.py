import pymysql as mysql
import pandas as pd 
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
import os
ventana = Tk()
def crear_archivo():
    archivo_guardado = filedialog.asksaveasfile(initialdir = "/",title="Select file",defaultextension=".csv",filetypes = (("csv files","*.csv"),("all files","*.*")))
    archivo = open(archivo_guardado,"w")
    messagebox.showinfo("Crear archivo", "Archivo creado")
    print(archivo_guardado)
def abrir_archivo():
    archivo_abierto = filedialog.askopenfilename(initialdir = "/",title="Seleccione archivo",filetypes = (("csv files","*.csv"),("all files","*.*")))
    consulta_sql(archivo_abierto)
    print (archivo_abierto)

def convierte_a_csv(sql,mydb,path):
    myresult = pd.read_sql_query(sql,mydb)
    files = path
    df = pd.DataFrame(myresult)
    res = df.to_csv(df.files,index=False)
    return res
def consulta_sql(path):
    try:
          mydb = mysql.connect(
            host="ec2-15-237-132-44.eu-west-3.compute.amazonaws.com",
             user="infra",
             password="infra_pass",
             database="db771268751"
           )
          print (path)
    
          sql = ("SELECT pstl_order_invoice.id_order_invoice  as id_pedido, pstl_order_detail.product_id as id_producto,pstl_order_invoice.date_add as fecha_de_alta,pstl_order_payment.payment_method as forma_de_pago,pstl_order_detail.product_quantity as cantidad_producto,pstl_order_invoice.total_paid_tax_incl as total_pag_inclu, pstl_order_invoice.total_paid_tax_excl as total_pag_excl,pstl_order_invoice.total_discount_tax_incl as desc_total_incl,pstl_order_invoice.total_discount_tax_excl as desc_total_excl, pstl_order_detail.total_price_tax_excl as total_price_tax_excl, pstl_order_detail.total_price_tax_incl as total_price_tax_incl,pstl_order_invoice.total_shipping_tax_incl as total_envio_incl,pstl_order_invoice.total_shipping_tax_excl as total_envio_excl FROM pstl_order_invoice  LEFT JOIN pstl_order_detail on pstl_order_invoice.id_order_invoice = pstl_order_detail.id_order_detail LEFT JOIN pstl_order_payment on pstl_order_invoice.id_order_invoice = pstl_order_payment.id_order_payment  WHERE pstl_order_invoice.date_add <='2020-01-09 00:00:00' AND pstl_order_invoice.date_add >='2020-31-12 00:00:00' UNION ALL SELECT pstl_order_invoice.id_order_invoice  as id_pedido, pstl_order_detail.product_id as id_producto,pstl_order_invoice.date_add as fecha_de_alta,pstl_order_payment.payment_method as forma_de_pago,pstl_order_detail.product_quantity as cantidad_producto,pstl_order_invoice.total_paid_tax_incl as total_pag_inclu, pstl_order_invoice.total_paid_tax_excl as total_pag_excl,pstl_order_invoice.total_discount_tax_incl as desc_total_incl,pstl_order_invoice.total_discount_tax_excl as desc_total_excl, pstl_order_detail.total_price_tax_excl as total_price_tax_excl, pstl_order_detail.total_price_tax_incl as total_price_tax_incl,pstl_order_invoice.total_shipping_tax_incl as total_envio_incl,pstl_order_invoice.total_shipping_tax_excl as total_envio_excl from pstl_order_invoice   RIGHT JOIN pstl_order_detail on pstl_order_invoice.id_order_invoice = pstl_order_detail.product_id RIGHT JOIN pstl_order_payment on pstl_order_invoice.id_order_invoice = pstl_order_payment.id_order_payment  WHERE pstl_order_invoice.date_add <='2020-01-09 00:00:00' AND pstl_order_invoice.date_add >='2020-31-12 00:00:00'")
          convierte_a_csv(sql,mydb,path)
    except mysql.InternalError as err:
        code, message=err.args
        print ("Error",code,message)
    
Button(text="Seleccionar archivo csv",bg="Pale green",command=abrir_archivo).place(x=10,y=10)
Button(text="Crear archivo csv",bg="Pale green",command=crear_archivo).place(x=10,y=40)
ventana.mainloop()