
def binary_clock(time):
    return [''.join([d if not ((i == 0 and (j % 2 == 0)) or (i == 1 and j == 0)) else ' ' for j, d in enumerate(x)]) for i, x in enumerate(zip(*['{:>04b}'.format(col) for n in [[int(x) // 10, int(x) % 10] for x in time.split(':')] for col in n]))]

