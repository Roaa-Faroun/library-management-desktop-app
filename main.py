from tkinter import *
import cv2
import sqlite3
from tkinter import messagebox
import addBook
import deleteBook
import viewBook
import IssueBook
import returnBook

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

lblframe = Frame(window)
lblframe.place(x=140,y=50)
lbl = Label(lblframe,bg='black',fg='#fff',width= 40,height=4,text="Welcome to The Library App",font=('Arial',15))
lbl.pack()

btnframe = Frame(window)
btnframe.place(x=180,y=200)

btn1 = Button(btnframe,width= 50,height=4,bg = 'black', fg = 'white',
              text='Add Book',command=lambda:[window.destroy(),addBook.addbook()])
btn1.pack()

btn2 = Button(btnframe,width= 50,height=4,bg = 'black', fg = 'white',text='Delete Book',
                  command=lambda:[window.destroy(),deleteBook.deletebook()])
btn2.pack()

btn3 = Button(btnframe,width= 50,height=4,bg = 'black', fg = 'white',text='View Book',
                  command=lambda:[window.destroy(),viewBook.viewbook()])
btn3.pack()
btn4 = Button(btnframe,width= 50,height=4,bg = 'black', fg = 'white',text='Issue Book',
                  command=lambda:[window.destroy(),IssueBook.issueBook()])
btn4.pack()
btn5 = Button(btnframe,width= 50,height=4,bg = 'black', fg = 'white',text='Return Book',
                  command=lambda:[window.destroy(),returnBook.returnbook()])
btn5.pack()
window.mainloop()

