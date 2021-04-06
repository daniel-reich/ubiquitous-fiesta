
def bomb(txt):
    t=txt.lower()
    word="bomb"
    if word in t:
        return "Duck!!!"
    else:
        return "There is no bomb, relax."

