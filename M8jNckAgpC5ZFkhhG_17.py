
def reverse_complement(i):
  return i.replace('A','X').replace('G','Y').replace('U','A').replace('C','G').replace('X','U').replace('Y','C')[::-1]

