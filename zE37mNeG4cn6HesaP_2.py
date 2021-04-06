
def max_ham(s1, s2):
  count = 0
  if sorted(s1) != sorted(s2):
    return False
  else:
    for i in range(len(s1)):
      if s1[i]!=s2[i]:
        count+=1
    if count==len(s1):
      return True
    else:
      return count

