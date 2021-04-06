
def uncensor(str1, xlate):
    star_pos = 0; newlist = []
    for letter in str1:
        if letter == '*':
            newlist.append(xlate[star_pos])
            star_pos += 1
        else:
            newlist.append(letter)
    return ''.join(newlist)

