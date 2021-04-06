
def replace_vowels(txt, ch):
    voels = ['a','e','i','o','u']
    newtxt=''
    for i in range(len(txt)):
        if txt[i] in voels:
            newtxt+=ch
        else:
            newtxt += txt[i]
    return newtxt

