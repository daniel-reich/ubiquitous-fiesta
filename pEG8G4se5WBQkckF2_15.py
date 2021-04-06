
def reverse_sort(txt):
    txt = txt.split(' ')
    txt.sort(key=lambda x: x.lower(),reverse=True)
    txt.sort(key=len,reverse=True)
    return ' '.join(txt)

