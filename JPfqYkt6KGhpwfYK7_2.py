
def replace_the(txt):
    lst = txt.split(" ")
    for index, i in enumerate(lst):
        if i == "the":
            if lst[index+1][0] in "aeiou":
                lst[index] = "an"
            else:
                lst[index] = "a"
    return " ".join(lst)

