
def guess_score(code, guess):
    black = 0
    white = 0
    for i in range(0, len(code)):
        if code[i] == guess[i]:
            black += 1
        elif code[i] in guess:
            white += 1
    return {"black": black, "white": white}

