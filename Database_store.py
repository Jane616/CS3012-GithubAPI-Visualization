import mysql.connector

def database_test():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd=""
    )

    mycursor = mydb.cursor()

    mycursor.execute("SHOW DATABASES")

    for x in mycursor:
        print(x)
    return
