import math;
def ball_collide(x1, x2, y1, y2, r1, r2):
      dist=math.sqrt((x1-x1)**2 + (y1-y2)**2);
      print("Distance between two balls: ", dist);

      if dist<(r1+r2):
            print("The balls are Colliding");
            return True;
      else:
            print("The balls are NOT Colliding");
            return dist;
x1=int(input('Enter x1'));
x2=int(input('Enter x2'));
y1=int(input('Enter y1'));
y2=int(input('Enter y2'));
r1=int(input('Enter r1'));
r2=int(input('Enter r2')); 
c=ball_collide(x1, x2, y1, y2, r1, r2);
print(c);
