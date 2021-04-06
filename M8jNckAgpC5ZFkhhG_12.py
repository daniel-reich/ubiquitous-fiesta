
def reverse_complement(input_sequence):
  res = ''
  for letter in input_sequence[::-1]:
    if letter == 'A':
      res += 'U'
    elif letter == 'U':
      res += 'A'
    elif letter == 'G':
      res += 'C'
    elif letter == 'C':
      res += 'G'
  return res

