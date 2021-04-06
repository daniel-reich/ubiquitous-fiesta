
def fibonacci_sequence():
  sequence = [0, 1]
  sum_sequence = sequence[0] + sequence[1]
  
  while sum_sequence < 255:
    sequence.append(sum_sequence)
    sum_sequence = sequence[-1] + sequence[-2]
    
  return sequence

