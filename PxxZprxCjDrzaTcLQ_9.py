
def vowel_links(txt):
    x = txt.split()
    y = x.pop(0)
    for item in x:
        if item[0] in 'aeiou' and y[-1] in 'aeiou':
            
            return True
        else:
            y = item
            
    return False

