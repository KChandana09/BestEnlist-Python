myfunction(x, y):   # syntax error
    return x + y

for x in range(a, b):                 # name error
    print("(%f, %f, %f)" % my_list[x]) 

marks = 10000    # logical error
a = marks / 0
print(a) 

X = 10          # attribute error
X.append(6)

if(a<3):        # indentation error
print("gfg")

x = 1           # assertion error
y = 0
print(x / y) 

default = 'Scruffy'         #key error
a = adict.get('dogname', default)

import sys                  # index error
try:
    my_list = [3,7, 9, 4, 6]
    print my_list[6]
except IndexError as e:
    print e
    print sys.exc_type

import sys                     # import error
try:
    from exception import myexception
except Exception as e:
    print e
    print sys.exc_type