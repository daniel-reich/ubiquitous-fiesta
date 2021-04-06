
def remix(txt, indexes):
    lengh = len(txt)
    new = ['' for i in range(lengh)]
    for (i, value) in enumerate(indexes):
        new[value] = txt[i]
    return "".join(new)

