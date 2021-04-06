
def reverse_complement(input_sequence):
    my_dict = {'A':'U', 'U':'A', 'G':'C','C':'G'}
    string = ''
    for x in input_sequence:
        string += my_dict[x]
    return string[::-1]

