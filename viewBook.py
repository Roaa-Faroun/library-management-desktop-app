from subprocess import call
import tkinter
from tkinter import *
import cv2
import sqlite3


connection = sqlite3.connect('librarymangsys.db')
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS addBook(bookid INTEGER PRIMARY KEY NOT NULL,"
          "bookname Text NOT NULL,"
          "author Text NOT NULL,"
          "status INTEGER NOT NULL)")
connection.commit()

def gotomain():
    call(["python", "main.py"])

def viewbook():
    img = 'img/lib.png'
    img = cv2.imread(img)
    img = cv2.resize(img,(700,600))
    cv2.imwrite('img/lib.png',img)

    window = Tk()
    img = PhotoImage(file = 'img/lib.png')
    window.title("main page")
    window.geometry("700x600")
    window.resizable(False,False)
    window.config(bg = 'black')
    lbl = Label(window)
    lbl.config(image = img)
    lbl.image = img
    lbl.place(x = 0,y = 0)
    btnback = Button(window,width= 10,height=2,bg = 'red',
                     fg = 'white',text='Back',command=lambda :[window.destroy(),gotomain()])
    btnback.place(x = 20, y =20)

    c.execute("Select * from addBook")
    data = c.fetchall()
    lblframe = Frame(window)
    lblframe.place(x=50, y=70)
    lbl = Label(lblframe, bg='black', fg='#fff', width=55, height=20, text="",
                font=('Arial', 15))
    lbl.pack()

    lbl = Label(window, width=5, font=('Arial', 15),
                bg='#000', fg='orange', text="id")
    lbl.place(x=55, y=75)
    lbl = Label(window, width=15, font=('Arial', 15),
                bg='#000', fg='orange', text="Book name")
    lbl.place(x=130, y=75)
    lbl = Label(window, width=15, font=('Arial', 15),
                bg='#000', fg='orange', text="author")
    lbl.place(x=360, y=75)
    lbl = Label(window, width=5, font=('Arial', 15),
                bg='#000', fg='orange', text="status")
    lbl.place(x=600, y=75)
    col = 135
    if data:
        for i in range(len(data)):
            row = 55
            for j in range(len(data[0])):
                if type(data[i][j]) == str:
                    lbl = Label(window,  width=20,font=('Arial', 12,'bold'),
                            bg='#000', fg='#e5e5e5', text=data[i][j])
                    lbl.place(x=row,y=col)
                    row = row + 250
                else:
                    lbl = Label(window,  width=5,font=('Arial', 12,'bold'),
                            bg='#000', fg='#e5e5e5', text=data[i][j])
                    lbl.place(x=row,y=col)
                    row = row + 50
            col = col + 50



    window.mainloop()
