
def recaman_index(n):
  sequence = [0]
  while sequence[-1] !=n:
    if sequence[-1]-len(sequence)>=0 and (sequence[-1]-len(sequence)) not in sequence :
      sequence.append(sequence[-1]-len(sequence))
    else:
      sequence.append(sequence[-1]+len(sequence))
  return sequence.index(n)

