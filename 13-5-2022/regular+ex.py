import re
text="welcome to python,tttt,ttt,t,ta,tm"
a=re.search("t",text)
print(a)
b=re.findall("t",text)
print(b)
c=re.split("t",text)
print(c)
d=re.search("mam",text)
print(d)
e=re.search("^w.to$",text)
print(e)
f=re.findall("to|To",text)
print(f)
k=re.sub("to","TO",text)
print(k)
