import re
#p=r"hello"
s="hello"
k=re.search(r'h..*', s, re.M|re.I)
if k:
    print (k.group())
else: print("No match")
