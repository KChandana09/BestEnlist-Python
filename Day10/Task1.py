import re
def check_char(string):
    char = re.compile(r'[^a-zA-Z0-9.]')
    string = char.search(string)
    return not bool(string)

print(check_char("ABCDabcd3450")) 
print(check_char("*&%}{"))