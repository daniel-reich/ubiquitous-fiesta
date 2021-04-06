
def missing_letter(txt):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    first = alphabets.index(txt[0])
    last = alphabets.index(txt[-1])
    main = set(alphabets[first: last+1])
    txt = set(txt)
    final = "".join(list(main - txt))
    if final:
        return final
    else:
        return "No Missing Letter"

