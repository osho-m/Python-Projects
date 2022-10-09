import re
pattern = re.compile("use")

for i, line in enumerate(open('findsomething.txt')):
    for match in re.finditer(pattern, line):
        print ('Found on line', i+1, match.group())
