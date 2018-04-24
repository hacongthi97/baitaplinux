#!/usr/bin/python
n = input('n = ')
a = []
for i in range(n):
	a.append(input('a[%d] = ' %i))
print "Day so vua nhap"
print a
tong = 0
for i in range(n):
	if(a[i]%2 == 0):
		tong += a[i]
print 'Tong cac phan tu chan: ',tong

#Sap xep mang

print 'Sau khi sap xep: '
a.sort()
print a
