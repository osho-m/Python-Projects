def find_dup(l):
      mycount=0;
      for i in l:
            mycount=l.count(i);
            print('item: ', i, 'count: ', mycount);
            if mycount>1:
                  return True;
            
a=[1, 2, 3, 4, 5, 3];
c=find_dup(a);
if c==True:
      print("There are duplicate Items");
else:
      print("There are NO duplicate Items");
