__author__ = 'dami'

import ast

f = open('test.txt', 'r')
dic = {'a':'d', 'd':'m'}
#f.write(str(dic))


st = f.read()
print(ast.literal_eval(st))
