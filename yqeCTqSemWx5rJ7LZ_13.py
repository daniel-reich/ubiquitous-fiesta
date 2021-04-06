
def full_key_name(piece):
    last = piece.split()[-1]
    return '{} {} {}'.format(' '.join(piece.split()[:-1]) , last.title(),  ['minor', 'major'][last[0].isupper()])

