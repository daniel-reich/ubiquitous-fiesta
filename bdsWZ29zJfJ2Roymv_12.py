
def swap_two(txt):
    chunkified = [txt[i:i+2] for i in range(0,len(txt), 2)]
    swapped = [(y,x) if len(y) == 2 and len(x) == 2 else (x,y) for (x,y) in zip(chunkified[0::2], chunkified[1::2])]
    if len(chunkified) % 2 == 0:
        return ''.join(i[0]+i[1] for i in swapped)
    elif len(chunkified) % 2 == 1:
        return ''.join(i[0]+i[1] for i in swapped) + chunkified[-1]

