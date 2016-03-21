# -*- coding: utf-8 -*-

import re,json,os
from urllib import request

def get_ip():
	try:
		url='http://members.3322.org/dyndns/getip'
		data=request.urlopen(url).read()
		data_ed=date.decode('gb2312')
		ip=re.search('^\d+\.\d+\.\d+\.\d+',data).group(0)
	except Exception as e:
		print (str(e))
	print(ip)
	
	
	
	
