
def secret_password(message):
    if all(c.isalpha() and c.islower() for c in message) and len(message) == 9:
        p1, p2, p3 = message[:3], message[3:6], message[6:]
        p1 = str(ord(p1[0]) - 96) + p1[1] + str(ord(p1[2]) - 96)
        p2 = p2[2] + p2[1] + p2[0]
        p3 = "".join(chr((ord(c) - 96) % 26 + 97) for c in p3)
        return p2 + p3 + p1
    return "BANG! BANG! BANG!"

