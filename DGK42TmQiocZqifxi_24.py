
def reverse_complement(input_sequence):
  return input_sequence.translate(str.maketrans("AUGC", "UACG"))[::-1]

