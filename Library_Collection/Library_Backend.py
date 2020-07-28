import sqlite3


def connectToDB():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS library "
                "(id INTEGER PRIMARY KEY,"
                "title text,"
                "author text,"
                "year integer,"
                "isbn integer)")
    conn.commit()
    conn.close()


def insertToDB(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO library VALUES (NULL, ?, ?, ?, ?)", (title, author, year, isbn))
    conn.commit()
    conn.close()


def updateToDB(id, title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE library SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
    conn.commit()
    conn.close()


def viewFromDB():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM library")
    rows = cur.fetchall()
    conn.close()
    return rows


def searchFromDB(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM library WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows


def deleteFromDB(id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM library WHERE id=?", (id, ))
    conn.commit()
    conn.close()


connectToDB()