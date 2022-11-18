import tkinter.messagebox
import tkinter
from tkinter import *
import cv2
import sqlite3
from subprocess import call

connection = sqlite3.connect('librarymangsys.db')
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS addBook(bookid INTEGER PRIMARY KEY NOT NULL,"
          "bookname Text NOT NULL,"
          "author Text NOT NULL,"
          "status INTEGER NOT NULL)")
connection.commit()

def gotomain():
    call(["python", "main.py"])

def addbook():
    global bookid, bookname
    global authorname, status
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
    btnback = Button(window,width= 10,height=2,bg = 'red', fg = 'white',text='Back',
                     command= lambda :[window.destroy(),gotomain()])
    btnback.place(x = 20, y =20)


    lblframe = Frame(window)
    lblframe.place(x=125,y=50)
    lbl = Label(lblframe,bg='black',fg='#fff',width= 40,height=4,text="Add book here",font=('Arial',15))
    lbl.pack()

    lblframe = Frame(window,bg = 'black',)
    lblframe.place(x=120,y=200)
    enyframe = Frame(window,bg = 'black',)
    enyframe.place(x=190,y=200)

    lbl1 = Label(lblframe,width= 10,height=4, bg = 'black',fg = 'white',text='Book ID')
    lbl1.pack()
    lbl2 = Label(lblframe,width= 10,height=4,bg = 'black', fg = 'white',text='Book Name')
    lbl2.pack()
    lbl3 = Label(lblframe,width= 10,height=4,bg = 'black', fg = 'white',text='Author')
    lbl3.pack()
    lbl4 = Label(lblframe,width= 10,height=4,bg = 'black', fg = 'white',text='Status')
    lbl4.pack()

    bookid = Entry(enyframe,width= 50, bg = 'white',font=("Arial",10),fg= "#000")
    bookid.pack(ipady=5,padx = 20,pady=18)

    bookname = Entry(enyframe,width= 50,bg = 'white',font=("Arial",10),fg= "#000")
    bookname.pack(ipady=5,padx = 20,pady=18)

    authorname = Entry(enyframe,width= 50,bg = 'white',font=("Arial",10),fg= "#000")
    authorname.pack(ipady=5,padx = 20,pady=18)

    status = Entry(enyframe,width= 50,bg = 'white',font=("Arial",10),fg= "#000")
    status.pack(ipady=5,padx = 20,pady=18)


    btnadd = Button(window,width= 10,height=2,bg = 'orange', fg = '#000',text='Add Book',
                    font=("Arial",10),command=RegBook)
    btnadd.place(x = 300,y = 500)
    window.mainloop()



def RegBook():
    id = bookid.get()
    name = bookname.get()
    author = authorname.get()
    stat = status.get()
    if id == '' or name == '' or author == '' or stat == '':
        tkinter.messagebox.showinfo("Failed","Enter All Fields")
    else:
        c.execute("Select bookid from addBook where bookid = ?",(id,))
        istaken = c.fetchone()
        if istaken:
            tkinter.messagebox.showinfo("Failed", "ID must be unique")
        else:
                c.execute("INSERT INTO addBook(bookid,bookname,author,status) VALUES (?,?,?,?)",(id,name,author,stat,))
                connection.commit()
                tkinter.messagebox.showinfo("succes","Book Added Successfuly")







