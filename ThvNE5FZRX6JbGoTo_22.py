
def inverter(txt, type):
    if type == "P":
        y = []
        z = txt.split(" ")
        z.reverse()
        for i in range(len(z)):
            if i == 0:
                y.append(z[i].capitalize())
            else:
                y.append(z[i].lower())
        return " ".join(y)
    elif type == "W":
        x = txt.split(" ")
        y = []
        for i in range(len(x)):
            if i == 0:
                y.append(x[i][::-1].capitalize())
            else:
                y.append(x[i][::-1].lower())
        return " ".join(y)

