def find_unique(l):
      unique=set(l);
      print("Elements are", unique);
      for i in unique:
            count=l.count(i);
            print('item: ', i, 'count: ', count);
            if count>1:
                  return True;
            
a=input('Enter list Items: ');
b=a.split();
c=find_unique(b);
if c==True:
      print("There no Unique Items");
