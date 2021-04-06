
def reverse_complement(input_sequence): 
    d = {'A':'U', 'U':'A', 'G':'C', 'C':'G'}
    return ''.join([d[x] for x in input_sequence][::-1])

