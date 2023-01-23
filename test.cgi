#!/usr/bin/python3

print("Content-type: text/html")
print("")

def add(b):
    return b+b

a=2

print(add(a))
for i in range(a):
    print("Le chiffre: ",a)