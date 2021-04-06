
def reverse_complement(s):
  return s.translate(s.maketrans("ACGU", "UGCA"))[::-1]

