
def generate_word(num, a='b', b='a', res='b, a'):
    if num < 2:
        return 'invalid'
    a, b = b, a + b
    res += ', {}'.format(b)
    num -= 1
    return res if num == 2 else generate_word(num, a, b, res)

