
def remove_special_characters(txt):
    x = ''
    for i in txt:
        if i == '-' or i == '_' or i == ' ':
            x += i
        elif i.isalnum():
            x += i
    return x

