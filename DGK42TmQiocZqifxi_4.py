
def reverse_complement(input_sequence):
  a = {"G":"C", "C":"G", "A":"U", "U":"A",}
  return "".join(a[i] for i in input_sequence)[::-1]

