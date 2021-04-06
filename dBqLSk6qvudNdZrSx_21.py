
def is_boiling(temp):
    unit =  temp[-1]
    deg = int(temp[:len(temp)-1])
    if unit == 'F' and deg >= 212:
        return True
    if unit == 'C' and deg >= 100:
        return True
    return False

