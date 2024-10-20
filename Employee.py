import mysql.connector
con = mysql.connector.connect(
    host ='localhost',
    user ='root',
    password =''
    
)
mycursor = con.cursor()
mycursor.execute('Drop DATABASE Employee')

