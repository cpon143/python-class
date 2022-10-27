import sqlite3
conn=sqlite3.connect('love.db')
cursor=conn.cursor()
conn.execute("DROP TABLE IF EXISTS Employee")
table='''CREATE TABLE Employee(Name varchar(255), Income int, Age int);'''
cursor.execute(table)
# By MD......

cursor.execute('''INSERT INTO Employee VALUES('Rahul', 6000, 18)''')
cursor.execute('''INSERT INTO Employee VALUES('Vinit', 10000, 30)''')
cursor.execute('''INSERT INTO Employee VALUES('Anjali', 7000, 32)''')
cursor.execute('''INSERT INTO Employee VALUES('Anyone', 8000, 21)''')
cursor.execute('''INSERT INTO Employee VALUES('Someone', 12000, 23)''')

print("Employee Table: ")
data= cursor.execute('''SELECT * FROM Employee''')
for row in data:
    print(row)
    
# updating
# cursor.execute('''UPDATE Employee SET Income=5000  WHERE Age<25;''')
# print("\n After updating....\n")
# diaplay data

# delete data
print("\n After Deleting....\n")
cursor.execute("DELETE FROM Employee WHERE Age=21")
data= cursor.execute('''SELECT * FROM Employee''')
for row in data:
    print(row)
    
conn.commit()