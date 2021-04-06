
def reverse_complement(input_sequence):
  result = list(input_sequence[::-1])
  result = ["A" if i == "U" else "U" if i == "A" else i for i in result]
  result = ["G" if i == "C" else "C" if i == "G" else i for i in result]
  return "".join(result)

