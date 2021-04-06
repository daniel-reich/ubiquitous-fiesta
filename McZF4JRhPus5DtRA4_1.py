
mapping = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
​
def dna_to_rna (dna):
    return ''.join([mapping[c] for c in dna])

