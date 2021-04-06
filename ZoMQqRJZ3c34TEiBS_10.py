
def get_rectangle(table, digram):
    for row in range(5):
        for col in range(5):
            if table[row][col] == digram[0]:
                coord1 = (row, col)
            elif table[row][col] == digram[1]:
                coord2 = (row, col)
    return coord1, coord2
​
def digram_to_digram_encrypt(table, digram):
    coord1, coord2 = get_rectangle(table, digram)
    if coord1[0] == coord2[0]:
        # letters in same row of table:
        if coord1[1] == 4:
            c1 = table[coord1[0]][0]
        else:
            c1 = table[coord1[0]][coord1[1]+1]
        if coord2[1] == 4:
            c2 = table[coord1[0]][0]
        else:
            c2 = table[coord1[0]][coord2[1]+1]
    elif coord1[1] == coord2[1]:
        # letters in same column of table:
        if coord1[0] == 4:
            c1 = table[0][coord1[1]]
        else:
            c1 = table[coord1[0]+1][coord1[1]]
        if coord2[0] == 4:
            c2 = table[0][coord1[1]]
        else:
            c2 = table[coord2[0]+1][coord2[1]]
    else:
        # letters not in same row or column:
        c1 = table[coord1[0]][coord2[1]]
        c2 = table[coord2[0]][coord1[1]]
    return c1 + c2
​
def generate_table(key):
    chars = [chr(k) for k in range(65, 91)]
    table = [[None for _ in range(5)] for __ in range(5)]
    row, col = 0, 0
    for k in key:
        if not 'A' <= k <= 'Z' or k not in chars:
            continue
        table[row][col] = k
        chars.remove(k)
        col += 1
        if col == 5:
            col = 0
            row += 1
    for c in chars:
        if c == 'J':
            continue
        table[row][col] = c
        col += 1
        if col == 5:
            col = 0
            row += 1
    table1, table2 = {}, {}
    for i in range(65, 91):
        for j in range(65, 91):
            if i != j:
                digram1 = chr(i) + chr(j)
                if 'J' not in digram1:
                    digram2 = digram_to_digram_encrypt(table, digram1)
                    table1[digram1] = digram2
                    table2[digram2] = digram1
    return table1, table2
​
def playfair_encode(message, key):
    table1, table2 = generate_table(key)
    message = [char for char in message if 'A' <= char <= 'Z']
    cipher = ""
    while len(message) > 0:
        char1 = message.pop(0)
        if len(message) > 0 and message[0] != char1:
            char2 = message.pop(0)
        else:
            char2 = 'X'
        digram = char1 + char2
        digram2 = table1[digram]
        cipher += digram2
    return cipher
​
def playfair_decode(cipher, key):
    table1, table2 = generate_table(key)
    cipher = [char for char in cipher if 'A' <= char <= 'Z']
    msg = ""
    while len(cipher) > 0:
        char1 = cipher.pop(0)
        if len(cipher) > 0 and cipher[0] != char1:
            char2 = cipher.pop(0)
        else:
            char2 = 'X'
        digram = char1 + char2
        digram2 = table2[digram]
        msg += digram2
    return msg
​
def playfair(txt, keyword):
    if all(['A' <= c <= 'Z' for c in txt]):
        # cipher given, so decipher:
        txt = txt.replace('J', 'I')
        keyword = keyword.upper()
        msg = playfair_decode(txt, keyword)
        return msg
    else:
        # plaintext given, so encipher:
        txt = ''.join([c for c in txt.upper() if 'A' <= c <= 'Z']).replace('J', 'I')
        keyword = keyword.upper()
        cipher = playfair_encode(txt, keyword)
        return cipher

