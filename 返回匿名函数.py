# -*- coding: utf-8 -*-

#返回函数：内部num引用外部count的参数和局部变量，返回sum函数是保留引用的参数
#每次调用都会返回新的函数
'''
def count(*qt):
	def sum():
		ax=0
		for n in qt:
			ax=ax+n
		return ax
	return sum
f=count(1,4,4,8,2)
print(f)
print(f())
'''

'''
#返回函数内部有新的参数时，需要添加一个新的函数
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(),f2(),f3())

def count():
	def f(i):
		def t():
			return i*i
		return t
	fs=[]
	for i in range(1,4):
		fs.append(f(i))
	return fs

f1,f2,f3=count()
print(f1(),f2(),f3())

'''
#匿名函数
print(list(map(lambda x:x*x,[1,2,3,4,5,6])))

def se(x,y):
	return lambda: x*x+y*y

	
