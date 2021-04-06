
def guess_score(code, guess):
    black = 0
    setc, setg = set(), set()
    for i in range(len(code)):
        if code[i] == guess[i]:
            black += 1
        else:
            setc.add(code[i])
            setg.add(guess[i])
    white = len(setc & setg)
    return {'white':white, 'black':black}

