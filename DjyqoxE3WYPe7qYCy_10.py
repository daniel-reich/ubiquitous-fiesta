
def reverse_odd(txt):
    new_txt = []
    for word in txt.split(' '):
        if len(word) % 2 != 0:
            word = list(reversed(word))
            new_txt.append("".join(word))
        else:
            new_txt.append(word)
    return " ".join(new_txt)

