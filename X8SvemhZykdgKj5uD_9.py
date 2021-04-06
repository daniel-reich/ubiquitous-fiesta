
def letter_at_position(n):
    if n < 1 or n > 26 or n%1 != 0:
        return 'invalid'
    else:
        return chr(int(n) + 96)

