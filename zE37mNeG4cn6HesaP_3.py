
def max_ham(s1, s2):
  if sorted(s1) != sorted(s2):
    return False
  ham = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      ham += 1
  return True if ham == len(s1) else ham

