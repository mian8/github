# -*- coding: utf-8 -*-
#装饰器

import functools	#提供functools.wraps的支持

'''
def log(func):
	@functools.wraps(func) #需要functools支持
	def wrap(*args,**kw):
		print('call %s:' % func.__name__)
		return func(*args,**kw)
	return wrap
	
@log  #now=log(now)
def now():
	print('2015-3-25')
'''
'''
f=now
f()
print(f.__name__)
'''	
import functools

def wenben(text):
	def hanshu(func):
		@functools.wraps(func)	#需要functools支持
		def jieshou(*a,**b):
			print('%s %s():' % (text,func.__name__))
			func()
			print('小尾巴')
			return func(*a,**b)
		return jieshou
	return hanshu

@wenben('飞龙在天') #log('飞龙在天')(now)
def now():
	print('2015-3-25')

print(now())
print(now.__name__)


#	既支持：
#	@log
#	def f():
#		pass
#	又支持：
#	@log('execute')
#	def f():
#		pass

import functools
def log(text):
    if isinstance(text,str):
        def decorator(func):
            @functools.wraps(func)
            def wrapper (*args,**kw):
                print('%s %s():' % (text,func.__name__))
                return func(*args,**kw)
            return wrapper
        return decorator
    else:

        @functools.wraps(text)
        def wrapper(*args, **kw):
            print('call %s():' % text.__name__)
            return text(*args, **kw)
        return wrapper



