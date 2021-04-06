
def retrieve(txt):
    result = []
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in txt.split(' '):
        try:
            if i[0].lower() in vowels:
                result.append(i.lower().strip('.'))
        except:
            IndexError
    return result

