
def full_cycle(lst):
  if sorted(lst)==list(range(len(lst))):
    A=[lst[0]]
    while lst[A[-1]] not in A:
      A.append(lst[A[-1]])
    return len(A)==len(lst)
  else:
    return False

