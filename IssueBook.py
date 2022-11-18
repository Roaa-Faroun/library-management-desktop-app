import sqlite3
import tkinter
from tkinter import *
import cv2
from subprocess import call


connection = sqlite3.connect('librarymangsys.db')
c = connection.cursor()
c.execute("CREATE TABLE IF NOT EXISTS"
          " issueBook(bookid INTEGER NOT NULL,"
          "studNum INTEGER NOT NULL,"
          "issueID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL UNIQUE)")
connection.commit()
def gotomain():
    call(["python", "main.py"])

def issueBook():
    global bookid, stdNum
    img = 'img/lib.png'
    img = cv2.imread(img)
    img = cv2.resize(img,(700,600))
    cv2.imwrite('img/lib.png',img)

    window = Tk()
    img = PhotoImage(file = 'img/lib.png')
    window.title("Issue book page")
    window.geometry("700x600")
    window.resizable(False,False)
    window.config(bg = 'black')

    lbl = Label(window)
    lbl.config(image = img)
    lbl.image = img
    lbl.place(x = 0,y = 0)

    btnback = Button(window,width= 10,height=2,bg = 'red', fg = 'white',text='Back',
                     command=lambda: [window.destroy(), gotomain()])
    btnback.place(x = 20, y =20)


    lblframe = Frame(window)
    lblframe.place(x=125,y=50)
    lbl = Label(lblframe,bg='black',fg='#fff',width= 40,height=4,text="Issue book here",font=('Arial',15))
    lbl.pack()

    lblframe = Frame(window,bg = 'black',)
    lblframe.place(x=120,y=250)
    enyframe = Frame(window,bg = 'black',)
    enyframe.place(x=190,y=250)

    lbl1 = Label(lblframe,width= 10,height=4, bg = 'black',fg = 'white',text='Book ID')
    lbl1.pack()
    lbl2 = Label(lblframe,width= 10,height=4,bg = 'black', fg = 'white',text='Reg Num')
    lbl2.pack()


    bookid = Entry(enyframe,width= 50, bg = 'white',font=("Arial",10),fg= "#000")
    bookid.pack(ipady=5,padx = 20,pady=18)

    stdNum = Entry(enyframe,width= 50,bg = 'white',font=("Arial",10),fg= "#000")
    stdNum.pack(ipady=5,padx = 20,pady=18)



    btnadd = Button(window,width= 10,height=2,
                    bg = 'orange', fg = '#000',text='Issue Book',font=("Arial",10),command=issuingBook)
    btnadd.place(x = 300,y = 500)
    window.mainloop()



def issuingBook():
    id = bookid.get()
    regnum = stdNum.get()
    stat = 0
    if id == '' or regnum == '':
        tkinter.messagebox.showinfo("Failed","Enter All Fields")
    else:
        c.execute("Select status from addBook where bookid = ?",(id,))
        istaken = c.fetchone()
        if istaken:
            if istaken[0] == 1:
                c.execute("INSERT INTO issueBook(bookid,studNum) VALUES (?,?)", (id, regnum,))
                connection.commit()
                c.execute("Update addBook SET status = (?) where bookid = ?", (stat,id,))
                connection.commit()
                tkinter.messagebox.showinfo("succes", "Book Issued Successfuly")
            else:
                tkinter.messagebox.showinfo("Failed", "Book isn't availabe")
        else:
            tkinter.messagebox.showinfo("Failed", "There is no such book")

