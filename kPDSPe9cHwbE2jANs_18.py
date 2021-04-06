
def cards_needed(n):
    if n >=0 :
        a = (n * (3 * n + 1 ) / 2 )
        return int(a)
    else:
        return 'invalid'

