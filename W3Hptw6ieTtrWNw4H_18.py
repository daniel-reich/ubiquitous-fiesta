
map1 = {}
for a in range(97, 123):
    b = a if a <= 105 else a - 1
    row, col = 1 + (b - 97) // 5, 1 + (b - 97) % 5
    map1[(row, col)] = chr(a)
map1[(2, 4)]= 'i'
map2 = {value: key for key, value in map1.items()}
map2['j'] = (2, 4)
​
def decipher(code):
    row = []
    for c in code:
        r, c = map2[c]
        row.append(r)
        row.append(c)
    L = len(row)
    row1, row2 = row[:L//2], row[L//2:]
    msg = ""
    for i in range(len(row1)):
        r, c = row1[i], row2[i]
        msg += map1[(r,c)]
    return msg
    
def encipher(text):
    row1, row2 = [], []
    for char in text.lower():
        if 'a' <= char <= 'z':
            row, col = map2[char]
            row1.append(row)
            row2.append(col)
    row = row1 + row2
    code = ""
    for i in range(len(row) // 2):
        r, c = row[2*i:2*i+2]
        code += map1[(r, c)]#str(row) + str(col)
    return code
​
def bifid(text):
    if all(['a' <= c <= 'z' for c in text]):
        # it's ciphertext, so decipher:
        return decipher(text)
    else:
        # it's a plain text, so encipher:
        return encipher(text)

