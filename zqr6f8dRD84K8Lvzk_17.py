
def make_hex_list(n):
    res, i = [1], 0
    while res[-1] < n:
        i += 1
        res.append(3 * i * (i + 1) + 1)
    return res
​
​
n_max = 7777
hex_lst = make_hex_list(n_max)
​
​
def hex_lattice(n):
    if n not in hex_lst:
        return 'Invalid'
    idx = hex_lst.index(n)
    res = ' ' + ' '.join('o' for _ in range(2 * idx + 1)) + ' \n'
    for i in range(1, idx + 1):
        line = (' ' + ' ' * i + ' '.join('o' for _ in range(2 * idx + 1 - i))
                + ' ' * i + ' \n')
        res = line + res + line
    return res[:-1]

