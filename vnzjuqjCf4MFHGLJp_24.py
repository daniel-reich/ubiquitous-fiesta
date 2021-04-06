
def shift_letters(s, n):
    spaces = list(t[0] for t in enumerate(s) if t[1] == ' ')
    chrs = s.replace(' ', '')
    shift = n % len(chrs)
    chrs = chrs[-shift:] + chrs[:-shift]
    chunks = [0] + [spaces[i] - i for i in range(len(spaces))] + [len(chrs)]
    return ' '.join(chrs[chunks[i]:chunks[i+1]] for i in range(len(spaces)+1))

