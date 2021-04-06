
def bracket_logic(x):
    brackets = ["[","]","{","}","(",")","<",">"]
    openers, closers = brackets[::2],brackets[1::2]
    lst = []
    for i in x:
        if i in brackets and i in openers:
            lst.append(i)
        elif i in brackets and i in closers:
            if brackets[brackets.index(i) - 1] != lst[-1]:
                return False
            else:
                del lst[-1]
    return True if not lst else False

