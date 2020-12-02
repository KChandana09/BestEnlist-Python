import re
def check_upper(string):
    char = re.compile(r'[^[A-Z]+$')
    string = char.findall(string)
    return not bool(string)

print(check_upper("ABCDabcd")) 
print(check_upper("ABCD"))  