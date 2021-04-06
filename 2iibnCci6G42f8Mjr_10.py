
def guess_score(code, guess):
    black=sum(1 for i in range(len(guess)) if guess[i] == code[i])
    white=sum(min(code.count(i),guess.count(i)) for i in set(guess) if i in code)
    return {'black': black, 'white': (white-black)}

