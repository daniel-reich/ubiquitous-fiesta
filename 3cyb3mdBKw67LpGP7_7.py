
import itertools
​
def numbers_need_friends_too(n):
    emptystring = ''
    for key,group in itertools.groupby(str(n)):
        print(key)
        x = len(list(group))
        if x == 1:
            emptystring += str(key)*3
        else:
            emptystring += x*key
    return int(emptystring)

