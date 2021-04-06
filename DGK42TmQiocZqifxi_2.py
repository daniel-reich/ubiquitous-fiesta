
def reverse_complement(s):  
  return s[::-1].translate(str.maketrans('ACGU', 'UGCA'))

