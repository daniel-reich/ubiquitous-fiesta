
def get_missing_letters(s):
    return ''.join(sorted(set('abcdefghijklmnopqrstuvwxyz') - set(s)))

