
def reverse_complement(input_sequence):
    return input_sequence.translate(input_sequence.maketrans('AUGC','UACG'))[::-1]

