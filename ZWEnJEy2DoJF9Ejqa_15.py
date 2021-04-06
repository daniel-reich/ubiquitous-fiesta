
def edabit_in_string(txt):
    answer = []
    for char in "edabit":
        if char not in txt:
            return ("NO")
            answer.append(1)
            break
        else:
            txt = txt.split(char,1)[1]
    if answer == []:
        return ("YES")

