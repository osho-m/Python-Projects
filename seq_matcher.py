from difflib import SequenceMatcher;
def neary_equal(a, b):
      return SequenceMatcher(None, a, b).ratio();

a="India";
b="Indian";
c=neary_equal(a, b);
print('c=', c)
if(c*100==100):
      print('a and b are equaL');
elif(c*100>80):
      print('a and b are Nearly equaL');
else:
      print('a and b are Not equaL');
