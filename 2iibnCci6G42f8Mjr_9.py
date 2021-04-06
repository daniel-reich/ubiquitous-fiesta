
def guess_score(code, guess):
    nms_code = set()
    nms_guess = set()
    blacks = 0
    for ix in range(len(code)):
        if code[ix] == guess[ix]:
            blacks += 1
        else:
            nms_code.add(code[ix])
            nms_guess.add(guess[ix])
    return {'black': blacks, 'white': len(nms_code.intersection(nms_guess))}

