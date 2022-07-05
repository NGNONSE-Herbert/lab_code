#print("Hello, World")
from pprint import pprint


x = 5           # x is of type int
y = "bonjour"   # y is of type str
a = b = c = 5 #, 2, 'Hello!'
print(a,b,c)
print(type(a))
v = 'Hi!'
pprint(type(v))

fruits = ['apple', 'banana', 'orange']
e, r, t = fruits
print(r,e,t)
print(r+e+t)
print(x,e)
""""
f = 'Hello!'
def myfunc():
    print('python is ' + f)
myfunc()

f = 'Hello!'
def myfunc():
    f = 'World'
    print('python is ' + f)
myfunc()
print("python is " + f)

import random
print(random.randrange(1, 6))

f = -1.2
v = int(f)
print(v)
a = "Hello, World!"
print(a[5])
"""
for x in "banana":
  print(x)

a = "Hello, World! "
print('l' not in a)
print(len(a))
print('Hello' in a)
if 'o' in a:
    print('o is present in a')
if 'l' not in a:
    print("no, 'k' is not in a")

