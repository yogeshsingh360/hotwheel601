from sys import argv
import sys
if len(argv)<2:
    print("Too few command-line argument")
    sys.exit(1)
elif len(argv)>2:
    print("Too many command-line arguments")
    sys.exit(1)
if not argv[1].endswith('.py'):
    print("Not a pyhton file")
    sys.exit(1)
count=0
try:
    with open (argv[1],'r') as file:
        lines=file.readlines()
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)
for line in lines:
    if line.lstrip().startswith('#'):
        continue
    elif not line.lstrip():
        continue
    else:
        count+=1
print(count)
