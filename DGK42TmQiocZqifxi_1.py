
def reverse_complement(input_sequence):
    rnr = {'A': 'U', 'U': 'A', 'G': 'C', 'C': 'G'}
    return ''.join([rnr[c] for c in input_sequence][::-1])

