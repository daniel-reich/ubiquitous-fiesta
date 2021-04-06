
def retrieve(txt):
    b = txt.split('.')
    return [i.lower() for i in b[0].split() if i[0] in 'aeiouAEIOU']

