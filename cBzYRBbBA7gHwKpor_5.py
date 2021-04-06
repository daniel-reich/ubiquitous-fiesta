
def secret_password(message):
    if len(message) != 9 or any(x.isupper() for x in message)\
            or any(not x.isalpha() for x in message):
        return "BANG! BANG! BANG!"
    threes = [message[x:x + 3] for x in range(0, len(message), 3)]
    part_1 = str((ord(threes[0][0])-96))+threes[0][1]+str((ord(threes[0][2])-96))
    part_2 = threes[1][::-1]
    part_3_1 = []
    for x in threes[2]:
        if x == 'z':
            part_3_1.append('a')
        else:
            part_3_1.append(chr(ord(x)+1))
    part_3 = ''.join(part_3_1)
    return part_2+part_3+part_1

