#!/usr/bin/env python3
# -*- coding： utf-8 -*-
#文件模板
' a test module'# 模块的第一个字符串被视为文档注释

__author__='Michael Liao'#作者名
#正式代码
import sys #导入模块sys

def test():	
	args=sys.argv
	if len(args)==1:
		print('Hello, World')
	elif len (args)==2:
		print('hello, %s !'% args[1])
	else: 
		print('Too many arguements!')
		
if __name__=='__main__':
	test()