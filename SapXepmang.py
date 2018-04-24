n = input("Nhap n = ")
a = []
for i in range(n):
	a.append(input('a[%d] = '%i))
print 'Mang vua nhap la: '
print a
#sap xep mang
a.sort()
print 'Sau khi sap xep: '
print a
