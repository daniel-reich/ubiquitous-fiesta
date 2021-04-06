
def mystery_func(txt):
    return  ''.join([txt[i]*int(txt[i+1]) for i in range(0,len(txt),2)])

