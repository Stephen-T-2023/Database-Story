import sqlite3

try:
    table = sqlite3.connect("schoolData.db")
    db = table.cursor()

    db.execute('''CREATE TABLE STUDENTS (STUDENT_ID INTEGER PRIMARY KEY, STUDENT_FIRST_NAME TEXT, STUDENT_LAST_NAME TEXT)''')
        
    db.execute('''CREATE TABLE STUDENT_DETAILS (STUDENT_ID INTEGER PRIMARY KEY, YEAR_GROUP TEXT, DATE_OF_BIRTH DATETIME, EMERGENCY_PHONE INTEGER, EMERGENCY_EMAIL EMAIL, FOREIGN KEY(STUDENT_ID) REFERENCES STUDENTS(STUDENT_ID)) ''')

    db.execute('''CREATE TABLE COURSE_LEAD (COURSE_LEAD_ID INTEGER PRIMARY KEY, COURSE_LEAD_NAME TEXT)''')

    db.execute('''CREATE TABLE COURSES (COURSE_ID INTEGER PRIMARY KEY, COURSE_NAME TEXT, COURSE_LEAD_ID INTEGER, STUDENT_ID INTEGER, FOREIGN KEY(COURSE_LEAD_ID) REFERENCES COURSE_LEAD(COURSE_LEAD_ID), FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT_COURSE_JOIN(STUDENT_ID))''')

    db.execute('''CREATE TABLE STUDENT_COURSE_JOIN (STUDENT_ID INTEGER, COURSE_ID INTEGER, PRIMARY KEY (STUDENT_ID, COURSE_ID), FOREIGN KEY(STUDENT_ID) REFERENCES STUDENTS(STUDENT_ID), FOREIGN KEY(COURSE_ID) REFERENCES COURSES(COURSE_ID))''')

    db.execute('''CREATE TABLE GRADES (STUDENT_ID INTEGER PRIMARY KEY, COURSE_ID INTEGER, ASSIGNMENT_NAME TEXT, GRADE TEXT, DATE_GRADED DATETIME, FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT_COURSE_JOIN(STUDENT_ID), FOREIGN KEY(COURSE_ID) REFERENCES STUDENT_COURSE_JOIN(COURSE_ID))''')

    db.execute('''CREATE TABLE ATTENDANCE (STUDENT_ID INTEGER PRIMARY KEY, COURSE_ID INTEGER, DAY_ATTENDANCE INTEGER, TOTAL_ATTENDANCE INTEGER, FOREIGN KEY(STUDENT_ID) REFERENCES STUDENT_COURSE_JOIN(STUDENT_ID), FOREIGN KEY(COURSE_ID) REFERENCES STUDENT_COURSE_JOIN(COURSE_ID))''')

except:
    table = sqlite3.connect("schoolData.db")
    table = table.cursor()