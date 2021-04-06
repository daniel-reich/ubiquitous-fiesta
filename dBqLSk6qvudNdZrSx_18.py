
def is_boiling(temp):
    if temp[-1] == 'F':
        return int(temp[:-1]) > 211
    else:
        return int(temp[:-1]) > 99

