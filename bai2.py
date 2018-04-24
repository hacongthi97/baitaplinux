#!/usr/bin/python
a = input('a = ')
b = input('b = ')
def swap(a,b):
	a, b = b, a
    	return a,b
print('Sau khi hoan doi: ')
print swap(a,b)

