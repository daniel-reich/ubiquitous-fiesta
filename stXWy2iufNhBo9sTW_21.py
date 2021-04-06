
def valid_rondo(s):
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    seq = s[0] + s.replace('A', '')
    return seq in alph[:len(seq)] and s.endswith('A') and len(seq) > 1

