# -*- cod: utf-8 -*-
#一元二次方程求解
'''
import math
def er(a,b,c):
	q = ('%dx^2+%dx+%d'%(a,b,c))
	p = b*b-4*a*c
	m = (-b+p**0.5)/(2*a)
	n = (-b-p**0.5)/(2*a)
	return q,m,n
	
a=float(input('请输入a的值'))
b=float(input('请输入b的值'))
c=float(input('请输入c的值'))
q,m,n=(er(a,b,c))
print('一元二次方程为：%r'%q)
print('方程的两个解为：\n x1=%r\n x2=%r'%(m,n))
'''

'''
def move (n):
	if isinstance(n,str):
		return n
	else:
		d.pop(n)
		
'''
#杨辉三角
'''
def ccc(a,b):
	return a+b
def YH(n):
	k=1
	aaa=[]
	while n>k:
		if k==1:
			print([1])
		else:
			bbb=[1]+list(map(ccc,aaa[1:],aaa[:-1]))+[1]
			aaa=bbb
			print(bbb)
		k=k+1
			
		
c=int(input('请输入杨慧三角行数：'))
while c>0:
	YH(c)
	c=int(input('请输入杨慧三角行数：'))
'''

#菱形
'''
def lx(n):
	k=1
	while k<n:		
		print(' '*(n-k),'* '*k)
		k=k+1
	while k>0:
		print(' '*(n-k),'* '*k)
		k=k-1
'''
#规范用户名大小写
'''
def normalize():
	return name[0].upper()+name[1:].lower()
	
def sb(L)：
	return list(map(normalize,L))
	
L=input('请输入多个英文名')
'''
#接受list求积
'''
import reduce
def prod(L):
	return reduce(lambda x,y:x*y,L)
print(reduce(prod,[1,2,3,4,5]))	
'''
	
#转化浮点数字符串
'''
def ddd(x):
	def ccc(x):
		k=0
		z=(z for z in x[::-1])
		for n in z:
			k=k+1
			if n=='.':
				return k
	k=ccc(x)
	z=x[:len(x)-k]+x[len(x)-k+1:]
	def f1(x,y):
		return x*10+y
	def f2(s):
		return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
return (reduce(f1,map(f2,z)))/(10**(k-1))

'''

#sorted作用在list的每个元素上
'''
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(x):
	return x

def by_score(x):
	a = [a for a in x]
	return a[1]

list(sorted(L,key=by_name))
list(sorted(L,key=by_score,reverse=True)

'''
#简单爬虫
'''
import urllib.request as request	 #调用urllib.request抓取网页
import os								#用于切换工作目录
url='http://www.bilibili.com'
origin_bytes=request.urlopen(url).read()
origin_str=origin_bytes.decode(''utf-8)		#B站用的utf-8
open('123.html','w',encoding='utf-8').write(origin_str)#创建写入指定格式
'''
#学生类
'''
class Student(object):			#创建名为Student的类，继承object类
	def __init__(self,name,score):#__init__方法，创建实例的时候自动执行
		self.name=name
		self.score=score
	def print_score(self):
		print ('%s:%s'%self.name,self.score)
	
	def get_score(self):
		if self.score>=90:
			return'A'
		elif self.score>60:
			return'B'
		else:
			return 'C'

bart=Student('name','score')	#创建名为bart的实例：类+()；当有方法调用参数时就不能传入空参数
bart.son='zxc'					#绑定类中没有的属性
'''
	'''
#动物类
class Anamal(object):
	def __init__(self):			#类中的方法第一个参数必为self()，自动接收实例名为参数	
		pass
	def run(self):
		return 'anamal is running!'
		
class cat(Anamal):
	def run(self):
		print ('cat is running')
		
class dog(Anamal):
	pass
'''
