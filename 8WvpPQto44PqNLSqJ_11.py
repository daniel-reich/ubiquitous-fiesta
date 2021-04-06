
def pad(message):
    diff = 140 - len(message)
    if diff == 0:
        return message
    if diff % 2 == 0:
        return message + " l" + "ol" * (diff // 2 - 1)
    else:
        return message + "l" + "ol" * (diff // 2)

