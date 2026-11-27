import sqlite3

conn = sqlite3.connect("task.db")

cursor = conn.cursor()


# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS Tasks(
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name VARCHAR(20),
#     des  TEXT
#     )
# ''')

conn.close()

def tasks():
    conn = sqlite3.connect("task.db")

    cursor = conn.cursor()
    tname = input("Enter taskname: ")
    tdas = input("Enter des: ")
    cursor.execute('''
    INSERT INTO Tasks(name,des)
    VALUES(?,?)
    ''',(tname,tdas))




    conn.commit()

    print("Task added")
    
    conn.close()



def views():
    conn = sqlite3.connect("task.db")

    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM Tasks
    ''')


    data = cursor.fetchall()
    if data:
        print("Tasks Found")

        for i in data:
            print(f"{i[0]}     Name: {i[1]}    Des: {i[2]}")
    else:
        print("No tasks")
    conn.commit()

    print("Task Printed")
    
    conn.close()




def searchtask():
    conn = sqlite3.connect("task.db")

    cursor = conn.cursor()
    t_id = int(input("Enter task id: "))
    cursor.execute('''
    SELECT * FROM Tasks WHERE id = ?
    ''',(t_id,))


    task = cursor.fetchone()
    if task:
        print("Tasks Found")

        print(f"{task[0]}     Name: {task[1]}    Des: {task[2]}")
    else:
        print("No such tasks")
    conn.commit()

    print("Task Search Finished")
    
    conn.close()

def main():
    print("Welcome to task management")
    while True:
        ch = input("Enter your choice\n1.Task\n2.Views\n3.Search Task\n")
        if ch == "1":
            tasks()
        elif ch == "2":
            views()
        elif ch == "3":
            searchtask()
        else:
            break

main()