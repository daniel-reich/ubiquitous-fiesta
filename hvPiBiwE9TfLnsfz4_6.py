
def generate_word(n):
    if n < 2:
        return 'invalid'
    if n == 2:
        return 'b, a'
    groups = generate_word(n-1).split(', ')
    return '{}, {}{}'.format(generate_word(n-1), groups[-2], groups[-1])

