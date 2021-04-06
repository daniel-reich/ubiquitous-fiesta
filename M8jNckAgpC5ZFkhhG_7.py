
def reverse_complement(input_sequence):
    a = list(input_sequence)
    for i in range(len(a)):
        if a[i] == 'A':
            a[i] = 'U'
            continue
        if a[i] == 'U':
            a[i] = 'A'
            continue
        if a[i] == 'G':
            a[i] = 'C'
            continue
        if a[i] == 'C':
            a[i] = 'G'
    return ''.join(a[::-1])

