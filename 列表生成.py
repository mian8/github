# -*- coding: utf-8 -*-
'''
d={'a':'Q','s':'W','d':'E'}

q=[k.upper()+'='+v.lower() for k,v in d.items()]#.upper()转换为大写；.lower转换为小写
print(q)				#‘+’为连接符号；.items（）列表条目；.values输出字典后面的值
'''

#生成器
def fi(max):
	n,a,b=0,0,1
	while n<max:
		print(b)
		a,b=b,a+b
		n=n+1
	return 'done'
	
	
print(fi(int(input('斐波拉契数列'))))