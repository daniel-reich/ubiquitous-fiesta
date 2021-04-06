
def showdown(p1:str, p2:str):
    if p1.find("B") < p2.find("B"):
        return "p1"
    elif p1.find("B") > p2.find("B"):
        return "p2"
    else:
        return "tie"

