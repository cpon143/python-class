# # inbuild library in python . it is server less cann't work upon internet
# # 1. Import sqlite3
# # 2. Bulid up connection with the data base
# # 3. Generate curser(function) to fetch the data
# import sqlite3
# # connect to DB and create a curser
# sqliteConnection= sqlite3.connect('sql.db')
# cursor = sqliteConnection.cursor()
# print('BD Init')

# # write a query and excute it with curser
# query='select sqlite_version();'
# cursor.execute(query)

# # Fetch and output result
# result= cursor.fetchall()
# print('sqlite vesion is()'.format(result))
# # close the curser
# cursor.close()
# # close DB connection
# sqliteConnection.close()
# print('sqlite connection closed')


# # ------------------------------------------------------------------

# cnt=sqlite3.connect('gfg.db')
# cnt.execute('''drop table if exists exam_hall''')
# # create exam_hall relation
# cnt.execute('''CREATE TABLE exam_hall(
#     NAME TEXT,
#     PIN INTEGER,
#     OCCUPANCY REAL);''')
# # Insert tples for the relation
# cnt.execute('''INSERT INTO exam_hall VALUES(
#     'center-a',1125,98.6
# )''')
# cnt.execute('''INSERT IN TO exam_hall VALUES(
#     NULL,1158,80.5
# )''')
# # Query the data , print the data and its type
# cursor = cnt.execute('''SELECT * FROM exam_hall;''')
# # for i in cursor:
# #     # print(str(i[0])+" "+str(i[1])+" "+)

# --------------------------------------------
# import sqlite3
# connecton_obj = sqlite3.connect('are.db')
# cursor_obj = connecton_obj.cursor()
# cursor_obj.execute("DROP TABLE IF EXISTS T1")
# table="""CREATE TABLE t1(Email varchar(255) NOT NULL,Name varchar(25) NOT NULL,Score int);"""
# cursor_obj.execute(table)
# # print("Table is ready")
# connecton_obj.execute(
#     """INSERT INTO t1 (Email,Name,Score) VALUES ("k1@gmail.com","k1",25)""")
# connecton_obj.execute(
#     """INSERT INTO t1 (Email,Name,Score) VALUES ("k2@gmail.com","k2",26)""")
# connecton_obj.execute(
#     """INSERT INTO t1 (Email,Name,Score) VALUES ("k3@gmail.com","k3",27)""")
# connecton_obj.execute(
#     """INSERT INTO t1 (Email,Name,Score) VALUES ("k4@gmail.com","k4",28)""")
# connecton_obj.execute(
#     """INSERT INTO t1 (Email,Name,Score) VALUES ("k5@gmail.com","k5",29)""")
# connecton_obj.execute(
#     """INSERT INTO t1 (Email,Name,Score) VALUES ("k6@gmail.com","k6",30)""")
# connecton_obj.execute(
#     """INSERT INTO t1 (Email,Name,Score) VALUES ("k7@gmail.com","k7",31)""")
# statement='''SELECT * FROM t1'''
# cursor_obj.execute(statement)
# print("All the data")
# output = cursor_obj.fetchall()
# for row in output:
#     print(row)

# -----------------------------------------------------------------------------

import sqlite3
conn=sqlite3.connect('lovely.db')
cursor=conn.cursor()
conn.execute("DROP TABLE IF EXISTS Student")
table='''CREATE TABLE Student(Name varchar(255), Class varchar(25), Section text);'''
cursor.execute(table)

cursor.execute('''INSERT INTO Student VALUES('Rahul', 'K', 'B')''')
cursor.execute('''INSERT INTO Student VALUES('Vinit', 'Kl', 'O')''')
cursor.execute('''INSERT INTO Student VALUES('Anjali', 'EK', 'B')''')
cursor.execute('''INSERT INTO Student VALUES('Anyone', 'Ko', 'B')''')
cursor.execute('''INSERT INTO Student VALUES('Someone', 'K', 'B')''')

# print("Data inserted in to table: ")
# data=cursor.execute('''SELECT * FROM Student''')
# for row in data:
#     print(row)

# WHERE CLAUSE TO RETRIVE DATA
#  R% (name starting with R)
# cursor.execute("SELECT * FROM Student WHERE Name Like 'R%'")

# table in assending order based on address
cursor.execute("SELECT * FROM Student ORDER BY Class DESC")

# printing the cursor data
# print(cursor.fetchall())
# conn.commit()

# DISPLAY DATA ROW BY ROW 
for i in cursor:
    print(i)
conn.close()
