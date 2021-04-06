
def weight_allowed(car, p, max_weight):
    matyikaaa = 0
    for i in p:
        matyikaaa = matyikaaa + i
    max_weight = max_weight / 0.453592
    if matyikaaa + car < max_weight:
        return True
    else:
        return False

