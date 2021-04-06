
def number_pairs(txt):
    txt  = txt.split(' ')
    numLis =  txt[1:]
    pair = 0
    while len(numLis):
        count = numLis.count(numLis[0])
        pair += count//2
        numLis = list(filter(lambda n: n !=numLis[0], numLis))
    return pair

