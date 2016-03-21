#-*- coding: utf-8 -*-
'''
std1={'name':'LJC','score':98}
std2={'name':'LXK','score':89}

def print_score(std):
	print('%s:%s"'%(std['name'],std['score']))
'''

class Student(object):
	def __init__(self,name,score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s:%s' % (self.name,self.score))
		
bart = Student('sdaas',59)
lisa = Student('new',98)
bart.print_score()
lisa.print_score()