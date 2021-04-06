
def reverse_complement(input_sequence):
  d = {
    "A" : "U",
    "U" : "A",
    "G" : "C",
    "C" : "G",
  }
  
  res = ""
  for c in input_sequence:
    res += d[c]
  return res[::-1]

