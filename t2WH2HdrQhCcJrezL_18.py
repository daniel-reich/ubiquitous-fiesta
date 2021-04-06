
def eda_bit(start, end):
    newtxt = []
    for i in range(start, end+1):
        if i % 3 == 0 and i % 5 == 0:
            newtxt.append("EdaBit")
        elif i % 3 == 0:
            newtxt.append("Eda")
        elif i % 5 == 0:
            newtxt.append("Bit")
        else:
            newtxt += [i]
    return newtxt

