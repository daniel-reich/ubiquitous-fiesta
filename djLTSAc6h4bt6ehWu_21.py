
def camelCasing(txt):
    rep = txt.lower().replace("_", " ")
​
    s = rep.split()
​
    answer = [s[0]]
​
    for i in s[1:]:
        answer.append(i[0].upper() + i[1:])
​
    return "".join(answer)

