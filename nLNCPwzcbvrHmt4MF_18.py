
def fibonacci_sequence():
  sequence = [0,1]
  while sequence[-1] + sequence[-2]<255:
    sequence.append(sequence[-1] + sequence[-2])
  return sequence

