
def guess_score(code, guess):
    black = 0
    white = 0
    for c in range(0, len(code)):
        if code[c] == guess[c]:
            black+=1
        elif code[c] in guess:
            white+=1
    return {'black': black, 'white': white}

