
def binary_clock(time):
    time = time.replace(':','')
    result = [];
    for i,v in enumerate(time):
        binary = bin(int(v)).replace('0b', '')
        if i == 0:
            result+=['  '+binary.zfill(2)]
        elif i == 2 or i == 4:
            result+=[' '+binary.zfill(3)]
        else:
            result+=[binary.zfill(4)]
    result = map(list, zip(*result))
    return [''.join(row) for row in result]

