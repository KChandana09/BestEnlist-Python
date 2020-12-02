import re
string = input("Enter the string:")
results = re.finditer(r'([0-9]{1,3})', string)
print("Numbers of length between 1 to 3")
for n in results:
     print(n.group(0))