
def reverse_complement(input_sequence):
  t = ""
  for c in input_sequence:
    if c == 'G':
      t += 'C'
    elif c == 'C':
      t += 'G'
    elif c == 'A':
      t += 'U'
    elif c == 'U':
      t += 'A'
  return t[::-1]

