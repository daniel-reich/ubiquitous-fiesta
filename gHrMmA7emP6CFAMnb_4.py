
def is_apocalyptic(number):
    n = str(2**number)
    x = n.count('666')
    return ["Safe", "Single", "Double", "Triple"][x]

