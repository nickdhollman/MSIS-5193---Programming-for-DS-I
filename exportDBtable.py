from mysql.connector import connection
import csv

# connect to DB server
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='classicmodels')

# initialize the cursor
cursor = cnx.cursor()

# Show tables
cursor.execute("show tables")
for x in cursor:
    print(x)

# select the data from a table to be exported
cursor.execute("select * from employees") ### this line of code selects the data you want to be exported - this would be switched out for a join statement, etc. but you are using the
                                            #### cursor.execute to select the data and within quotes is SQL syntax on what you want to select from the database

# initialize a cursor to execute SQL statement
print(cursor.description) ############ this line of code prints column attributes in the mySQL database
num_fields = len(cursor.description)
print(num_fields) ############ this line of code prints the number of columns in the mySQL database
field_names = [i[0] for i in cursor.description] ########## this line of code selects the first description/attribute from the cursor.description syntax which the first attribute is the column name
print(field_names) ########### this line of code prints the column names

# save the table to a file customers.csv
'''
with open('employees.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
'''
### in class exercise - repeat for customers and offices
# select the data from a table to be exported
### you have to do the cnx = step below and the cursor = step below for both csv creations
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='classicmodels')
cursor = cnx.cursor()
cursor.execute("select * from customers")

# initialize a cursor to execute SQL statement
print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

# save the table to a file customers.csv
'''
with open('customers.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
'''
# select the data from a table to be exported
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='classicmodels')
cursor = cnx.cursor()
cursor.execute("select * from offices")

# initialize a cursor to execute SQL statement
print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

# save the table to a file customers.csv
'''
with open('offices.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
'''
#repeat for orders
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='classicmodels')
cursor = cnx.cursor()
cursor.execute("select * from orders")

# initialize a cursor to execute SQL statement
print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

# save the table to a file customers.csv
'''
with open('orders.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
'''
#repeat with payments
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='classicmodels')
cursor = cnx.cursor()
cursor.execute("select * from payments")

# initialize a cursor to execute SQL statement
print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

# save the table to a file customers.csv
'''
with open('payments.csv', 'w', newline='')  as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
'''
# close DB connection
cnx.close()