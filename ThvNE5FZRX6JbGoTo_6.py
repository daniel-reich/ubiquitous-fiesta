
def inverter(txt, type):
    if type == "P":
        return " ".join(txt.split()[::-1]).capitalize()
    return " ".join([ch[::-1] for ch in txt.split()]).capitalize()

