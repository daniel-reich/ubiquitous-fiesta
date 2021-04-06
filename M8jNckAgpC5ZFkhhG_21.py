
def reverse_complement(input_sequence):
    x=input_sequence.translate(input_sequence.maketrans('AGCU','UCGA'))
    return x[::-1]

