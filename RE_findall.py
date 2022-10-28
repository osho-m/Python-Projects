import re
s='All cats are not wild cat'
p="cat"
mt=re.findall(p, s)
print(mt)
