
def remove_special_characters(txt):
    l = []
    for item in txt:
        if item in ['-','_',' '] or 'A'<=item<= 'Z'or 'a'<=item<='z' or '0'<=item<='9'  :
            l.extend(item)
    print(l)
    return ''.join([item for item in l])

