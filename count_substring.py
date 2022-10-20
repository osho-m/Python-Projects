str=input("Enter a string: ");
d={};
for i in str:
      d[i]=str.count(i);

print(d);
print(type(d));
