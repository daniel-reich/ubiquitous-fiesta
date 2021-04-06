
def camel_to_snake(s):
    for char in s:
        if char.isupper():
            s = s.replace(char, ('_'+char.lower()))
    return s

