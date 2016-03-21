# -*- coding: utf-8 -*-
'''
def t(a,b,f):
	return f(a)*f(b)
	
	
n=t(-8,5,abs)
print(n)

def ji(a):
	return a*a

r=map(ji,([1,2,3,4,5,9]))#map()传入的第一个参数是f，即函数对象本身。
print(list(r))			#由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

list(map(str,[1,2,34,5,6,7,7,]))


from functools import reduce
def add(x,y):
	return x*10+y

print(reduce(add,[1,2,3,45,6]))  

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
	return name[0].upper()+name[1:].lower()
	
L1=['adam', 'LISA', 'barT']	
r=list(map(normalize,L1))
print(r)

#请编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce
def prod(name):
	return reduce(ff,name)
	
def ff(x,y):
	return x*y

print(prod([1,2,3,4,5,6,7]))


#filter将函数作用于每一个序列中的元素，如果是false将丢弃
def is_odd(n):
	return n%2==1
	
print(list(filter(is_odd,(1,2,3,4,5,67,9))))
'''
'''
#filter求素数
def _odd_iter():	#无限奇数序列
	n=1
	while True:
		n=n+2
		yield n
		
def _not_divi(n):	#筛选素数
	return lambda x:x%n >0
	
def primes():		#不断(无限)返回下一个素数
	yield 2
	it = _odd_iter()
	while True:
		n=next(it)
		yield n
		it = filter(_not_divi(n),it)

for n in primes():	#调用
	if n<1000:
		print(n)
	else:
		break
'''
'''
#排序算法：sorted()可以就受一个key函数来定义排序；如果x>y则返回-1
print(sorted([12,45,56,-23,-4,67]))
print(sorted([12,45,56,-23,-4,67],reverse=True))
print(sorted(['we','WS','Ew','aV']))
print(sorted(['we','WS','Ew','aV'],key=str.lower))
'''
S=[('Bob',75),('Adam',92),('Bart',66),('Lisa',86)]

def m(n):
	return n[0]	


def f(n):
	return n[1]
	
print(sorted(S))
print(sorted(S,key=f,reverse=True))
