
from re import *
​
​
def markdown(symb):
    def func(text, word):
        p = compile(word.lower())
        iterator = p.finditer(text.lower())
        places = []
        for i in iterator:
            places.append(i.span())
        new_text = []
        if len(places) > 0:
            place = False
            for count, i in enumerate(text):
                if count == places[0][0]:
                    new_text.append(symb)
                    place = True
                if place and i == ' ':
                    place = False
                    new_text.append(symb)
                    if len(places) > 1:
                        del places[0]
                new_text.append(i)
        else:
            return text
        if place:
            place = False
            new_text.append(symb)
            if len(places) > 1:
                del places[0]
        return ''.join(new_text)
​
    return func

