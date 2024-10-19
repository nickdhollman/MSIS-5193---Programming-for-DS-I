from mysql.connector import connection
import csv

# create a mySQL connection msis5193-ssb
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='classicmodels')
#in class announcement professor stated database is 'Northwind'

# initialize a cursor to execute SQL statement
cursor = cnx.cursor()

# Show tables
cursor.execute("show tables")
for x in cursor:
   print(x)


# show records in table employees
cursor.execute("select * from employees")
for x in cursor:
    print(x)

# close the mySQL connection
cnx.close()