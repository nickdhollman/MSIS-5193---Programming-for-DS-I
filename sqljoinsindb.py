from mysql.connector import connection
import csv

# connect to DB server
cnx = connection.MySQLConnection(user='readonlyuser', password='Fall2024Msis5193!',
                                 host='34.66.134.201',
                                 database='classicmodels')
# initialize the cursor
cursor = cnx.cursor()

# inner join
cursor.execute("SELECT customers.*, employees.* FROM customers INNER JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber;")
for x in cursor:
    print(x)

'''
# inner join - export to table
cursor.execute("SELECT customers.*, employees.* FROM customers INNER JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber;")

print(cursor.description)
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(field_names)

with open('employees_customer_inner.csv', 'w', newline='') as fp:
    writer = csv.writer(fp)
    writer.writerow(field_names)
    for x in cursor:
        print(list(x))
        writer.writerow(list(x))
'''

# left join
cursor.execute("SELECT * FROM customers LEFT JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber;")
for x in cursor:
    print(x)

# right join
cursor.execute("SELECT * FROM customers RIGHT JOIN employees ON customers.salesRepEmployeeNumber = employees.employeeNumber;")
for x in cursor:
    print(x)

# close DB connection
cnx.close()