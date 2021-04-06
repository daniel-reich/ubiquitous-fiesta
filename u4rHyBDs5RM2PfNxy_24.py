
def count_ones(lst):
    frase = ''
    for n in lst:
        frase += str(n)
    return len([i for i in frase.split('0') if len(i) >= 2])

