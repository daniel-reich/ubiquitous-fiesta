
def is_boiling(temp):
    if temp.endswith('F'):
        return int(temp[:-1]) >= 212
    else:
        return int(temp[:-1]) >= 100

