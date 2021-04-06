
def bifid(text):
    text = text.upper()
    tabel = []
    nr = 0
    plaintext = ''
    ok = 2
    if ' ' in text:
        ok = 1
    else:
        ok = 0
    for i in range(len(text)):
        if (text[i] < 'a' or text[i] > 'z') and (text[i] < 'A' or text[i] > 'Z'):
            plaintext = plaintext
        else:
            plaintext += text[i]
    for i in range(5):
        a = []
        for j in range(5):
            if nr == 9:
                nr += 1
                a.append(chr(65 + nr))
                nr += 1
            else:
                a.append(chr(65 + nr))
                nr += 1
        tabel.append(a)
    linie1 = ''
    linie2 = ''
    if ok == 1:
        for i in range(len(plaintext)):
            for j in range(len(tabel)):
                if tabel[j][0] > plaintext[i]:
                    linie1 = linie1 + str(j)
                    linie2 = linie2 + str(tabel[j - 1] .index(plaintext[i]) + 1)
                    break
                if j == len(tabel) - 1 and ord(plaintext[i]) >= ord(tabel[j][0]):
                    linie1 = linie1 + str(j + 1)
                    linie2 = linie2 + str(tabel[j].index(plaintext[i]) + 1)
        linief = linie1 + linie2
        message = ''
        for i in range(0, len(linief), 2):
            message += tabel[int(linief[i]) - 1][int(linief[i + 1]) - 1]
        message = message.lower()
        return message
    else:
        linie1 = ''
        linie2 = ''
        for i in range(len(plaintext)):
            for j in range(len(tabel)):
                if tabel[j][0] > plaintext[i]:
                    linie1 = linie1 + str(j)
                    linie2 = linie2 + str(tabel[j - 1].index(plaintext[i]) + 1)
                    break
                if j == len(tabel) - 1 and ord(plaintext[i]) >= ord(tabel[j][0]):
                    linie1 = linie1 + str(j + 1)
                    linie2 = linie2 + str(tabel[j].index(plaintext[i]) + 1)
        linief = ''
        for i in range(len(linie1)):
            linief += linie1[i] + linie2[i]
        linie1 = linief[0:len(linie1)]
        linie2 = linief[len(linie2):]
        message = ''
        for i in range(len(linie1)):
            message += tabel[int(linie1[i]) - 1][int(linie2[i]) - 1]
        message = message.lower()
        return message

