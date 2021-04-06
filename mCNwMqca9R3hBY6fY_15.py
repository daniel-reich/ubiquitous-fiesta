
def make_happy(txt):
    characters = [':', '8', 'x', ';']
    list_txt = list(txt)
    for pos, char in enumerate(list_txt):
        if char in characters:
            if list_txt[pos + 1] == "(":
                list_txt[pos + 1] = ')'
​
    return ''.join(list_txt)

