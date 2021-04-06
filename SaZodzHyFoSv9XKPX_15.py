
def domino_chain(dominos):
    if dominos.count("|") == len(dominos):
        return "/" * len(dominos)
    s = "";
    C = 0;
    for i in range(len(dominos)):
        if dominos[i]=="|" and dominos[0] == "|":
            s += "/";
        elif dominos[i] == "/" or dominos[i] == " ":
            C = i;
            break
    return s + dominos[C:]

