
letters = "abcdefghijlmnopqrstuvwxyz"
​
map1 = {}
for row in range(5):
    for col in range(5):
        c = letters[5*row+col]
        map1[c] = '.' * (row + 1) + ' ' + '.' * (col + 1)
map2 = {v: k for k, v in map1.items()}
map1['k'] = '. ...'
​
def tap_code(text):
    if all([c in ['.', ' '] for c in text]):
        # decode:
        text = text.split()
        msg = ""
        for i in range(len(text) // 2):
            code = text[2*i] + ' ' + text[2*i+1]
            msg += map2[code]
        return msg
    else:
        # encode:
        return ' '.join([map1[c] for c in text])

