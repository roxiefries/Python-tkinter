import sqlite3


def connect():
    conn=sqlite3.connect("student.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY"
                ", name TEXT, section TEXT, student_number INTEGER, midExam INTEGER,"
                " midCls INTEGER, finExam INTEGER, finCls INTEGER, finalGrade INTEGER)")
    conn.commit()
    conn.close()


def insert(name, section, student_number, midExam, midCls, finExam, finCls, finalGrade):
    from backEnd import calculation
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?,?,?,?,?,?,?,"
                "?)",(name, section, student_number, midExam, midCls, finExam, finCls ,calculation(midExam, midCls, finExam, finCls)))
    conn.commit()
    conn.close()
    view()


def view():
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    conn.close()
    return row


def search(name="", section="", student_number="", midExam="", midCls="", finExam="", finCls="", finalGrade=""):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM student WHERE name=? OR section=? "
                "OR student_number=? OR midExam=? OR midCls=? OR finExam=? OR finCls=? OR finalGrade=?"
                ,(name, section, student_number, midExam, midCls, finExam, finCls, finalGrade))
    row=cur.fetchall()
    conn.close()
    return row


def delete(id):
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM student where id=?", (id,))
    conn.commit()
    conn.close()


def update(id,name,section, student_number,midExam,midCls,finExam,finCls,finalGrade):
    from backEnd import calculation
    conn = sqlite3.connect("student.db")
    cur = conn.cursor()
    cur.execute("UPDATE student SET name=?,section=?,student_number=?,midExam=?,midCls=?,finExam=?,finCls=?, "
                "finalGrade=?", (name, section, student_number,midExam,midCls,finExam,finCls, calculation(midExam,midCls,finExam,finCls)))
    conn.commit()
    conn.close()

def calculation(midExam, midCls, finExam, finCls):
    fltmidExam = float(midExam)
    fltmidCls = float(midCls)
    fltfinExam = float(finExam)
    fltfinCls = float(finCls)
    midGrade = (fltmidExam * .40) + (fltmidCls * .60)
    finGrade = (fltfinExam * .50) + (fltfinCls * .50)
    finalGrade = ((midGrade + finGrade) / 2)
    return finalGrade


connect()
