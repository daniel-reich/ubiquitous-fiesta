
def missing_letter(txt):
    for i, j in zip(txt, txt[1:]):
        if ord(i) + 1 - ord(j):
            return chr(ord(i) + 1)
    return 'No Missing Letter'

