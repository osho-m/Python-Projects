x=1;
p=1;
total=0;
a, b=1,2;
print(a, b)
while x<2000000:
      for i in range (2, int(b/2)):
            if b%i==0:
                  p=0;
      if p==0:
            print(b, 'is not prime')
            p=1;
      else:
            print(b, 'is Prime')
            total+=b;
      a, b=b, a+b;
      x=b;
print('Sum of primes =', total);
