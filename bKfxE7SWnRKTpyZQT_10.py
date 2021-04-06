
def replace_vowel(word):
    dict={'a':'1','e':'2','i':'3','o':'4','u':'5'}
    lst=[]
    for i in word:
        if i in 'aeiou':
            lst.append(dict[i])
        else:
            lst.append(i)
    return ''.join(lst)

