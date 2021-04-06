
def reverse_sort(txt):
  A=txt.split()
  B=sorted(A, key=lambda x:(len(x), x.lower()), reverse=True)
  return ' '.join(B)

