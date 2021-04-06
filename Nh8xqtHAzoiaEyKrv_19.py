
def correct_sentences(s):
    low = s.split()
    low[0] = low[0].capitalize()
    low[-1] += '.'
    for i in range(1,len(low)):
        if low[i][0].isupper():
            low[i-1] += '.'
    return ' '.join(low)

