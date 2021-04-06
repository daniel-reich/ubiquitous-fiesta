
def shift_sentence(txt):
  A=txt.split()
  B=[x[0] for x in A]
  C=[x[1:] for x in A]
  D=[B[-1]+C[0]]
  E=[x+y for x, y in zip(B, C[1:])]
  return ' '.join(D+E)

