
def get_name(string):
    alphabet, name = 'abcdefghijklmnopqrstuvwxyz', []
    for i in list(string):
        if i.lower() in alphabet:
            name.append(i)
        if i == "@":
            break
    return "".join(name)

