import re
x='dine2004'
res=re.search(r'\d+',x)
f=int(res.group())
print(f)


