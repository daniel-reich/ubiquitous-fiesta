
def reverse_complement(input_sequence):
  revStr = ""
  for i in range(len(input_sequence)):
    if input_sequence[i] == "A":
      revStr = "U" + revStr
    elif input_sequence[i] == "U":
      revStr = "A" + revStr
    elif input_sequence[i] == "C":
      revStr = "G" + revStr
    else:
      revStr = "C" + revStr
  return revStr

