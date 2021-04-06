
def my_sub(a, b):
    binary_a = '0' * (8 - len(bin(a)[2:])) + bin(a)[2:]
    ones_comp = ''.join('0' if i == '1' else '1' for i in binary_a)
    twos_comp_plus_b = int(ones_comp, 2) + 1 + b
    return int(bin(twos_comp_plus_b)[-8:], 2)

