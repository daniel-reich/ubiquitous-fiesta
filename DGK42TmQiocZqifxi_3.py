
def reverse_complement(input_sequence): 
  return input_sequence[::-1].translate(str.maketrans("ACGU", "UGCA"))

