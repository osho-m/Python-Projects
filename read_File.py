import os;
countline=0;
countch=0;
s=[];
file=open("D:\Courses\Python\Programs\evenOdd.py")
filename, file_extention=os.path.splitext("D:\Courses\Python\Programs\evenOdd.py");

if(file_extention=='.py'):
      print(filename, ": A python file");
      
for line in file:
      countline+=1;
      for c in line:
            countch+=1;
print("Number of lines: ", countline);
print("Number of Characters: ", countch);
file=open("D:\Courses\Python\Programs\evenOdd.py")
for l in file:
      k=len(l);
      type(l);
      for i in range(k-1, 0, -1):
            print (l[i], end="");
