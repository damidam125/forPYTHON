from tkinter import messagebox

__author__ = 'dami'

from tkinter import * # Tk, Text, BOTH, W, N, E, S
from tkinter.ttk import Frame, Button, Label, Style
import sqlite3
import manage_Book

class BookManagerGUI(Frame):
    def __init__(self, parent):
        self.man = manage_Book.MyDb('book.db') #DB에 접근하는 변수

        Frame.__init__(self, parent) #MAIN FRAME만들기
        self.parent = parent
        self.table_name = 'manager'
        self.conn = sqlite3.connect('book.db')
        self.cursor = self.conn.cursor()
        self.initUI()


    def initUI(self):
        self.parent.title("Windows")
        self.style = Style()
        self.style.theme_use("default")
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(1, weight=1)
        self.columnconfigure(3, pad=7)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(5, pad=7)

        lbl = Label(self, text="BookManager")
        lbl.grid(sticky=W, pady=4, padx=5)

        self.area = Text(self) #WHITE TEXT BOX
        self.area.grid(row=1, column=0, columnspan=3, rowspan=4,
            padx=5, sticky=E+W+S+N)

        abtn = Button(self, text="add", command=self.press_add)
        abtn.grid(row=1, column=3)

        srcbtn = Button(self, text="search", command=self.press_search)
        srcbtn.grid(row=2, column=3, pady=3)

        rbtn = Button(self, text="remove", command=self.press_remove)
        rbtn.grid(row=3, column=3, pady=3)

        sbtn = Button(self, text="show all", command=self.press_show)
        sbtn.grid(row=4, column=3, pady=3)

    def create_new_frame(self, com): #CREATE SUB FRAME. TRIGGERED WHEN CLICKING BUTTONS ON MAIN FRAME.
        newFrame = Toplevel(self)
        newFrame.geometry('300x150')
        newFrame.wm_title('title')

        l = Label(newFrame, text='fill the blank : ')
        l.grid(sticky=W, pady=4, padx=5)
        Label(newFrame, text='name: ').grid(row=1)
        Label(newFrame, text='author: ').grid(row=2)
        Label(newFrame, text='price: ').grid(row=3)

        self.eName, self.eAuth, self.ePri, = Entry(newFrame), Entry(newFrame), Entry(newFrame)
        self.eName.grid(row=1, column=1)
        self.eAuth.grid(row=2, column=1)
        self.ePri.grid(row=3, column=1)

        okbtn = Button(newFrame, text="OK", command=com)
        okbtn.grid(row=4, column=0, pady=1)

        clsbtn = Button(newFrame, text="CLOSE", command=lambda: newFrame.destroy())
        clsbtn.grid(row=4, column=1, pady=1)

    def clear_entry(self): #sub frame에서 text entry를 공백으로 돌려주는 메소드
        self.eName.delete(0, 'end')
        self.eAuth.delete(0, 'end')
        self.ePri.delete(0, 'end')

    def press_add(self):
        self.create_new_frame(self.addDB)

    def press_search(self):
        self.create_new_frame(self.filter)

    def press_remove(self):
        self.create_new_frame(self.removeDB)

    def press_show(self): #main frame에서 show_all button클릭하면 실행
        self.area.delete(1.0, END) #원래의 text area를 공백으로 초기화
        lst = self.man.get_all_qr() #모든 쿼리(tuple타입)를 불러와 리스트에 저장
        for tup in lst:
            self.area.insert(INSERT, '{0}\n'.format(' '.join([str(i) for i in tup])))

    def addDB(self): #main frame의 add btn -> sub frame의 ok btn 순으로 클릭되면 실행. 중복되는 책이 있더라도 add해줌
        if '' in (self.eName.get(), self.eAuth.get(), self.ePri.get()):
            #name, author, price칸이 하나라도 비어있으면 경고
            messagebox.showinfo('warning', 'please fill all of the field')
            return;

        lst=[ { 'name': self.eName.get(), 'author': self.eAuth.get(), 'price':int(self.ePri.get()) } ]
        self.man.add_qr(lst)
        self.clear_entry()

    def filter(self): #main frame의 search btn -> sub frame의 ok btn 순으로 클릭되면 실행. filter는 book name으로만 했음
        if '' is self.eName.get(): #name칸이 비어있으면 경고
            messagebox.showinfo('warning', 'please fill the field : name')
            return self.press_search()

        self.area.delete(1.0, END)
        lst = self.man.get_filtered_qr(self.eName.get()) #필터된 리스트를 받아옴
        for tup in lst:
            self.area.insert(INSERT, '{0}\n'.format(' '.join([str(i) for i in tup])))
        self.clear_entry()

    def removeDB(self): #main frame의 remove btn -> sub frame의 ok btn 순으로 클릭되면 실행. book name과 author이 일치하면 제거
        if '' in (self.eName.get(), self.eAuth.get()):
            messagebox.showinfo('warning', 'please fill field : name and author')
            return self.press_remove()

        self.man.del_qr(self.eName.get(), self.eAuth.get())
        self.clear_entry()


def main():
    root = Tk()
    root.geometry("400x500")
    app = BookManagerGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()