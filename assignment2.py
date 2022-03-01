import sqlite3

# Connection to the database
conn = sqlite3.connect('Stu_data.db')

# Create a cursor
c = conn.cursor()

# Creating the tables
c.execute(""" CREATE TABLE Student(
        Student_ID INT,
        Student_firstname VARCHAR(30),
        Student_lastname VARCHAR(30),
        Major VARCHAR(30),
        GPA REAL,
        Email VARCHAR(50)
    )""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


c.execute(""" CREATE TABLE Course(
        Course_ID VARCHAR(30),
        Course_name VARCHAR(30),
        Total_credit INT,
        Term VARCHAR(30),
        Student_id INT
    )""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Inserting the data into the Student Table
c.execute(""" INSERT INTO Student VALUES(0887, 'John', 'Steve', 'IT', 3.46, 'jsteve@auaf.edu.af');""")
c.execute(""" INSERT INTO Student VALUES(0888, 'Sarah', 'Paul', 'Business', 3.95, 'spaul@auaf.edu.af');""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Inserting the data into the Course Table
c.execute("""INSERT INTO Course VALUES('ITC215', 'Programming 1', 3, 'Spring 2021', 0887);""")
c.execute("""INSERT INTO Course VALUES('ITC345', 'Python', 4, 'Fall 2021', 0888);""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Allow user to search for a specific course/student using the ID. 
c.execute("SELECT Student_firstname FROM Student WHERE Student_ID = 0888")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Show a list of students or a list of available courses.
c.execute("SELECT Course_Name FROM Course")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Allow the user to update specific content within a table.
c.execute(""" UPDATE Student SET GPA = 3.8 WHERE Student_ID = 0887""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Delete a record from a database
c.execute(""" DELETE FROM Course WHERE Student_ID = 0888""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Show a list of students who are enrolled in a particular course.
c.execute(""" SELECT DISTINCT A.Student_firstname FROM STUDENT A INNER JOIN COURSE B ON A.Student.ID = B.Student_ID
            WHERE B.Course_name = 'Programming 1';""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()


# Show a list of courses that are offered in a specific term
c.execute(""" SELECT Course_name FROM Course WHERE Term = 'Spring 2021';""")
# Comming the command
conn.commit()
# Closing the connection
conn.close()