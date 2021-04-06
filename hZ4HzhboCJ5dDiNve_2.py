
def special_reverse_string(txt):
    new_txt = []
    special_reversed = []
    for char in reversed(txt):
        if char != " ":
            new_txt.append(char.lower())
​
    j = 0
    for i in range(0, len(txt)):
​
        if txt[i] != " " and txt[i].isupper():
            special_reversed.append(new_txt[j].upper())
            j += 1
        elif txt[i] == " ":
            special_reversed.append(" ")
        else:
            special_reversed.append(new_txt[j])
            j += 1
​
    return "".join(special_reversed)

