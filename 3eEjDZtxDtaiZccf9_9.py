
def can_play(hand, face):
    for card in hand:
        if card[:4] in face or card[-1] in face:
            return True
    return False

