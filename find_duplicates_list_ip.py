def find_dup(l):
      mycount=0;
      for i in l:
            mycount=l.count(i);
            print('item: ', i, 'count: ', mycount);
            if mycount>1:
                  return True;
            
a=input('Enter list Items: ');
b=a.split();
s=0;
for x in b:
      s+=int(x);
print(s);
c=find_dup(b);
if c==True:
      print("There are duplicate Items");
else:
      print("There are NO duplicate Items");
