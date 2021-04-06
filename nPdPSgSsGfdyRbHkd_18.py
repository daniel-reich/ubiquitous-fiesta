
def hacker_speak(txt):
    lst = list(txt)
    for a in range(len(lst)):
        if lst[a] == "a":
            lst[a] = "4"
        if lst[a] == "e":
            lst[a] = "3"
        if lst[a] == "i":
            lst[a] = "1"
        if lst[a] == "o":
            lst[a] = "0"
        if lst[a] == "s":
            lst[a] = "5"
    return ''.join(lst)

