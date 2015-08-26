#merge multiple text file

import glob
original = open('origin.txt', 'w')
lst = glob.glob('*.txt')
for fn in lst:
    with open(fn, 'r') as f:
        data = f.read()
        original.write(data)
