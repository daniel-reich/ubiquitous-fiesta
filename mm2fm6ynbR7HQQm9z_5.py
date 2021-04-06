
def knights_jump(position):
    letter, number = position
    number = int(number)
    pos_jump = []
    #big if block
    if ord(letter) >= 66 and number >= 3: pos_jump.append("{}{}".format(chr(ord(letter) - 1), number - 2))
    if ord(letter) <= 71 and number >= 3: pos_jump.append("{}{}".format(chr(ord(letter) + 1), number - 2))
    if ord(letter) >= 67 and number >= 2: pos_jump.append("{}{}".format(chr(ord(letter) - 2), number - 1))
    if ord(letter) <= 70 and number >= 2: pos_jump.append("{}{}".format(chr(ord(letter) + 2), number - 1))
    if ord(letter) >= 67 and number <= 7: pos_jump.append("{}{}".format(chr(ord(letter) - 2), number + 1))
    if ord(letter) <= 70 and number <= 7: pos_jump.append("{}{}".format(chr(ord(letter) + 2), number + 1))
    if ord(letter) >= 66 and number <= 6: pos_jump.append("{}{}".format(chr(ord(letter) - 1), number + 2))
    if ord(letter) <= 71 and number <= 6: pos_jump.append("{}{}".format(chr(ord(letter) + 1), number + 2))
    return ",".join(pos_jump)

