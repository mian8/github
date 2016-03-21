# -*- coding: utf-8 -*-
'''
x的n（2）次方
def power(x,n=2):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s
x=int(input('平方基数'))
n=int(input('平方次数'))
print(power(x,n))
'''

'''平方和
def he(*num):
	sum=0
	for n in num:
		sum = sum +n*n*n
	return sum


print(he(1,2,3,4))'''


'''关键字参数'''
def person(name,age,*,city,**kw):

	print('name:',name,'age:','age',age,city,'other:',kw)
	
print(person('wang',30,city='beijing',da='smell',cs='qs'))