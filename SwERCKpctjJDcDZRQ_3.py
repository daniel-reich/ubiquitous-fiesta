
def longest_string(str1, str2):
  A=list(str1)
  for x in str2:
    if x not in A:
      A.append(x)
  return ''.join(sorted(set(A)))

