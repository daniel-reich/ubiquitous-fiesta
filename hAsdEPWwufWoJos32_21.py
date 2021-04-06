
def no_yelling(phrase):
    phrase = list(phrase)
    while phrase[-2] in "!?":
        phrase.pop(-1)
    return "".join(phrase)

