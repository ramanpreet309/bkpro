import mysql.connector,time, os


def connect():
    conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="bookings")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT,author TEXT,year INTEGER, price INTEGER)")
    conn.commit()
    conn.close()


def view_command():
    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="bookings")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows


def insert_command(title, author, year, price):
    conn = mysql.connector.connect("bookings.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book(title,author,year,price) VALUES('"+title+"','"+author+"','"+year+"','"+price+"') ")
    conn.commit()
    conn.close()


def delete_command(id):
    conn = mysql.connector.connect("bookings.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = ?",(id,))
    conn.commit()
    conn.close()



def search_command(title="", author="", year="", price=""):
    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="bookings")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title = '"+title+"'  or author = '"+author+"' or year = '"+year+"' or price ='"+price+"'")
    rows = cur.fetchall()
    conn.close()
    return rows


def update_command(id, title, author, year, price):
    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="bookings")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title='"+title+"',author='"+author+"',year='"+year+"',price='"+price+"' WHERE id ='"+id+"'")
    conn.commit()
    conn.close()


connect()
os.system("cls")


connect()






















