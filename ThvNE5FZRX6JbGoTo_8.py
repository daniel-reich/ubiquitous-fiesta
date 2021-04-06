
def inverter(txt, type):
    old = txt.split()
    new = []
    if type == "P":
        new = old[-1::-1]
    else:
        for item in old:
            new.append(item[-1::-1])
    return (' ').join(new).lower().capitalize() #make final string lowercase and then capitalize first word

