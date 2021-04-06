
def max_ham(s1, s2):
  set1,set2 = (set(s1),set(s2))
  if set1 != set2:
    return False
  else:
    count = 0
    for i in range(len(s1)):
      if s1[i] == s2[i]:
        count += 1
    if count >= 1:
      return len(s1)-count
    else:
      return True

