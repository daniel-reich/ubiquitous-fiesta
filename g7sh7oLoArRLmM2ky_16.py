
def baconify(msg, mask=''):
    key_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", " "]
    value_list = ["uuuuu", "uuuul", "uuulu", "uuull", "uuluu", "uulul", "uullu", "uulll", "uluuu", "uluul", "ululu",
                  "ulull", "ulluu", "ullul", "ulllu", "ullll", "luuuu", "luuul", "luulu", "luull", "luluu", "lulul",
                  "lullu", "lulll", "lluuu", "lluul", "llllu", "lllll"]
    if mask == '':
        ciphertext = ""
        for i in range(len(msg)):
            if not((msg[i] < 'a' or msg[i] > 'z') and (msg[i] < 'A' or msg[i] > 'Z')):
                ciphertext += msg[i]
        i = 0
        text = ''
        loc = 4
        cate = int(len(ciphertext) / 5)
        while i < cate * 5:
            if i == loc:
                text += ciphertext[i]
                text += ' '
                loc += 5
            else:
                text += ciphertext[i]
            i += 1
        ciphertext = text
        text = ''
        list = ciphertext.split(' ')
        print(list)
        for i in range(len(list) - 1):
            cuv = ''
            for j in range(5):
                if list[i][j] >= 'a':
                    cuv += 'l'
                else:
                    cuv += 'u'
            nr = value_list.index(cuv)
            text += key_list[nr]
        return text
    else:
        msg = msg.lower()
        plaintext = ''
        for i in range(len(msg)):
            if msg[i] == '.' or msg[i] == ' ':
                plaintext += msg[i]
            elif not((msg[i] < 'a' or msg[i] > 'z') and (msg[i] < 'A' or msg[i] > 'Z')):
                plaintext += msg[i]
        msg = plaintext
        plaintext = ''
        i = 0
        a = 0
        while i < len(msg):
            nr = key_list.index(msg[i])
            cuv = value_list[nr]
            print(cuv)
            for j in range(5):
                if mask[a] == ' ' or mask[a] == ':' or mask[a] == ',' or mask[a] == ';' or mask[a] == '.':
                    plaintext += mask[a]
                    a += 1
                if mask[a] == ' ' or mask[a] == ':' or mask[a] == ',' or mask[a] == ';' or mask[a] == '.':
                    plaintext += mask[a]
                    a += 1
                if cuv[j] == 'u' and mask[a] >= 'a':
                    plaintext += chr(ord(mask[a]) - 32)
                    a += 1
                elif cuv[j] == 'u' and mask[a] < 'a':
                    plaintext += mask[a]
                    a += 1
                elif cuv[j] == 'l' and mask[a] < 'a':
                    plaintext += chr(ord(mask[a]) + 32)
                    a += 1
                elif cuv[j] == 'l' and mask[a] >= 'a':
                    plaintext += mask[a]
                    a += 1
            i += 1
        plaintext += mask[a:]
        return plaintext

