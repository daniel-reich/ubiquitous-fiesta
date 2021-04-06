
def reverse_complement(input_sequence):
  a = {"A": "U", "G": "C", "U": "A", "C": "G"}
  return "".join([i.replace(i, a[i]) for i in input_sequence])[::-1]

