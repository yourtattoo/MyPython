#!/usr/bin/python
def add(x,y):
    return x+y
x = float(raw_input("pls enter the 1st number:\n"))
y = float(raw_input("pls enter the 2ed number:\n"))
print add(x,y)
d = dict(name = "george",age = "24")
d.setdefault('address',[]).append("No.50")
print d
