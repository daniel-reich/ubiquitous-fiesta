
def letter_at_position(n):
    if n != int(n) or n == 0:
        return 'invalid'
    else:
        return ('abcdefghijklmnopqrstuvwxyz')[int(n)-1]

