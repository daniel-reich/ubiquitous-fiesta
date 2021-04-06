
def remove_abc(txt):
    res = ''.join(i for i in txt if i not in 'abc')
    return None if res == txt else res

