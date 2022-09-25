import os;
countline=0;
countch, nl, ws=0,0,0;
s=[];
file=open("D:\Courses\Python\Programs\evenOdd.py")
filename, file_extention=os.path.splitext("D:\Courses\Python\Programs\evenOdd.py");

if(file_extention=='.py'):
      print(filename, ": A python file");
      
for line in file:
      countline+=1;
      for c in line:
            countch+=1;
            if c==" ":
                  ws+=1;
            elif c=="\n":
                  nl+=1;
print("Number of lines: ", countline);
print("Number of Characters:", countch);
print("Number of Characters: %d \n Number of white space: %d \n Number of newline: %d "%(countch-ws-nl, ws, nl));
