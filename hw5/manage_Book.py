import sqlite3
import bring_data

'''
sqlite3 모듈을 통해 book.db를 관리하는 모듈

'''

class MyDb:
    def __init__(self, db_file):
        self.table_name = 'manager' #테이블 이름 설정
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def create_table(self): #테이블을 생성하는 메소드
        query = '''CREATE TABLE manager ( BOOKNAME VARCHAR(10), AUTHOR VARCHAR(10), PRICE INTEGER )'''
        self.cursor.execute(query)

    def add_qr(self, lst): #lst는 dict type의 element들을 가짐. list의 element를 db파일에 insert해주는 메소드
        for dic in lst:
            self.cursor.execute('INSERT INTO ' + self.table_name +
                                ' VALUES (?,?,?)', [dic["name"], dic["author"], dic["price"]])
            self.conn.commit();

    def get_filtered_qr(self, bn): #BOOKNAME으로 FILTER한 결과를 반환해줌
        self.cursor.execute('select * from '+self.table_name + ' where BOOKNAME="%s"' %bn)
        lst = self.cursor.fetchall()
        return lst

    def del_qr(self, *args): #BOOKNAME과 AUTHOR모두 일치하면 삭제
        self.cursor.execute('DELETE FROM ' + self.table_name + ' WHERE BOOKNAME="%s" AND AUTHOR="%s"' %(args[0], args[1]))
        self.conn.commit();

    def get_all_qr(self):
        self.cursor.execute('select * from '+ self.table_name )
        lst = self.cursor.fetchall()
        return lst


def main():
    dataList = bring_data.bring_Data().get_data()

    myDB = MyDb('book.db')
    #myDB.create_table()
    #myDB.add_qr(dataList)
    myDB.get_all_qr()

if __name__ == '__main__':
    main()