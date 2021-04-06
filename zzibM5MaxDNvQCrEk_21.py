
def will_fit(holds, cargo):
    for i in range(len(holds)):
        if holds[i] == "S" and cargo[i] > 50:
            return False
        if holds[i] == "M" and cargo[i] > 100:
            return False
        if holds[i] == "L" and cargo[i] > 200:
            return False
    return True

