
def c_decrypt(msg, keyword):
    L = len(keyword)
    n = len(msg)
    rows = n // L
    table = []
    for _ in range(rows):
        table.append(['x'] * L)
    k = 0
    for key in sorted(keyword):
        idx = keyword.find(key)
        for row in range(rows):
            table[row][idx] = msg[k]
            k += 1
    plain = ""
    for row in table:
        plain += ''.join(row)
    return plain
​
def c_encrypt(msg, keyword):
    msg = msg.lower()
    msg = ''.join([char for char in msg.lower() if (('a' <= char <= 'z') or ('0' <= char <= '9'))])
    L = len(keyword)
    table = []
    while len(msg) > 0:
        table.append(msg[:L])
        msg = msg[L:]
    while len(table[-1]) < L:
        table[-1] += 'x'
    cipher = ""
    for key in sorted(keyword):
        idx = keyword.find(key)
        for row in range(len(table)):
            cipher += table[row][idx]
    return cipher
​
def c_cipher(msg, keyword):
    if all(['a' <= char <= 'z' or '0' <= char <= '9' for char in msg]):
        # it's a cipher so decrypt it:
        return c_decrypt(msg, keyword)
    else:
        # it's a plain text, so encrypt it:
        return c_encrypt(msg, keyword)

