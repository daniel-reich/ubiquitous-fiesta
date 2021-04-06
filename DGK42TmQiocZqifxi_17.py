
def reverse_complement(input_sequence):
  pairs = {('A', 'U'), ('C', 'G')}
  output_sequence = ''
  
  for letter in input_sequence:
    for pair in pairs:
      if letter in pair:
        if letter == pair[0]:
          output_sequence += pair[-1]
        else:
          output_sequence += pair[0]
  
  return output_sequence[::-1]

