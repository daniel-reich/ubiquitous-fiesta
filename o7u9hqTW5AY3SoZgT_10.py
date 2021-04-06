
import re
def switcheroo(txt):
    switch = ''
    for word in txt.split(' '):
        if re.search('nts(\W)*$',word) != None:
            word = re.sub('nts','nce',word)
            switch += word + ' '
        elif re.search('nce(\W)*$',word) != None:
            word = re.sub('nce','nts',word)
            switch += word + ' '
        else:
            switch += word + ' '
    return switch[:-1]

