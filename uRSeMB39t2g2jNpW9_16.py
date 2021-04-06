
repl = {'1': 'I', '2': 'Z', '3': 'E', '4': 'H', '5': 'S', '6': 'G',
        '7': 'L', '8': 'B', '9': '-', '0': 'O'}
​
def turn_calc(num):
    n = str(num).replace('.', '')[::-1]
    for a, b in repl.items():
        n = n.replace(a, b)
    return n

