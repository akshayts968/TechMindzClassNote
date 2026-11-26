import sqlite3

conn = sqlite3.connect("firrst.db") # to connect to the db
cursor = conn.cursor() # to interact with db

# cursor.execute(
#     ''' CREATE TABLE IF NOT EXISTS student (
#     name VARCHAR(20),
#     roll INTEGER,
#     address TEXT
#     )
# '''
# )


# cursor.execute(''' 
#     CREATE TABLE IF NOT EXISTS employee (
#     name VARCHAR(20),
#     roll INTEGER,
#     address TEXT
#     )
# '''
# )

# cursor.execute(
#     '''
#     INSERT INTO student(name,roll,address)
#     VALUES ("Mohan",25,"Kochi"),
#     ("Das",22,"Kakkanad")
# '''
# )

# cursor.execute(
#     '''
#     INSERT INTO employee(name,roll,address)
#     VALUES ("Das",22,"Kakkanad"),
#     ("Mohan",25,"Kochi")
# '''
# )

cursor.execute(
    '''
    SELECT * FROM student
'''
)
data = cursor.fetchall()

print(data)
for i in data:
    print(i[0])
conn.commit()

conn.close()

