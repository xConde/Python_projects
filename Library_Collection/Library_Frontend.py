from tkinter import *
from Library_Collection import Library_Backend
import time

"""
Library_Collection: Library_Frontend.py : library.db
Shows an interactive library interface in which the user can modify the library
database and maintain records in library.db. Library_Frontend.py creates the GUI in
tkinter and creates functionality for buttons. 

"""


def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END, selected_tuple[4])


def view_command():
    list1.delete(0, END)
    for row in Library_Backend.viewFromDB():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in Library_Backend.searchFromDB(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)


def add_command():
    list1.delete(0, END)
    if title_text.get() and author_text.get() and year_text.get() and isbn_text.get():
        Library_Backend.insertToDB(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        time.sleep(.2)
        view_command()
    else:
        list1.insert(END, "Please enter all fields")


def update_command():
    if title_text.get() and author_text.get() and year_text.get() and isbn_text.get():
        Library_Backend.updateToDB(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(),
                                   isbn_text.get())
        time.sleep(.2)
        view_command()


def delete_command():
    Library_Backend.deleteFromDB(selected_tuple[0])
    time.sleep(1.5)
    view_command()


window = Tk()


window.wm_title("Library Database")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=7, width=70)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update selected", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete selected", width=12, command=delete_command)
b5.grid(row=6, column=3)


view_command()
window.mainloop()