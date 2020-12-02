import re
def text_match(text):
    patterns = '\w*ab.\w*'
    if re.search(patterns, text):
        return 'Matched!'
    else:
        return 'Not matched!'

print(text_match("The girl will gab!"))
print(text_match("Python Internship!"))