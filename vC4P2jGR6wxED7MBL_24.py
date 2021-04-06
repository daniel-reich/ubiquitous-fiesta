
def larger_than_right(n):
  return [base for i,base in enumerate(n) if all(base>n for n in n[i+1:])]

