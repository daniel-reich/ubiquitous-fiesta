
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
    msg = ""
    idx = 0
    while idx < len(code):
        if code[idx] == ' ':
            msg += ' '
            idx += 1
        else:
            row, col = int(code[idx]), int(code[idx+1])
            msg += map1[(row, col)]
            idx += 2
    return msg.replace('j', 'i')
    
def encipher(text):
    code = ""
    for char in text.lower():
        if char == ' ':
            code += char
        elif 'a' <= char <= 'z':
            row, col = map2[char]
            code += str(row) + str(col)
    return code
​
def polybius(text):
    try:
        k = int(text.replace(' ', ''))
        # it's pure numbers, so decipher:
        return decipher(text)
    except ValueError:
        # it's a text, so encipher:
        return encipher(text)

