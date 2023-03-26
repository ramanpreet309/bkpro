from tkinter import *
import mysql.connector
import backend

main_win = Tk()
main_win.title("Books ’round the clock")


def get_selected_row(event):
    global selected_tuple
    index = list_box.curselection()[0]
    selected_tuple = list_box.get(index)

    e_title.delete(0,END)
    e_title.insert(END, selected_tuple[1])

    e_author.delete(0,END)
    e_author.insert(END, selected_tuple[2])

    e_year.delete(0,END)
    e_year.insert(END, selected_tuple[3])

    e_price.delete(0,END)
    e_price.insert(END, selected_tuple[4])


def view_command():
    list_box.delete(0, END)
    for row in backend.view_command():
        list_box.insert(END, row)


def search_command():
    list_box.delete(0,END)
    for row in backend.search_command(e_title.get(), e_author.get(), e_year.get(), e_price.get()):
        list_box.insert(END, row)
    e_title.delete(0,END)
    e_author.delete(0,END)
    e_year.delete(0,END)
    e_price.delete(0,END)


def add_command():
    conn = mysql.connector.connect(host="localhost",username="root",password="1234",database="bookings")
    cur = conn.cursor()
    cur.execute("INSERT INTO book(title,author,year,price) VALUES('" + e_title.get() + "','" + e_author.get() + "','" + e_year.get() + "','" + e_price.get() + "') ")
    conn.commit()
    conn.close()
    list_box.delete(0,END)
    list_box.insert(END,(e_title.get(),e_author.get(),e_year.get(),e_price.get()))
    e_title.delete(0,END)
    e_author.delete(0,END)
    e_year.delete(0,END)
    e_price.delete(0,END)


def update_command():
    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="bookings")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title='"+e_title.get()+"',author='"+e_author.get()+"',year='"+e_year.get()+"',price='"+e_price.get()+"' WHERE id ='"+e_id.get()+"'")
    conn.commit()
    conn.close()
    list_box.delete(0, END)
    list_box.insert(END, (e_title.get(), e_author.get(), e_year.get(), e_price.get()))
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_year.delete(0, END)
    e_price.delete(0, END)
    e_id.delete(0,END)


def delete_command():
    conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="bookings")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id = '"+e_id.get()+"'")
    conn.commit()
    conn.close()
    list_box.delete(0, END)
    list_box.insert(END, (e_title.get(), e_author.get(), e_year.get(), e_price.get()))
    e_title.delete(0, END)
    e_author.delete(0, END)
    e_year.delete(0, END)
    e_price.delete(0, END)
    e_id.delete(0, END)
    view_command()


def exit_command():
    exit()


# Labels and entries
l_title = Label(main_win, text="Title")
l_title.grid(row=0, column=0)
title_text = StringVar()
e_title = Entry(main_win)
e_title.grid(row=0, column=1)

l_author = Label(main_win, text="Author")
l_author.grid(row=0, column=2)
author_text = StringVar()
e_author = Entry(main_win)
e_author.grid(row=0, column=3)


l_year = Label(main_win, text="year")
l_year.grid(row=1, column=0)
e_year = Entry(main_win)
e_year.grid(row=1, column=1)


l_price = Label(main_win, text="Price")
l_price.grid(row=1, column=2)
e_price = Entry(main_win)
e_price.grid(row=1, column=3)

l_id = Label(main_win, text="id")
l_id.grid(row=2, column=0)
id_text = StringVar()
e_id = Entry(main_win, textvariable=id_text)
e_id.grid(row=2, column=1)

# list box

list_box = Listbox(main_win,height=7,width=55)
list_box.grid(row=3, column=0,rowspan=5,columnspan=2)
list_box.bind("<<listboxSelect>>", get_selected_row)

# buttons

b_view = Button(main_win,text="view all",width=10,command=view_command)
b_view.grid(row=2,column=3)

b_search = Button(main_win,text="search",width=10,command=search_command)
b_search.grid(row=3,column=3)

b_add = Button(main_win,text="add",width=10,command=add_command)
b_add.grid(row=4,column=3)

b_update = Button(main_win, text="update",width=10,command=update_command)
b_update.grid(row=5,column=3)

b_delete = Button(main_win, text="delete",width=10,command=delete_command)
b_delete.grid(row=6,column=3)

b_exit = Button(main_win, text="exit",width=10,command=exit_command)
b_exit.grid(row=7,column=3)

main_win.mainloop()

