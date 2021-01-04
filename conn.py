import mysql.connector

mydb = mysql.connector.connect(
    host="ec2-15-237-106-110.eu-west-3.compute.amazonaws.com",
    user="root",
    password="$l1n4xl1n4x$",
   
)

print(mydb)