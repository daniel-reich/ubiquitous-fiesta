
def unrepeated(txt):
    result = ''
    for i in txt:
        if i not in result:
            result += i
    return result

