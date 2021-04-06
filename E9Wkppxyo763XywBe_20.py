
def binary_clock(time):
    binary = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001'
    }
    nums = filter(lambda n: n.isdigit(), time)
    bins = map(lambda b: binary.get(b), nums)
    clock = list(''.join(row) for row in zip(*bins))
    clock[0] = ' ' + ' '.join(clock[0][1::2])
    clock[1] = ' ' + clock[1][1:]
    return clock

