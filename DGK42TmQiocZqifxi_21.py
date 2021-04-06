
def reverse_complement(input_sequence):
  translation = input_sequence.maketrans("AUGC", "UACG")
  return input_sequence.translate(translation)[::-1]

