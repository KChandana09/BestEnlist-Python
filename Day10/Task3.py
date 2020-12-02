import re
def text_match(text):
    patterns = '[0-9]+$'
    if re.search(patterns, text):
        return 'Matched!'
    else:
        return 'Not matched!'

print(text_match("eg3"))
print(text_match("36eg"))