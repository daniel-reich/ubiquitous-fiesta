
def generate_word(n, fw = None, a='b', b='a'):
    if not fw:
        if n < 2: return 'invalid'
        fw = a + ', ' + b
    return fw if n == 2 else generate_word(n-1, fw + ', ' + a + b, b, a + b)

