
def guess_score(code, guess):
    d = {'black':0, 'white':0}
    seen = []
    for i in range(len(guess)):
        if guess[i] == code[i]:
            d['black'] += 1
            seen.append(i)
    for i in range(len(guess)):
        if guess[i] in code:
            for j in range(len(code)):
                if guess[i] == code[j] and j not in seen:
                    d['white'] += 1
                    seen.append(j)           
    return d

