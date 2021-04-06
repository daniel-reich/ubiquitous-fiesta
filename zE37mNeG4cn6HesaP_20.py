
def max_ham(s1, s2):
  if (len(s1) != len(s2)) or (len(set(s1+s2)) != len(set(s1))) or ((abs(len(set(s1)) - len(set(s2))) >= 1)):
    return False
  else:
    temp = sum(1 for i in range(len(s1)) if s1[i] != s2[i])
    if temp == len(s1):
      return True
    else:
      return temp

