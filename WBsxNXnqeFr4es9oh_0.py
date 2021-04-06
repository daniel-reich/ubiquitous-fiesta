
def encode(s):
    n = int((s - 1) ** .5) + 1
    for x, r in enumerate(range(n, 0, -2)):
        for y in range(x, x+r-(r>1)):
            for _ in range(4):
                yield x * n + y
                if r == 1: return
                x, y = y, n-x-1
​
def clockwise_cipher(message):
    table = {j: i for i, j in enumerate(encode(len(message)))}
    return ''.join(message[i] if i < len(message) else ' ' for i in map(table.get, range(len(table))))

