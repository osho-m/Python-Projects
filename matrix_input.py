r1=int(input('Enter r1: '));
c1=int(input('Enter c1: '));
r2=int(input('Enter r2: '));
c2=int(input('Enter c2: '));
if r1==r2 and c1==c2:
      print("Addition is possible");
else:
      print("Addition is NOT possible");
x=[[int(input(('Enter x',i, j, 'value: '))) for j in range (c1)]for i in range (r1)]



y=[[int(input(('Enter x',i, j, 'value: '))) for j in range (c2)]for i in range (r2)]
print('x=', x);
print('y=', y);

print('concatination=', x+y);
z=[[x[i][j]+y[i][j] for j in range (len(x))]for i in range (len(x[0]))]
print('sum=', z);
m= [[0 for j in range(c2)] for i in range(r1)]
for i in range (r1):
      for j in range (c2):
            for k in range (r2):
                  m[i][j]+=x[i][k]*y[k][j];
print('mul=', m);
