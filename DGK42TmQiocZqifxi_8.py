
def reverse_complement(i):
  return i.translate(str.maketrans('ACGU', 'UGCA'))[::-1]

