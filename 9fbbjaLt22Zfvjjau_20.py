
def paul_cipher(txt):
    char_alpha = [chr(i) for i in range(65, 91)]
    num = [chr(i) for i in range(48, 58)]
    char = [chr(i) for i in range(33, 48)]
    char2 = ["{", "|", "}", "~"]
    char.extend(char2)
    idx_previous = []
    sifra = []
    j = 0
    idx = []
    first_is_num = False
    for i in txt:
        first_is_num = False
        if txt.index(i) == 0:
            if i in num:
                sifra.append(i)
                first_is_num = True
            else:
                sifra.append(i.upper())
            if i.upper() in char_alpha:
                idx_previous.append(char_alpha.index(i.upper()))
​
        if i.upper() in char_alpha and txt.index(i) != 0 and first_is_num != True:
            idx = char_alpha.index(i.upper())
            if idx_previous != []:
                idx += idx_previous[j] + 1
                j += 1
            idx %= len(char_alpha)
            sifra.append(char_alpha[idx])
            idx_previous.append(char_alpha.index(i.upper()))
​
        if i in num and first_is_num != True:
            sifra.append(i)
​
        if i in char and first_is_num != True:
            sifra.append(i)
​
​
    return "".join(i for i in sifra)

