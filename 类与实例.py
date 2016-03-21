#-*- coding: utf-8 -*-
'''
class Student(object):
	pass

bart =Student()
print(bart)
print(Student)
bart.name='asdasdasdasd'
print(bart.name)
'''
'''
class Student(object):
	def __init__(self,name,score):
		self.score=name
		self.name=score
	def print_score(self):
		print('%s:%s' %(self.score,self.name))
	def get_grade(self):
		if self.name >=90:
			return 'A'
		elif self.name >=60:
			return 'B'
		else:
			return 'C'
		
bart=Student('asdasd',89)
print(bart.name,bart.score)
bart.print_score()
bart.get_grade()
bart.age=23		#和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
print(bart.age)

'''
#私有变量	
class Student(object):
	def __init__(self,name,score):#添加__可使对象变为私有，限制访问
		self.__name=name
		self.__score=score
	def print_score(self):
		print('%s:%s'%(self.__name,self.__score))
	def get_name(self):#限制访问后，增加get_name可以外部获取name
		return self.__name
	def get_score(self):
		return self.__score
	def set_score(self,score):#限制访问后，使用set_score可以修改score
		if 0<=score<=100:
			self.__score=score
		else:
			raise ValueError('bad score')
		
bart=Student('asdasd',89)
lisa=Student('asda',121)
#print(bart.__name)
print(bart.get_score())
print(lisa.set_score())
