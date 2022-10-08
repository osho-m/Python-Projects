import re

textfile = open('findsomething.txt', 'r')
matches = []
reg = re.compile("use")
for line in textfile:
    matches += [(reg.findall(line), line)]
textfile.close()
print(matches)
