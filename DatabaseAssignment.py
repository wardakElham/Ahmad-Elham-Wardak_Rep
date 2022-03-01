
import sqlite3

def database():

    data = sqlite3.connect("StudentsData.db")
    data.execute('''CREATE TABLE Student_table(Student_ID INTEGER PRIMARY KEY, Student_firstname TEXT NOT NULL,
                    Student_lastname TEXT NOT NULL, Major TEXT NOT NULL , GPA TEXT, Email TEXT);''')

    data.commit()
    print('success')
    data.close()

database()
exit()
def dataInsert():

    data = sqlite3.connect("StudentsData.db")

    data.execute("INSERT INTO Student_table VALUES(0887, 'John', 'Steve', 'IT', '3.46', 'jsteve@auaf.edu.af');")

    data.commit()
    data.close()

def readData():
    
    data = sqlite3.connect("StudentsData.db")

    cur = data.execute('SELECT * FROM Student_table')
