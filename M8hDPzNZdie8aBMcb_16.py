
def count_substring(s):
  count=0
  for i in range(len(s)-1):
    if s[i]=='A':
      for j in range(i,len(s)):
        if s[j]=='X':
          count+=1
  return count

