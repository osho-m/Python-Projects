import math;
def gcdc(n1, n2):
      gcd=math.gcd(n1, n2);
      return gcd;
def lcm(n1, n2):
      return n1*n2/ gcdc(n1, n2);
a=int(input('Enter first No: '));
b=int(input('Enter Second No: '));

c=gcdc(a, b);
print('GCD is', c);

d=lcm(a, b);
print('LCM is', d);
