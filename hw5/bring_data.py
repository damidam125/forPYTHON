__author__ = 'dami'
"""
data.txt에는 라인마다 dict 자료형 데이터가 있음. ex) {'name': 'book0', 'author': 'author0', 'price':'5000'}
data.txt의 dict를 불러와서 list에 append해줌
"""

from ast import literal_eval

class bring_Data:
    def __init__(self): #file opening
        self.f = open('data.txt', 'r')
        self.lst = []
    def convert_data(self): #data.txt에서 라인을 불러와 list에 append
        for line in iter(self.f.readline, ''):
            self.lst.append(literal_eval(line)) #literal_eval()를 통해 str을 dict로 형변환 -> list에 append
    def get_data(self): #list를 반환하는 함수
        self.convert_data()
        return self.lst

if __name__ == '__main__':
    df = bring_Data()
    df.get_data()