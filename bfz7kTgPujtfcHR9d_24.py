
def x_pronounce(txt):
    lst = txt.split()
    for x in range(len(lst)):
        if lst[x] == "x":
            lst[x] = "ecks"
        elif lst[x].startswith("x"):
            word = lst[x][1:]
            lst[x] = "z" + word
        elif "x" in lst[x]:
            replaced = lst[x].replace("x", "cks")
            lst[x] = replaced
    return " ".join(lst)

