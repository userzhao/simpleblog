#/usr/bin/python
with open('base.html') as f:
	b=f.read().decode('gbk')
	with open('base1.html','a+') as f:
		f.write(b.encode('utf8'))

