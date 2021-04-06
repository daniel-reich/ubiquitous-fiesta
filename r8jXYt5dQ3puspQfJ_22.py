
def split(txt):
    vowels = 'aeiou'
    x = ""
    for i in txt:
        if i in vowels:
            x += i          
    for i in txt:
        if i not in vowels:
            x += i
    return (x)

