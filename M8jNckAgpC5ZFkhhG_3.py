
def reverse_complement(input_sequence):
  d = {"A":"U","G":"C","C":"G","U":"A"}
  s = ""
  for i in input_sequence:
    s += d[i]
  return s[::-1]

