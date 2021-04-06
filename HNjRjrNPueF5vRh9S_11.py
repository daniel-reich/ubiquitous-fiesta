
#ONE LINE CODE
def hamming_code(m):
  return ''.join([''.join(q) for q in [[z*3 for z in(bin(ord(i))[2:].zfill(8))] for i in m]])

