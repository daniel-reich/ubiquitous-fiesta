
def high_low(txt):
    ints = list(map(lambda x:int(x), txt.split()))
    return str(max(ints)) +' ' + str(min(ints))

