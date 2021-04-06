
def num_split(num):
    l = [int('{}{}'.format(x, '0' * i)) for i, x in enumerate(str(num)[::-1])][::-1]
    if num < 0:
        l = l[1:]
    return [-i if num < 0 else i for i in l]

