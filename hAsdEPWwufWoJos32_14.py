
def no_yelling(phrase):
    r_phrase = phrase[::-1]
    if phrase[-1]=="!":
        for i in r_phrase:
            if i == "!":
                r_phrase = r_phrase[r_phrase.index(i)+1:]
            else:
                r_phrase = r_phrase[r_phrase.index(i):]
                break
        return ("!"+r_phrase)[::-1]
​
    elif phrase[-1]=="?":
        for i in r_phrase:
            if i == "?":
                r_phrase = r_phrase[r_phrase.index(i)+1:]
            else:
                r_phrase = r_phrase[r_phrase.index(i):]
                break
        return ("?"+r_phrase)[::-1]
    else:
        return phrase

