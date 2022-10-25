import re
#p=r"hello"
s="hello welcome to Python class"
k=re.search(r'w.*. * ', s)
if k:
    print (k.group())
else: print("No match")
k=re.search(r'w\w', s)
print (k.group())
k=re.search(r'\Wi', s, re.M|re.I)
print (k.group())
