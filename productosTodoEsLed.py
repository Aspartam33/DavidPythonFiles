import pymysql as mysql
import pandas as pd 
def convierte_a_csv(sql,mydb):
    myresult = pd.read_sql_query(sql,mydb)

    df = pd.DataFrame(myresult)
    res = df.to_csv(r'data1.csv',index=False)
    return res
def consulta_sql():
    mydb = mysql.connect(
        host="ec2-15-237-132-44.eu-west-3.compute.amazonaws.com",
        user="infra",
        password="infra_pass",
        database="db771268751"
     )
    mycursor = mydb.cursor()

    sql = ("SELECT  pstl_product.state as state,  pstl_product.id_product as idProduct,  pstl_product_attribute.id_product_attribute  as combinacion_id,pstl_product.reference as referencia, pstl_product_attribute.reference as referencia_combinacion,pstl_product.quantity as cantidad,pstl_product_attribute.quantity as cantidad_referencia,pstl_product.ean13 as ean13_producto,pstl_product_attribute.ean13 as ean13_combinacion,pstl_product.price as precio_producto,pstl_product_attribute.price as precio_combinacion,pstl_product.wholesale_price as precio_mayor, pstl_product_attribute.wholesale_price as precio_m_combinacion FROM pstl_product  LEFT JOIN pstl_product_attribute on pstl_product.id_product  = pstl_product_attribute.id_product_attribute UNION ALL SELECT  pstl_product.state as state,  pstl_product.id_product as idProduct,  pstl_product_attribute.id_product_attribute  as combinacion_id,pstl_product.reference as referencia, pstl_product_attribute.reference as referencia_combinacion,pstl_product.quantity as cantidad,pstl_product_attribute.quantity as cantidad_referencia,pstl_product.ean13 as ean13_producto,pstl_product_attribute.ean13 as ean13_combinacion,pstl_product.price as precio_producto,pstl_product_attribute.price as precio_combinacion,pstl_product.wholesale_price as precio_mayor, pstl_product_attribute.wholesale_price as precio_m_combinacion FROM pstl_product  RIGHT JOIN pstl_product_attribute on pstl_product.id_product  = pstl_product_attribute.id_product_attribute")
#mycursor.execute(sql)
    myresult = pd.read_sql_query(sql,mydb)

    df = pd.DataFrame(myresult)
    df.to_csv(r'data.csv',index=False)
consulta_sql()