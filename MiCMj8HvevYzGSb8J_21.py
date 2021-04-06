
def fibo_word(n):
    out = ['b', 'a']
    for _ in range(n-2):
        out.append(out[-1] + out[-2])
    return ', '.join(out) if n > 1 else 'invalid'

