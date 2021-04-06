
def is_unfair_hurdle(hurdles):
    if (len(hurdles) >= 4):
        saida = True
    elif (len(hurdles[0].split('#')[1]) < 4):
        saida = True
    else:
        saida = False
    return saida

